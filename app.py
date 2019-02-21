from flask import Flask, jsonify, request
from weather import query_api

# remove this line in production
#app.config['DEBUG'] = True


app = Flask(__name__)

version = [ { 'Version': '0.0.1' }  ]

#GET /weather?city=cairo
@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    units = request.args.get('units')
    country = request.args.get('country')
    av_temp = request.args.get('av_temp')
    av_wind = request.args.get('av_wind')
    data = query_api(city, country, units, av_temp, av_wind)
#    for temp in data["weather"][0]["main"]:
#                if temp >= av_temp:
#                         return jsonify({'temprature': temp})                      
    return jsonify({'weather': data,
                        'av_temp': av_temp,
                        'av_wind': av_wind})


#GET /version
@app.route('/version')
def get_version():
        return jsonify({'weather API': version})

#app.run(port=5000)
app.run(host='0.0.0.0',port=5000)
