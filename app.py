from flask import Flask, jsonify

app = Flask(__name__)

weather = [
        {
          'city': 'Green Eggs and Ham',
          'temp': 20,
          '% chance of rain': '40%'
        },
]

version = [ { 'Weather API' : ' version: 0.0.1' }  ]

#GET /weather
@app.route('/weather')
def get_weather():
        return jsonify({'weather': weather})

#GET /version
@app.route('/version')
def get_version():
        return jsonify({'version': version})

#app.run(port=5000)
app.run(host='0.0.0.0',port=5000)
