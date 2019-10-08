from RPi import GPIO

GPIO.setmode(GPIO.BCM)


class Button:
    def __init__(self, pin, bouncetime=None):
        self.pin = pin
        self.pressed = False
        self.prev_value = 1
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    def on_release(self, my_callback):
        GPIO.add_event_detect(self.pin, GPIO.BOTH, callback=my_callback, bouncetime=200)

    def call(self, pin):
        print(GPIO.input(pin))
        if GPIO.input(pin) is not self.prev_value and GPIO.input(pin) == 0:
            # Button is pressed
            self.prev_value = GPIO.input(26)
            print('druk')
            self.pressed = True

        else:
            self.prev_value = 1
            self.pressed = False
            print(self.pressed)


# btn = Button(26)
# vorige_waarde = 0
#
# btn.on_release(btn.call)
# while True:
#     pass

    # def wait_for_press(self, timeout=None):
    #     GPIO.wait_for_edge(self.pin, GPIO.RISING)
    #     print('gedrukt')
    #
    # def amount_pressed(self, channel):
    #     self.pressed += 1
    #     print("Er is {0} keer op de joystick gedrukt!".format(self.pressed))
    #
    # def on_press(self):
    #     GPIO.add_event_detect(self.pin, GPIO.FALLING)
    #
    # def add_callback(self, my_callback):
    #     GPIO.add_event_callback(self.pin, my_callback)
