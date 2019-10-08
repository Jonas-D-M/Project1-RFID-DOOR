import lcd_driver
import socket
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

mylcd = lcd_driver.lcd()
reader = SimpleMFRC522()

try:

    while True:
        id, text = reader.read()
        print(text)
        mylcd.lcd_display_string("Welkom: ",1)
        mylcd.lcd_display_string(str(text).strip(" ").strip("\r\n"), 2)
finally:
    GPIO.cleanup()
