from componentClasses import lcd_driver
import socket
import time

mylcd = lcd_driver.lcd()


def get_ip_address():
 ip_address = ''
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(("8.8.8.8",80))
 ip_address = s.getsockname()[0]
 s.close()
 return ip_address
try:
    while True:
        mylcd.lcd_display_string("IP: ",1)
        mylcd.lcd_display_string(get_ip_address(), 2)
        time.sleep(5.0)  # Wait 5 seconds
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Jonas",1)
        mylcd.lcd_display_string("De Meyer",2)
        time.sleep(5.0)
        mylcd.lcd_clear()
except:
    mylcd.lcd_clear()
