from mfrc522 import SimpleMFRC522
# from keypad import keypad
from RPi import GPIO
import mysql.connector
from componentClasses.button import Button
from random import randint

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# kp = keypad()
reader = SimpleMFRC522()
# conn = Database(app, 'mct', 'mct', 'project', '192.168.0.10')
# status = 1
#
#
# def scan():
#     try:
#         id = reader.read_id_no_block()
#         if id is None:
#             return None
#         return id
#     except Exception as e:
#         print(e)
#
#
# def scan_unlock():
#     print('SCAN_UNLOCK() started')
#     try:
#         print('ready for scan')
#         while True:
#             if status != 0:
#                 id = scan()
#                 if id is not None:
#                     print('Dit is het gescande ID: ' + str(id))
#                     sleep(2)
#
#     except Exception as e:
#         print(e)
#     finally:
#         print('scan_unlock says bye')
#         GPIO.cleanup()
#
# print(status)
# # t3 = threading.Thread(target=scan).start()
# # t2 = threading.Thread(target=pw_unlock).start()
# # t1 = threading.Thread(target=scan_unlock).start()
#
# while True:
#     print(scan())
#     sleep(1)


# arr = [1,2,3,4]
# print(arr)
# stri = ''
# for i in range(0, len(arr)):
#     stri += str(arr[i])
#     print(arr[i])
#
# print(stri)
# test = '1' + '1'
# print(test)
# try:
#     while True:
#         magnet = 27
#         magnet_value = 1
#         GPIO.setup(magnet, GPIO.OUT)
#         GPIO.output(magnet, magnet_value)
# except Exception as e:
#     print(e)
# finally:
#     GPIO.cleanup()

mydb = mysql.connector.connect(host='localhost', user='mct', passwd='mct', database='project')
mycursor = mydb.cursor()
#
#
# mycursor.execute(
# 'select first_name, id_user from project.user where card_id=2522002321870'
# )
#
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
#     print(x[0])
#
# print(myresult)
# if not myresult:
#     print('tis niks')


# pw = [1,2,3,4]
# p_pw = ''
# print(len(pw))
# for i in range (0, len(pw)):
#     p_pw += str(pw[i])
# print(p_pw)

# par = True
#
# def test3():
#     if event.is_set():
#         event.clear()
#     else:
#         event.set()
#
# def test2():
#     event.set()
#     for i in range(0,2):
#         test3()
#
# def test():
#     event.wait()
#     while event.is_set():
#         print('dit werkt')
#         sleep(1)
#     print('stopped')
#
#
#
#
# event = multiprocessing.Event()
# p1 = multiprocessing.Process(target=test)
# p2 = multiprocessing.Process(target=test2)
# p3 = multiprocessing.Process(target=test3)
# p3.start()
# p2.start()
# p1.start()
# p3.join()
# p2.join()
# p1.join()
# event.set()


# import queue
# import numpy as np
#
# def flag(event):
#     sleep(3)
#     event.set()
#     print('starting countdwon')
#     sleep(7)
#     print('event is cleared')
#     event.clear
#
# def start_operations(event):
#     event.wait()
#     while event.is_set():
#         print('starting random integer task')
#         x = np.random.randint(1,30)
#         sleep(0.5)
#         if x == 29:
#             print('True')
#     print('event has been cleared, random operation stops')
#
# event = None
# def my_setup(event_):
#   global event
#   event = event_
#   print "event is %s in child" % event
#
# if __name__ == "__main__":
#
#     event = multiprocessing.Event()
#     p1 = multiprocessing.Process(target=flag, args=event)
#     p2 = multiprocessing.Process(target=start_operations, args=event)
#     p1.start()
#     p2.start()
#
# import time
# import multiprocessing
#
#
# def event_func():
#     print('\t%r is waiting' % multiprocessing.current_process())
#     event.wait()
#     while event.is_set():
#         print('jeeps')
#         sleep(1)
#
#
# def event_sett():
#     print('event_setter is sleeping now')
#     sleep(5)
#     print('event setter has awoken')
#     event.set()
#     sleep(5)
#     event.clear()
#
# # if __name__ == "__main__":
# event = multiprocessing.Event()
#
# # pool = multiprocessing.Pool()
# # a = pool.map_async(event_func, [i for i in range(pool._processes)])
#
# p = multiprocessing.Process(target=event_func)
# p1 = multiprocessing.Process(target=event_sett)
# p1.start()
# p.start()
# # print('main is sleeping')
# time.sleep(2)

