#!/usr/bin/python3

from componentClasses.Database import database
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from random import randint
from componentClasses.hwinterface import HWInterface
import multiprocessing
import json
from time import sleep


app = Flask(__name__)
CORS(app)
conn = database(app, 'mct', 'mct', 'project')
socket = SocketIO(app)

# database connectie
# endpoint
endp = '/api/'


# ---------------
# ROUTES
# ---------------
@app.route('/')
def hallo():
    return "Server is running"


# Gets history from db
@app.route(endp + 'history', methods=['GET'])
def history():
    if request.method == 'GET':
        return jsonify(conn.get_data('select lock_time, locked, user.first_name, user.last_name, user.gender from history  join user on user.id_user=history.user_id_user order by lock_time desc'))
    else:
        jsonify(status='WRONG INPUTS'), 400


# Gets registered users from db
@app.route(endp + 'users', methods=['GET'])
def users():
    if request.method == 'GET':
        return jsonify(conn.get_data('SELECT first_name, last_name, gender FROM project.user;'))


# Post data when user registers
@app.route(endp + 'user', methods=['POST'])
def user():
    if request.method == 'POST':
        data = request.get_json()
        user = conn.set_data(
              'insert into user (first_name, last_name, card_id, gender, password) values (%s, %s, %s, %s, %s)',
              [data['first_name'], data['last_name'], data['card_id'], data['gender'], gen_pw()])
        print('succes')
        pw = conn.get_data('SELECT password from project.user order by id_user desc limit 1;')[0]
        return jsonify(pw)


# Get status about door
@app.route(endp + 'status', methods=['GET'])
def status():
    if request.method == 'GET':
        return jsonify(conn.get_data('select locked from project.history order by id_history desc limit 1'))
    else:
        return jsonify(status='WRONG API CALL'), 422


# @socket.on('status')
# def send_status():
#     socket.emit('send_status', json.dumps(conn.get_data('SELECT locked FROM project.history order by lock_time desc limit 1;')[0]))
#
#
# @socket.on('connect')
# def connect():
#     print('Client connected')
#


def gen_pw():
    pw = ''
    for i in range(0, 4):
        randy = randint(0, 9)
        pw += str(randy)
    return pw


def callback():
    test = socket.emit('send_status', json.dumps(conn.get_data('SELECT locked FROM project.history order by lock_time desc limit 1;')[0]))
    print('Dit is socket:          ')
    print(test)
    print('----------------')


if __name__ == '__main__':
    hw = HWInterface()
    p1 = multiprocessing.Process(target=hw.scan_unlock, args=(callback,))
    p2 = multiprocessing.Process(target=hw.pw_unlock)
    p3 = multiprocessing.Process(target=hw.lock)
    p1.start()
    p2.start()
    p3.start()
    print('')
    print('---BACK-END IS UP AND RUNNING---')
    print('')
    # app.run(debug=True)
    socket.run(app, host='0.0.0.0', port=5000, use_reloader=0)

