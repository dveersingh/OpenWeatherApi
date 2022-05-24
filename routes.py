
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask,  request,jsonify

from flask_login import LoginManager, UserMixin
from flask_login import login_user, logout_user, current_user, login_required
 
from flask_apscheduler import APScheduler #pip3 install flask_apscheduler

from app import app
from models import useraccount,WeatherData, weathers_schema




#login code
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'Login'
 

@login_manager.user_loader
def load_user(user_id):
	return useraccount.query.get(int(user_id))
 
 
#creating our routes
@app.route('/')
@login_required
def index():
 
	name = current_user.username
 
	return name
 
 
 
#login route
@app.route('/login' , methods = ['GET', 'POST'])
def Login():
	
 
	if request.method == 'POST':
		_json = request.json
		_username = _json['username']
		_password = _json['password']
		
		user = useraccount.query.filter_by(username=_username).first()

		if user:
			if check_password_hash(user.password, _password):
				login_user(user)

				return jsonify({"status": 200,"login":"successfull"})


			return jsonify({"status":"Invalid Credentials"})
		return jsonify({"status":"No user found"})
	return jsonify({"status":"Login again"})
 
	

#main route for weather data
@app.route('/weather_data',defaults={"page": 1})
@app.route('/weather_data/<int:page>', methods=['GET'])
@login_required
def weather_data(page):
	page = page
	per_page = 5
	data = WeatherData.query.paginate(page,per_page,error_out=False).items
	print(data)
	return jsonify({"status":200},weathers_schema.dump(data))


#logout route
@app.route('/logout')
@login_required
def logout():
	logout_user()
	return jsonify({"status":200, "log out": "succesfull"})
 
