from mfrc522 import SimpleMFRC522
from componentClasses import lcd_driver
from Database import Database
from flask import Flask
from flask_cors import CORS
from time import sleep
from random import randint
from keypad import keypad
from datetime import datetime
import threading

import RPi.GPIO as GPIO
app = Flask(__name__)
CORS(app)

GPIO.setmode(GPIO.BCM)

lcd = lcd_driver.lcd()
reader = SimpleMFRC522()
conn = Database(app, 'mct', 'mct', 'project', '192.168.0.10')
kp = keypad()


# reads rfid card to unlock door
def scan_unlock():
    while True:
        print('READY FOR SCAN')
        try:
                # clear screen and display welcome message
                lcd.lcd_clear()
                lcd.lcd_display_string('SCAN 2 UNLOCK', 1, 1)

                # call reader to read id from rfid card
                card_id, text = reader.read()
                print('ID: ')
                print(card_id)

                # make call to db with id from card to know if user is authorized
                response = (conn.get_data('select first_name, id_user from project.user where card_id='+str(card_id)))
                print('Result: ')
                print(response)

                # if user is not authorized:
                if not response:
                    lcd.lcd_clear()
                    lcd.lcd_display_string('ACCESS DENIED!')
                    print('UNAUTHORIZED USER TRIED TO OPEN DOOR!')
                # if user is authorized
                else:
                    sleep(0.01)
                    lcd.lcd_clear()
                    lcd.lcd_display_string('WELCOME:', 1)

                    name = ''.join([d['first_name'] for d in response])
                    lcd.lcd_display_string(name, 2)
                    print('welcome')
                    print('name: ' + name)

                    UID = ''.join(str([d['id_user'] for d in response]).strip('[]'))
                    print('id_user: ' + UID)

                    conn.set_data('insert into project.history(locked, user_id_user, Sensor_id_sensor)VALUES(0, %s, 2)' % UID)
                    print('USER OPENED DOOR!')
        except Exception as e:
            print(e)

        finally:
            GPIO.cleanup()
            lcd.lcd_clear()


# to do: close pw with # to end pw input
def pw_unlock():
    while True:
        print('READY FOR PW UNLOCK')
        lcd.lcd_clear()
        lcd.lcd_display_string('ENTER PIN:')

        # set empty password variable
        pw = ''
        star = ''
        master_pw = '*98#'
        while len(pw) < 4:
            digit = None
            while digit == None:
                digit = kp.getKey()
                if digit:
                    pw = pw + str(digit)[0]
                    star += '*'
                    sleep(0.4)
            lcd.lcd_display_string(star,2)
        print(pw)

        if pw == master_pw:
            print('MASTER PASSWORD USED @ ' + str(datetime.now().time()))
            lcd.lcd_clear()
            lcd.lcd_display_string('SCAN CARD FOR ID', 1)
            cid, text = reader.read()
            lcd.lcd_display_string(str(cid), 2)
            sleep(5)
            lcd.lcd_clear()

        else:
            # Check digit code
            response = (conn.get_data('select first_name, id_user from project.user where password=' + str(pw)))
            if not response:
                lcd.lcd_clear()
                lcd.lcd_display_string('ACCES DENIED!')
                print(datetime.now().time())
                print('UNAUTHORIZED PERSON TRIED TO OPEN DOOR!')

            else:
                lcd.lcd_clear()

                name = ''.join([d['first_name'] for d in response])
                lcd.lcd_display_string('WELCOME',1)
                lcd.lcd_display_string(name, 2)
                print('welcome')
                print('name: ' + name)

                UID = ''.join(str([d['id_user'] for d in response]).strip('[]'))
                print('id_user: ' + UID)

                # set data in db history table
                conn.set_data('insert into project.history(locked, user_id_user, Sensor_id_sensor)VALUES(0, %s, 3)' % UID)

                # print time when door opened
                print(datetime.now().time())
                print('USER OPENED DOOR!')


# code to gen random password for user based on card_id
def gen_pw(card_id):
    sci = str(card_id)
    print('Card_id: ')
    print(sci)
    print('length of card_id: ')
    lci = len(sci)
    print(lci)

    pw = ''

    for i in range(0, 4):
        randy = randint(1, 13)
        pw += sci[randy]

    print('password is: '+pw)

t1 = threading.Thread(target=pw_unlock)
t2 = threading.Thread(target=scan_unlock)
t1.start()
t2.start()
if __name__ == '__main__':
        app.run('0.0.0.0', 5000)
