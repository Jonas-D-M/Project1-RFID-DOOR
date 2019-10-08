#!/usr/bin/env python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

reader = SimpleMFRC522()


try:
    while True:
        id = reader.read_id()
        print(id)
except Exception as e:
    print(e)

finally:
    GPIO.cleanup()
    print('bye')
