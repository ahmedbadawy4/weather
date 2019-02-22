from datetime import datetime
import os
import pytz
import requests
import math
import base64

API_TOKEN = os.getenv("API_KEY")
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&country()&mode=json&units={}&av_temp{}&av_wind{}&appid={}')
temp_threshold = ""
wind_threshold = ""


def query_api(city, country, av_temp, av_wind, units):
    try:
        print(API_URL.format(city, country, units, wind_threshold, wind_threshold, API_TOKEN))
        data = requests.get(API_URL.format(city, units, temp_threshold, wind_threshold, API_TOKEN)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data
