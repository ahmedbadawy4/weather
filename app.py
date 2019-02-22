from flask import Flask, jsonify, request
from weather import query_api

# remove this line in production
# app.config['DEBUG'] = True


app = Flask(__name__)

version = [{'Version': '0.0.1'}]

# GET /weather with parameter
@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    units = request.args.get('units')
    country = request.args.get('country')
    temp_threshold = request.args.get('temp_threshold')
    wind_threshold = request.args.get('wind_threshold')
    data = query_api(city, country, units, temp_threshold, wind_threshold)
    temp_data = data['main']['temp']
    wind_data = data['wind']['speed']
    cloud_data = data['weather'][0]['description']
    humidity_data = data['main']['humidity']
    temp_state = ""
    wind_state = ""
    if float(temp_data) >= float(temp_threshold):
        temp_state = "high temprature"
    else:
        temp_state = "low temprature "
    if float(wind_data) >= float(wind_threshold):
        wind_state = "high speed wind"
    else:
        wind_state = "low speed wind"
    return jsonify({
        'cloud status': cloud_data, 
        'humidity': humidity_data,
        'wind': wind_data,
        'wind_state': wind_state,
        'temp': temp_data,
        'temp_state': temp_state})

# GET /version
@app.route('/version')
def get_version():
    return jsonify({'weather API': version})
# app.run(port=5000)


app.run(host='0.0.0.0', port=5000)
