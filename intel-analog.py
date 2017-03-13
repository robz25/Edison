#!/usr/bin/python

import time, mraa
from ubidots import ApiClient

#Connect to Ubidots

for i in range(0,5):
    try:
        print "Requesting Ubidots token"
        api = ApiClient('9a50f3a5664b25e9d84dd05a2b20ed95e2e5dfff')# Replace with your Ubidots API Key here
        break
        
    except:
        print "No internet connection, retrying..."
        time.sleep(5)

a0 = mraa.Aio(0)
a1 = mraa.Aio(1)
#reemplazar numeros por el ID de mis variables
while(1):
  api.save_collection([{'variable': 'a0','value':a0.read()}, {'variable': 'a1','value':a1.read()}])

