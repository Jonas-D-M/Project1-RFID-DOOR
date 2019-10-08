#!/usr/bin/python3

from RPi import GPIO


class Magnet:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.pin = 27
        self.setup = GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, 1)

    def off(self):
        GPIO.output(self.pin, 0)

