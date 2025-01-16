from flask import Flask
from flask_session_captcha import FlaskSessionCaptcha
from pymongo import MongoClient

app = Flask(__name__)
mongoClient = MongoClient('localhost', 27017)
app.config["SECRET_KEY"] = "123456"
app.config['CAPTCHA_ENABLE'] = True
app.config['CAPTCHA_LENGTH'] = 5
app.config['CAPTCHA_WIDTH'] = 160
app.config['CAPTCHA_HEIGHT'] = 60
app.config['SESSION_MONGODB'] = mongoClient
app.config['SESSION_TYPE'] = 'mongodb'
captcha = FlaskSessionCaptcha(app)

from app import routes
