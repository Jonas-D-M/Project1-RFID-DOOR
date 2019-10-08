from RPi import GPIO

magnet = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(magnet, GPIO.OUT)
GPIO.output(magnet, True)

