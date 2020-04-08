from flask import Flask

from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


from app.user import register, login
from app.match import match
from app.profile import profile
from app.profile import profile_callbacks
from app.chat import chat, chat_callbacks
