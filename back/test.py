# from mfrc522 import SimpleMFRC522
# from keypad import keypad
# from time import sleep
# from RPi import GPIO
# import multiprocessing
#
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# kp = keypad()
# reader = SimpleMFRC522()
# # conn = Database(app, 'mct', 'mct', 'project')
# status = 1
#
#
# # reads RFID card to unlock door - T
# def scan():
#     try:
#         cid = reader.read_id_no_block()
#         return cid
#     except Exception as e:
#         print(e)
#
#
# def scan_unlock():
#     print('SCAN_UNLOCK() started')
#     global status
#     try:
#         print('ready for scan')
#         while True:
#             while status == 1:
#                 sleep(2)
#                 cid = scan()
#                 print(cid)
#                 if cid is not None:
#                     print('Dit is het gescande ID: ' + str(cid))
#                     sleep(2)
#                     status = 0
#                     print(status)
#
#     except Exception as e:
#         print(e)
#     finally:
#         print('scan_unlock says bye')
#         GPIO.cleanup()
#
#
# # wait for keypad presses then pw_unlock will start
#
#
# # to do: close pw with # to end pw input - T
# def pw_unlock():
#
#     try:
#         global status
#         print('PW_UNLOCK() STARTED')
#         print('Enter pin:')
#         while True:
#             pw = ''
#             master_pw = ['*', 9, 8, '#']
#
#             pw = []
#             for i in range(4):
#                 digit = None
#                 while digit is None:
#                     digit = kp.getKey()
#                 pw.append(digit)
#                 sleep(0.4)
#
#             print(pw)
#             if pw == master_pw:
#                 status = 0
#                 print(status)
#                 while status == 0:
#                     sleep(1)
#                     cid = scan()
#                     if cid is not None:
#                         print('Register with this id: ' + str(cid))
#                         print('Sleeping for 2 sec')
#                         sleep(2)
#                         status = 1
#                 print('[Completed card registration]')
#                 print(status)
#             else:
#                     print('welcome')
#                     print('USER OPENED DOOR!')
#     except Exception as e:
#         print(e)
#
#     finally:
#         print('pw_unlock says bye')
#         GPIO.cleanup()
#
# print(status)
# # t2 = threading.Thread(target=pw_unlock).start()
# # t1 = threading.Thread(target=scan_unlock).start()
# p2 = multiprocessing.Process(target=pw_unlock)
# p2.start()
# p1 = multiprocessing.Process(target=scan_unlock)
# p1.start()
#
#

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)


if __name__ == '__main__':
    socketio.run(app)

