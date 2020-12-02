#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio / proyecto (segunda parte): "APIs" del Módulo 10 (OpenWeatherMap)

import requests

API_KEY = "xyz"

api_url = "http://api.openweathermap.org/data/2.5/weather?q=Zaragoza,es&units=metric&APPID=" + API_KEY
r = requests.get(api_url)
dic = r.json()
print(dic)
print("Current weather:", dic["weather"][0]["main"])
print("Current temperature:", dic["main"]["temp"], "degrees (Celsius)")
