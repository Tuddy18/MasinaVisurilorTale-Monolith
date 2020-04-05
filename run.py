#!flask/bin/python
from app import app, socketio

app.secret_key='secret'

if __name__ == '__main__':
    # app.run(host="0.0.0.0")
    socketio.run(app)