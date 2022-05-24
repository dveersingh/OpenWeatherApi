# OpenWeatherApi

### I have used flask restful api to implement the given task.

           Username = dharmveer11

           Password = Password@123
           
           
### Run below command to install the requirments

           pip install -r requirements.txt

## Requirments 
        Flask==2.0.2
        Flask_APScheduler==1.12.3
        Flask_Login==0.6.1
        flask_marshmallow==0.14.0
        Flask_SQLAlchemy==2.5.1
        requests==2.27.1
        SQLAlchemy==1.4.31
        Werkzeug==2.0.2


## To run the app run the below command on terminal

    flask run
   
### OR
    python app.py
 

## Login api: 
    url : localhost:5000/login
    
#### json data to send 
        {
        "username":"dharmveer11",
        "password":"Password@123"
        }


## LogOut Api :

    Url : localhost:5000/logout

 

## Weather Data Api of 30 cities:

    Total page: 6
    Per page item = 5
    Default page is 1.
    
    URL :  localhost:5000/weather_data/{pageNumber}

### Response: 

     {
            "status": 200
        },
        [
            {
                "city": "Berlin",
                "country": "DE",
                "created_date": "2022-05-23T23:56:27.543976",
                "description": "clear sky",
                "feels_like": "290.69",
                "humidity": "51",
                "id": 21,
                "main": "Clear",
                "pressure": "995",
                "temp": "291.47",
                "temp_max": "291.47",
                "temp_min": "290.99",
                "visibility": "10000",
                "wind_deg": "130",
                "wind_speed": "6.17"
            },
            {
                "city": "Las Vegas",
                "country": "US",
                "created_date": "2022-05-23T23:56:27.543976",
                "description": "clear sky",
                "feels_like": "302.82",
                "humidity": "9",
                "id": 22,
                "main": "Clear",
                "pressure": "1008",
                "temp": "305.02",
                "temp_max": "307.38",
                "temp_min": "303.57",
                "visibility": "10000",
                "wind_deg": "90",
                "wind_speed": "5.14"
            },
            {
                "city": "Washington",
                "country": "US",
                "created_date": "2022-05-23T23:56:27.543976",
                "description": "broken clouds",
                "feels_like": "290.33",
                "humidity": "35",
                "id": 23,
                "main": "Clouds",
                "pressure": "1014",
                "temp": "291.52",
                "temp_max": "293.37",
                "temp_min": "287.92",
                "visibility": "10000",
                "wind_deg": "320",
                "wind_speed": "6.14"
            },
            {
                "city": "Istanbul",
                "country": "TR",
                "created_date": "2022-05-23T23:56:27.544975",
                "description": "clear sky",
                "feels_like": "289.18",
                "humidity": "72",
                "id": 24,
                "main": "Clear",
                "pressure": "1012",
                "temp": "289.6",
                "temp_max": "289.83",
                "temp_min": "288.19",
                "visibility": "10000",
                "wind_deg": "60",
                "wind_speed": "2.57"
            },
            {
                "city": "Vienna",
                "country": "AT",
                "created_date": "2022-05-23T23:56:27.544975",
                "description": "few clouds",
                "feels_like": "289.47",
                "humidity": "77",
                "id": 25,
                "main": "Clouds",
                "pressure": "1008",
                "temp": "289.74",
                "temp_max": "290.86",
                "temp_min": "288.67",
                "visibility": "10000",
                "wind_deg": "250",
                "wind_speed": "3.09"
            }
        ]
    ]

