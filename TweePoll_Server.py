import TweePoll_API_single
from flask import Flask, request, render_template, session
from flask_socketio import SocketIO, emit
from time import sleep
import threading
from threading import Thread, Event
import eventlet
import json
from random import random
eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)

# tweepy thread (?)
thread = Thread()
thread_stop_event = Event()

def SocketConnect():
	while not thread_stop_event.isSet():
		streamer = TweePoll_API_single.MyStreamListener()
		output = streamer.main(v + " @realDonaldTrump", v + " @JoeBiden")
		print(output)
		socketio.emit('data', {'output':output}, namespace='/output')
		socketio.sleep(5)

# def randomNumberGenerator():
#     """
#     Generate a random number every 1 second and emit to a socketio instance (broadcast)
#     Ideally to be run in a separate thread?
#     """
#     #infinite loop of magical random numbers
#     print("Making random numbers")
#     while not thread_stop_event.isSet():
#         number = round(random()*10, 3)
#         print(number)
#         socketio.emit('newnumber', {'number': number}, namespace='/output')
#         socketio.sleep(5)

@app.route('/', methods = ['GET','POST'])
def index():
	return(render_template("index.html", async_mode = socketio.async_mode))
	
@socketio.on('connect', namespace='/output')
def test_connect():
	global thread
	print('Client connected')
	if not thread.is_alive():
		print("Starting Thread")
		thread = socketio.start_background_task(SocketConnect)
		#thread = socketio.start_background_task(randomNumberGenerator)

@socketio.on('json')
def handle_json(json):
	global v
	v = message
	print('received message: ' + message)

@socketio.on('json')
def handle_json(json):
	global v
	v = message
	print('received message: ' + message)

@app.route('/output', methods = ['POST'])
def inputs():
	if request.method == "POST":
		global v
		v = request.form['variable']
		print(v)
	return(render_template("out.html", async_mode = socketio.async_mode))

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
	print('Client disconnected')

if __name__ == '__main__':
	#app.run(port = 5000, debug = True)
	#print(threading.current_thread.__module__)
	socketio.run(app, port = 5000, debug = True)