# print('main is setting event')
# event.set()

# pool.close()
# pool.join()
# p.join()

# test = '****'
# if '#' and '*' in test:
#     print('chill')


# user_id = 1
# sql = "insert into project.history(locked, user_id_user, Sensor_id_sensor) VALUES(%s, %s, %s);"
# val = (0, user_id, 3)
# mycursor.execute(sql, val)
# mydb.commit()
# dbout = []
# for x in mycursor:
#     dbout.append(x)
#     print(x)
#
# def test(p_cid):
#     name = ''
#     user_id = ''
#     mycursor.execute('select first_name, id_user from project.user where card_id=%d' % p_cid)
#     myresult = mycursor.fetchall()
#     if not myresult:
#         name = None
#         user_id = None
#         return name, user_id
#     for x in myresult:
#         name = x[0]
#         user_id = x[1]
#     return name, user_id
#
# name, uid = test(1)
#
# if name is not None:
#     print('chill')









# -------------------------------------------------------------- from app.py--------------------------------------------
# Used to scan
# def scan():
#     try:
#         cid = reader.read_id_no_block()
#         return cid
#     except Exception as e:
#         print(e)


# # reads RFID card to unlock door - T
# def scan_unlock():
#     print('scan_unlock started')
#     try:
#         while True:
#             while status == 1:
#                 print("dit is de status " + status)
#                 sleep(2)
#                 cid = scan()
#                 print(cid)
#                 if cid is not None:
#                     response = (conn.get_data('select first_name, id_user from project.user where card_id=' + str(cid)))
#                     print('Result: ')
#                     print(response)
#
#                     # if user is not authorized:
#                     if not response:
#                         sleep(0.01)
#                         lcd.lcd_clear()
#                         lcd.lcd_display_string('ACCESS DENIED!')
#                         print('UNAUTHORIZED USER TRIED TO OPEN DOOR!')
#                         lcd.lcd_clear()
#                         lcd.lcd_display_string(get_ip_address(), 1)
#                         lcd.lcd_display_string('LOCKER', 2)
#                     # if user is authorized
#                     else:
#                         sleep(0.01)
#                         lcd.lcd_clear()
#                         lcd.lcd_display_string('WELCOME:', 1)
#
#                         name = ''.join([d['first_name'] for d in response])
#                         lcd.lcd_display_string(name, 2)
#                         print('welcome')
#                         print('name: ' + name)
#
#                         UID = ''.join(str([d['id_user'] for d in response]).strip('[]'))
#                         print('id_user: ' + UID)
#                         GPIO.output(magnet, 0)
#                         conn.set_data('insert into project.history(locked, user_id_user, Sensor_id_sensor)VALUES(0, %s, 2)' % UID)
#                         print('USER OPENED DOOR!')
#                         lcd.lcd_display_string(get_ip_address(), 1)
#                         lcd.lcd_display_string('LOCKER (OPEN)', 2)
#
#     except Exception as e:
#         print(e)
#
#     finally:
#         print('scan_unlock says bye')
#         GPIO.cleanup()

# wait for keypad presses then pw_unlock will start
# def flag():
#     digit = None
#     while digit is None:
#         print('waiting for keypress')
#         digit = kp.getKey()
#
#     if digit is not None:
#         print(digit)
#         return event.set()
#         print(event)
#

# to do: close pw with # to end pw input - T

