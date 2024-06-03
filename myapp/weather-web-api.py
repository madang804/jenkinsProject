from flask import Flask, request
import random


application = Flask(__name__)

@application.route('/')
def home():
    return '''
            <h1>How to make an API call</h1>
            <h3>Add the following parameter after the domain name to get the current weather at a given location</h3>
            <ul>/api/v1.0/weather?location=(location)</ul>
            <h3>Add the following parameter after the domain name to get the current temperature at a given location</h3>
            <ul>/api/v1.0/temperature?location=(location)</ul>
            <h3>Add the following parameter after the domain name to get the current wind condition at a given location</h3>
            <ul>/api/v1.0/wind?location=(location)</ul>
    '''

@application.route('/api/v1.0/weather')
def weather():
    location = request.args.get('location')
    weather_list = ['Clear', 'Clouds', 'Rain', 'Snow']
    weather = random.choice(weather_list)
    return {
            'location': location,
            'weather': weather
    }

@application.route('/api/v1.0/temperature')
def temperature():
    location = request.args.get('location')
    temperature = round(random.uniform(-15, 35), 2)
    return {
            'location': location,
            'temperature': f'{temperature} celcius'
    }

@application.route('/api/v1.0/wind')
def wind():
    location = request.args.get('location')
    wind_speed = round(random.uniform(0, 100), 2)
    wind_direction = round(random.uniform(0, 360), 2)
    return {
            'location': location,
            'wind speed': f'{wind_speed} kts',
            'wind direction': f'{wind_direction} deg'
    }


if __name__ == '__main__':
    application.run(debug=True)
