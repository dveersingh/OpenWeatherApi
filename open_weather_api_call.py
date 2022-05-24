def openweather_data():
	import requests #pip3 install requests
	import config
	from app import db
	from models import useraccount,WeatherData, weathers_schema
	
	print("openweather api started")
	
	#delete previous record from table
	try:
		db.session.query(WeatherData).delete()
		db.session.commit()
	except:
		db.session.rollback()
	
	count = 0
	
	#parse data and store in table
	for i in config.cities:		
		url = "{base_url}?q={i}&appid={key}".format(base_url = config.base_url,i=i,
		key = config.key)
		resp = requests.get(url)
		if resp.status_code == 200:
			
			response = resp.json()
			city = response['name']
			country = response['sys']['country']
			for i in response['weather']:
				main = i['main']
				description = i['description']
			visibility = response['visibility']
			temp = response['main']['temp']
			temp_min = response['main']['temp_min']
			feels_like = response['main']['feels_like']
			temp_max = response['main']['temp_max']
			pressure = response['main']['pressure']
			humidity = response['main']['humidity']
			speed = response["wind"]["speed"]
			deg = response["wind"]["deg"]
			data = WeatherData(city, country ,	main,
					description , visibility ,
					temp , temp_min , feels_like , 
					temp_max , pressure ,humidity , 
					speed , deg)
			db.session.add(data)
		count = count+1
		print(count)
	db.session.commit()
	print("openweather data inserted successfully")
