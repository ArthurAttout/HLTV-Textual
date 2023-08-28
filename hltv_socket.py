import socketio

sio = socketio.Client(reconnection_attempts=8)

@sio.event
def connect():
    print('connection established')

@sio.event
def scoreboard(data):
    print(data)


@sio.event
def log(data):
    print('Log')

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:8080')
sio.wait()
