from datetime import datetime
import os
import pytz
import requests
import math
import base64
API_TOKEN = os.getenv("API_KEY")
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&country()&mode=json&units={}&av_temp{}&av_wind{}&appid={}')
av_temp = ""
av_wind = ""
def query_api(city, country, units, av_temp, av_wind,):
    try:
        print(API_URL.format(city, country, units, av_temp, av_wind, API_TOKEN))
        data = requests.get(API_URL.format(city, units,av_temp , av_wind, API_TOKEN)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data
