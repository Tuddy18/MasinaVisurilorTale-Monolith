from flask import Flask


app = Flask(__name__)
from app.home import home
from app.user import register, login
from app.match import match
from app.orders import orders
from app.payment import payment
from app.profile import profile
from app.chat import chat
