from datetime import datetime
import os
import pytz
import requests
import math
import base64
API_KEY = "fac345183f69a2b3f80148bbdd18db43"
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&country()&mode=json&units={}&av_temp{}&av_wind{}&appid={}')

#CITY = 'Cairo'
av_temp = ""
av_wind = ""
def query_api(city, country, units, av_temp, av_wind,):
    try:
        print(API_URL.format(city, country, units, av_temp, av_wind, API_KEY))
        data = requests.get(API_URL.format(city, units,av_temp , av_wind, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data
