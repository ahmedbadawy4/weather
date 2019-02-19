from datetime import datetime
import os
import pytz
import requests
import math
import base64
API_KEY = base64.b64decode("ZmFjMzQ1MTgzZjY5YTJiM2Y4MDE0OGJiZGQxOGRiNDM=")
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')

#CITY = 'Cairo'

def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data