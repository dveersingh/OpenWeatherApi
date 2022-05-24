#main file to run the app  


import os
import requests
from werkzeug.security import check_password_hash, generate_password_hash


from flask import Flask  #pip3 install Flask
from flask_sqlalchemy import SQLAlchemy #pip3 install flask_sqlalchemy


from flask_login import  UserMixin # pip3 install flask_login


from flask_apscheduler import APScheduler #pip3 install flask_apscheduler
from flask_marshmallow import Marshmallow #pip3 install flask_marshmallow

from open_weather_api_call import openweather_data
import config

app = Flask(__name__)
app.secret_key = config.secret_key #secret key


#base dir
basedir = os.path.abspath(os.path.dirname(__file__))

#database location and name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)


scheduler = APScheduler() #scheduler to fetch data from openweather

#from flask_app import db

if __name__ == '__main__':
	from routes import *
	
	scheduler.add_job(id = 'Scheduled Task', func=openweather_data, trigger="interval", seconds=1800)
	scheduler.start()
	app.run(debug=True,use_reloader=False)
	
	







