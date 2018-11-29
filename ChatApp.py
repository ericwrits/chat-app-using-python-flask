from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fgkuhlkdhglfhg8gy4i5'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template("./chatApp.html")


@socketio.on('my event')
def my_event_handler(json):
    print('received something:' + str(json))
    socketio.emit('my response', json)


if __name__ == '__main__':
    socketio.run(app, debug=True)

    