# def pw_unlock():
#     GPIO.setmode(GPIO.BCM)
#     while True:
#         print('pw_unlock started')
#         GPIO.setmode(GPIO.BCM)
#         print('READY FOR PASSWORD')
#         try:
#             # set empty password variable
#             pw = ''
#             star = ''
#             master_pw = '*98#'
#             while len(pw) < 4:
#                 digit = None
#                 while digit is None:
#                     digit = kp.getKey()
#                     if digit:
#                         lcd.lcd_clear()
#                         lcd.lcd_display_string('ENTER PIN:')
#                         pw = pw + str(digit)[0]
#                         star += '*'
#                         sleep(0.2)
#                 lcd.lcd_display_string(star, 2)
#             print(pw)
#
#             if pw == master_pw:
#                 print('MASTER PASSWORD USED')
#                 lcd.lcd_clear()
#                 lcd.lcd_display_string('SCAN CARD FOR ID', 1)
#                 cid, text = reader.read()
#                 lcd.lcd_display_string(str(cid), 2)
#                 sleep(5)
#                 lcd.lcd_clear()
#
#             else:
#                 # Check digit code
#                 response = (conn.get_data('select first_name, id_user from project.user where password=' + str(pw)))
#                 if not response:
#                     lcd.lcd_clear()
#                     lcd.lcd_display_string('ACCESS DENIED!')
#                     print('UNAUTHORIZED PERSON TRIED TO OPEN DOOR!')
#                     sleep(5)
#
#                 else:
#                     lcd.lcd_clear()
#                     name = ''.join([d['first_name'] for d in response])
#                     print('welcome')
#                     print('name: ' + name)
#                     UID = ''.join(str([d['id_user'] for d in response]).strip('[]'))
#                     print('id_user: ' + UID)
#                     # set data in db history table
#                     conn.set_data('insert into project.history(locked, user_id_user, Sensor_id_sensor)'
#                                   'VALUES(0, %s, 3)' % UID)
#                     print('USER OPENED DOOR!')
#                     lcd.lcd_display_string('WELCOME', 1)
#                     lcd.lcd_display_string(name, 2)
#                     sleep(5)
#                     lcd.lcd_display_string(get_ip_address(), 1)
#                     lcd.lcd_display_string('LOCKER (OPEN)', 2)
#         except Exception as e:
#             print(e)
#
#         finally:
#             print("Testen of da henk gelijk heeft keypad")


# function to gen random password for user based on card_id
# def gen_pw(card_id):
#
#     sci = str(card_id)
#     print('Card_id: ')
#     print(sci)
#     print('length of card_id: ')
#     lci = len(sci)
#     print(lci)
#
#     pw = ''
#
#     for i in range(0, 4):
#         randy = randint(1, 13)
#         pw += sci[randy]
#
#     return pw


# function for getting ip address of pi
# def get_ip_address():
#     ip_address = ''
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.connect(("8.8.8.8", 80))
#     ip_address = s.getsockname()[0]
#     s.close()
#     return ip_address


# function for putting voltage on gpio pin to toggle magnet on or off
# def magnet_toggle(value):
#     GPIO.output(magnet, value)


# display startup text
# lcd.lcd_display_string(get_ip_address(), 1)
# lcd.lcd_display_string('LOCKER', 2)


# # make threads and start them
# t1 = threading.Thread(target=scan_unlock)
# t1.start()
# # event2 = threading.Event()
# # t2 = threading.Thread(target=pw_unlock)
#
# p1 = multiprocessing.Process(target=hw.scan_unlock)
# p1.start()
# p2 = multiprocessing.Process(target=hw.pw_unlock)
# p2.start()

btn = Button(26)
def klikt():
    print('klik')


def gen_pw():
    pw = ''
    for i in range(0, 4):
        randy = randint(0, 9)
        pw += str(randy)
    print(pw)
    return str(pw)
gen_pw()
gen_pw()
gen_pw()
gen_pw()
gen_pw()
gen_pw()
gen_pw()
gen_pw()
gen_pw()
gen_pw()
gen_pw()
gen_pw()