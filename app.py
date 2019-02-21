from flask import Flask, jsonify, request
from weather import query_api

# remove this line in production
#app.config['DEBUG'] = True


app = Flask(__name__)

version = [ { 'Version': '0.0.1' }  ]

#GET /weather?city=<city>,<county_code>&av_temp=<temp_threshold>&av_wind=<wind_threshold>
@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    units = request.args.get('units')
    country = request.args.get('country')
    av_temp = request.args.get('av_temp')
    av_wind = request.args.get('av_wind')
    data = query_api(city, country, units, av_temp, av_wind)
    temp_data = data['main']['temp']
    wind_data = data['wind']['speed']
    humidity_data = data['main']['humidity']
    
    if wind_data <= av_wind and temp_data >= av_temp:
            return jsonify({'the wind is so cool': wind_data,
                            'the temprature is so cool': temp_data})
    elif wind_data >= av_wind and temp_data <= av_temp:
            return jsonify({'wind speed is not safe to go outside': wind_data, 
                                        'temprature is cold': temp_data})
    elif wind_data <= av_wind and temp_data <= av_temp:
            return jsonify({'the wind is so cool': wind_data,
                                        'temprature is cold': temp_data})
    elif wind_data >= av_wind and temp_data >= av_temp:
            return jsonify({'wind speed is not safe  it sould not go outside': wind_data,
                                        'temprature is cool': temp_data})

    
    
#    return jsonify({'Temprature in Kelvin': temp_data, 'Wind Speed': wind_data, 'Humidity': humidity_data, 'temprature threshold': av_temp, 'Wind Speed threshold': av_wind})


#GET /version
@app.route('/version')
def get_version():
        return jsonify({'weather API': version})

#app.run(port=5000)
app.run(host='0.0.0.0',port=5000)
