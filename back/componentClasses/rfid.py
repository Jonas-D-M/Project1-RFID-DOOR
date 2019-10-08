import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    text = input('New data:')
    print("Now place your tag to write")
    reader.write(text)
    print("Written")


except Exception as e:
    print(e)


finally:
    GPIO.cleanup()


