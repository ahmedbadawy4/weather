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
    data = query_api(city)
    return jsonify({'weather': data})


#GET /version
@app.route('/version')
def get_version():
        return jsonify({'weather API': version})

#app.run(port=5000)
app.run(host='0.0.0.0',port=5000)
