#!/usr/bin/python

import time, mraa
from ubidots import ApiClient

#Connect to Ubidots

for i in range(0,5):
    try:
        print "Requesting Ubidots token"
        api = ApiClient('abebasfaf4e14d195c0044fcasdfdf9dsfab9d653af3')# Replace with your Ubidots API Key here
        break
        
    except:
        print "No internet connection, retrying..."
        time.sleep(5)

a0 = mraa.Aio(0)
a1 = mraa.Aio(1)
#reemplazar numeros por el ID de mis variables
while(1):
  api.save_collection([{'variable': '558073727625425555af27e4','value':a0.read()}, {'variable': '5580737876254257514be1e6','value':a1.read()}])

