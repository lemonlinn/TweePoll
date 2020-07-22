#import eventlet
#eventlet.monkey_patch(socket=True)
import gevent.monkey
gevent.monkey.patch_all()

import TweePoll_API_single
from flask import Flask, request, render_template, session
from flask_socketio import SocketIO, emit
from time import sleep
import threading
from threading import Thread, Event, Lock
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)
streamer = TweePoll_API_single.MyStreamListener()
thread = None
thread_lock = Lock()

def background_thread():
	count = 0
	while True:
		socket.sleep(10)
		output = streamer.main(v + " @realDonaldTrump", v + " @JoeBiden")
		count += 1
		socket.emit('my_response',
			{'data': output, 'count': count},
			namespace='/output')

@app.route('/', methods = ['GET','POST'])
def index():
	return(render_template("index.html", async_mode = socket.async_mode))
	
@socket.on('connect', namespace='/output')
def test_connect():
	#global thread
	print('Client connected')

@socket.on('my_event', namespace='/output')
def test_message(message):
	global v
	v = message['data']
	print(v)

	global thread 
	with thread_lock:
		if thread is None:
			thread = socket.start_background_task(background_thread)
	emit('my_response', {'data': v, 'count': 0})

@socket.on('disconnect', namespace='/output')
def test_disconnect():
	print('Client disconnected')

if __name__ == '__main__':
	socket.run(app, port = 5000, debug = True)