#!/usr/bin/python

import time, mraa
from ubidots import ApiClient

#Connect to Ubidots

for i in range(0,5):
    try:
        print "Connecting to Ubidots"
        api = ApiClient(token='BzMNrKvGJRpWYI0lA11ZC8rjLCYbQZ') # Replace with your Ubidots Token here
        break

    except:
        print "No internet connection, retrying..."
        time.sleep(5)

# Assign analog pins

a0 = mraa.Aio(0)
a1 = mraa.Aio(1)

# Read analog pins and send values to Ubidots
try:
    while(1):
        try:
            api.save_collection([{'variable': '58c601877625420177532bae','value':a0.read()}, {'variable': '58c6018f7625420177532c05','value':a1.read()}])
        except:
            print("Couldn't send data.")
            continue
except KeyboardInterrupt:
        GPIO.cleanup()
	break
