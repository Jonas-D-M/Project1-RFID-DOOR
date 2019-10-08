import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(26) == GPIO.HIGH:
            print("Button was pushed!")
except Exception as e:
    print(e)
finally:
    GPIO.cleanup()
