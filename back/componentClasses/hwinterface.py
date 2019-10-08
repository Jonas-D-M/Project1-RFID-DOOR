#!/usr/bin/python3

from mfrc522 import SimpleMFRC522
from time import sleep
from componentClasses.keypad import Keypad
from componentClasses.magnet import Magnet
from componentClasses.lcd_driver import lcd
from componentClasses.button import Button
from subprocess import check_output
from RPi import GPIO
import mysql.connector
import socket
import json
from multiprocessing import Process, Event

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class HWInterface:
    def __init__(self):

        self.reader = SimpleMFRC522()
        self.lcd = lcd()
        self.kp = Keypad()
        self.magnet = Magnet()
        self.magnet.on()
        self.mydb = mysql.connector.connect(host='localhost', user='mct', passwd='mct', database='project')
        self.mycursor = self.mydb.cursor()
        self.dbout = []

        self.event_scan = Event()
        self.event_scan.set()
        self.event_open = Event()

        self.lcd.lcd_display_string(self.get_ip_address(), 1)
        self.lcd.lcd_display_string('Scan or use PIN', 2)

        self.btn = Button(26)
        self.btn.pressed = False


    def scan(self):
        cid = self.reader.read_id_no_block()
        return cid

    def scan_unlock(self, callback):
        GPIO.setmode(GPIO.BCM)
        print('SCAN_UNLOCK() started')
        try:
            while True:
                self.event_scan.wait()
                while self.event_scan.is_set():
                    sleep(1)
                    cid = self.scan()
                    if cid is not None:
                        name, uid = self.user_in_db_scan(cid)
                        self.lcd.lcd_clear()
                        if uid is not None:
                            self.magnet.off()
                            self.lcd.lcd_display_string('Welkom:', 1)
                            self.lcd.lcd_display_string(name, 2)
                            self.db_add_event(0, uid, 2)
                            callback()
                            sleep(3)
                            self.lcd.lcd_clear()
                            self.lcd.lcd_display_string(self.get_ip_address(), 1)
                            self.lcd.lcd_display_string('OPENED', 2)
                            self.event_open.set()

                        else:
                            self.lcd.lcd_display_string('ACCESS DENIED', 1)
                            sleep(3)
                            self.lcd.lcd_clear()
                            self.lcd.lcd_display_string(self.get_ip_address(), 1)
                            self.lcd.lcd_display_string('Scan or use PIN', 2)

        except KeyboardInterrupt:
            print('Quit')
        finally:
            print('scan_unlock says bye')
            self.lcd.lcd_clear()
            GPIO.cleanup()

    def pw_unlock(self):
        GPIO.setmode(GPIO.BCM)
        try:
            print('PW_UNLOCK() STARTED')
            while True:
                master_pw = ['*', 9, 8, '#']
                star = ''
                pw = []
                for i in range(4):
                    digit = None
                    while digit is None:
                        digit = self.kp.getKey()

                    star += '*'
                    sleep(0.2)
                    self.lcd.lcd_clear()
                    self.lcd.lcd_display_string('Enter pin:', 1)
                    self.lcd.lcd_display_string(star, 2)
                    pw.append(digit)
                    sleep(0.3)
                    print(digit)

                if pw == master_pw:
                    self.event_clearer()
                    self.lcd.lcd_clear()
                    self.lcd.lcd_display_string('Scan card:')
                    cid = self.scan()
                    while cid is None:
                        sleep(1)
                        cid = self.scan()
                        if cid is not None:
                            self.lcd.lcd_clear()
                            self.lcd.lcd_display_string('Card id: ', 1)
                            self.lcd.lcd_display_string(str(cid), 2)
                            sleep(10)
                    self.lcd.lcd_clear()
                    self.lcd.lcd_display_string('CONFIRMED', 1)
                    self.lcd.lcd_clear()
                    self.event_setter()
                    self.lcd.lcd_display_string(self.get_ip_address(), 1)
                    self.lcd.lcd_display_string('Scan or use PIN', 2)
                else:
                    p_pw = ''
                    for i in range(0, len(pw)):
                        p_pw += str(pw[i])
                    name, uid = self.user_in_db_pw(p_pw)
                    self.lcd.lcd_clear()
                    if uid is not None:
                        self.magnet.off()
                        self.lcd.lcd_display_string('Welkom:', 1)
                        self.lcd.lcd_display_string(name, 2)
                        self.db_add_event(0, uid, 3)
                        # self.btn.pressed = False
                        sleep(3)
                        self.lcd.lcd_clear()
                        self.lcd.lcd_display_string(self.get_ip_address(), 1)
                        self.lcd.lcd_display_string('OPEN', 2)
                        self.event_open.set()
                    else:
                        self.lcd.lcd_display_string('ACCESS DENIED', 1)
                        sleep(3)
                        self.lcd.lcd_clear()
                        self.lcd.lcd_display_string(self.get_ip_address(), 1)
                        self.lcd.lcd_display_string('Scan or use PIN', 2)

        except KeyboardInterrupt:
            print('Quit')

        finally:
            print('pw_unlock says bye')
            self.lcd.lcd_clear()
            GPIO.cleanup()

    def lock(self):
        try:
            self.btn.on_release(self.btn.call)
            while True:
                self.event_open.wait()
                while self.event_open.is_set() and GPIO.input(26):
                    if self.btn.pressed is True:
                        print('setting magnet on in 3 sec')
                        self.db_add_event(1, self.user_closes_door(), 1)
                        sleep(3)
                        self.magnet.on()
                        self.event_open.clear()
                        self.db_last_opened()
                        self.lcd.lcd_clear()
                        self.lcd.lcd_display_string(self.get_ip_address(), 1)
                        self.lcd.lcd_display_string('Scan or use PIN', 2)

        except KeyboardInterrupt:
            print('Quit')
        finally:
            GPIO.cleanup()
            self.lcd.lcd_clear()

    def user_in_db_scan(self, p_cid):
        name = ''
        user_id = ''
        self.mycursor.execute('select first_name, id_user from project.user where card_id=%d' % p_cid)
        myresult = self.mycursor.fetchall()
        if not myresult:
            name = None
            user_id = None
            return name, user_id
        for x in myresult:
            name = x[0]
            user_id = x[1]
        return name, user_id

    def user_in_db_pw(self, p_pw):
        name = ''
        user_id = ''
        if '*' in p_pw:
            return None
        elif'#' in p_pw:
            return None
        else:
            self.mycursor.execute('select first_name, id_user from project.user where password='+str(p_pw))
            myresult = self.mycursor.fetchall()
            if not myresult:
                name = None
                user_id = None
                return name, user_id
            for x in myresult:
                print(myresult)
                name = x[0]
                print(name)
                user_id = x[1]
                print(user_id)
            return name, user_id

    def user_closes_door(self):
        self.mycursor.execute('select user_id_user from history order by lock_time desc limit 1;')
        myresult = self.mycursor.fetchall()
        if not myresult:
            user_id = None
            return user_id
        for x in myresult:
            user_id = x[0]
            return user_id

    def db_last_opened(self):
        pass

    def event_setter(self):
        self.event_scan.set()

    def event_clearer(self):
        self.event_scan.clear()

    def db_add_event(self, p_state, p_uid, p_sensor):
        sql = "insert into project.history(locked, user_id_user, Sensor_id_sensor) VALUES(%s, %s, %s);"
        val = (p_state, p_uid, p_sensor)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    @staticmethod
    def get_ip_address():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address

    @staticmethod
    def get_ip_addresses():
        ips = check_output(['hostname', '--all-ip-addresses'])
        ips = str(ips)[2:len(ips) - 3]
        list_ips = ips.split(" ")
        return list_ips
