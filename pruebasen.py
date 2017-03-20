#!/usr/bin/python
# -*- coding: utf-8  -*-
#Script de Python para enviar datos de sensores a PVcloud usando Edison
#Autor Robin Gonzalez

import os, time, mraa, math
from ubidots import ApiClient#solo necesario para el call GPIO.cleanup()

#Variables de conversion
#ref: http://wiki.seeed.cc/Grove-Temperature_Sensor_V1.2/
B = 4275.00#le pongo decimales para que python no redondee automaticamente
r0 = 100000.00#resisterncia desconectado

sen1 = '"Sensor de luz"'
sen2 = '"Temperatura °C:"'
sen3 = '"Sonido"'



try:
  while(1):
    a0 = mraa.Aio(0)
    a1 = mraa.Aio(1)
    a2 = mraa.Aio(2)
    
    r = 1023.0000/a1.read()-1
    r = r*r0
    temperatura = 1/(math.log(r/r0)/B+1/298.15)-273.15
               
    print1 = sen1+" "+'"'+str(a0.read())+'"'
    print2 = sen2+" "+'"'+str(temperatura)+'"'
    print3 = sen3+" "+'"'+str(a2.read())+'"'
    print print1
    print print2
    print print3
    tiempo = a0.read()
    print "tiempo", tiempo
    tiempo = tiempo/100
    print "tiempo", tiempo
    time.sleep(tiempo)
except KeyboardInterrupt:
  GPIO.cleanup()
