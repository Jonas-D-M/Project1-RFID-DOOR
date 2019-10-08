import time
import RPi.GPIO as GPIO
from keypad import keypad
import lcd_driver

GPIO.setwarnings(False)

lcd = lcd_driver.lcd()

if __name__ == '__main__':
    # Initialize
    kp = keypad()
    lcd.lcd_clear()
    lcd.lcd_display_string('Enter pin: ',1)

    # waiting for a keypress
    while True:
        digit = None
        while digit == None:
            digit = kp.getKey()
        # Print result
        print(digit)
        time.sleep(0.5)

    ###### 4 Digit wait ######
    # pw = ''
    # seq = []
    # for i in range(4):
    #     digit = None
    #     while digit == None:
    #         digit = kp.getKey()
    #     seq.append(digit)
    #     pw = ''.join(seq[i])
    #     print(pw)
    #     lcd.lcd_display_string(pw, 2)
    #     time.sleep(0.4)
    #
    # # Check digit code
    # print(seq)
    # if seq == [1, 2, 3, '#']:
    #     print("Code accepted")

