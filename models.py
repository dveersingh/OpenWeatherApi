import datetime

from app import db, ma,UserMixin
from sqlalchemy import  DateTime #pip3 install sqlalchemy


#user id and password model
class useraccount(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(100), unique = True)
	password = db.Column(db.String(100))
 
	def __init__(self, username, password):
		self.username = username
		self.password = password
		
		
#weather data model that is stored every 30 mins
class WeatherData(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	city = db.Column(db.String(100))#, 
	country = db.Column(db.String(100))				
	main = db.Column(db.String(100))
	description = db.Column(db.String(100))
	visibility = db.Column(db.String(100))
	temp = db.Column(db.String(100))
	temp_min = db.Column(db.String(100))
	feels_like = db.Column(db.String(100))
	temp_max = db.Column(db.String(100))
	pressure = db.Column(db.String(100))
	humidity = db.Column(db.String(100))
	wind_speed = db.Column(db.String(100))
	wind_deg = db.Column(db.String(100))
	created_date = db.Column(DateTime, default=datetime.datetime.utcnow)
 
	def __init__(self, 
					city, country ,	main,
					description , visibility ,
					temp , temp_min , feels_like , 
					temp_max , pressure ,humidity , 
					wind_speed , wind_deg  
				):
		
		self.city = str(city)
		self.country = str(country)				
		self.main = str(main)
		self.description = str(description)
		self.visibility = str(visibility)
		self.temp = str(temp)
		self.feels_like = str(feels_like)
		self.temp_min = str(temp_min)
		self.temp_max = str(temp_max)
		self.pressure = str(pressure)
		self.humidity = str(humidity)
		self.wind_speed = str(wind_speed)
		self.wind_deg = str(wind_deg)
 
 
#marshmallow serielizer
class WeatherDataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WeatherData
		
weather_schema = WeatherDataSchema()
weathers_schema = WeatherDataSchema(many=True)
 