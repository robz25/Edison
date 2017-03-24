#!/usr/bin/python
# -*- coding: utf-8  -*-
#Script de Python para enviar datos de sensores a PVcloud usando Edison
#Autor Robin Gonzalez

import os, time, mraa, math
import urllib2

from ubidots import ApiClient#solo necesario para el call GPIO.cleanup()
#funciones
def porcentaje(maximo, valor):
  return valor*100/maximo

#Variables de conversion
#ref: http://wiki.seeed.cc/Grove-Temperature_Sensor_V1.2/
B = 4275.00#le pongo decimales para que python no redondee automaticamente
r0 = 100000.00#resisterncia desconectado

init = 'pvcloud init "https://costaricamakers.com/pvcloud/backend/vse.php" 104 d063c414e35456bb54db9c4589699af6869bd272 "Robinson"'
#miap
#links2 = 'https://costaricamakers.com/pvcloud/backend/vse.php/appdata_write_get/104/d063c414e35456bb54db9c4589699af6869bd272/temperatura/'
links3 = 'https://costaricamakers.com/pvcloud/backend/vse.php/appdata_write_get/104/d063c414e35456bb54db9c4589699af6869bd272/sonido/'
#links1 = 'https://costaricamakers.com/pvcloud/backend/vse.php/appdata_write_get/104/d063c414e35456bb54db9c4589699af6869bd272/luz/'
#sing
links1 = 'https://costaricamakers.com/pvcloud/backend/vse.php/appdata_write_get/101/95b8bd7b72f37a29ae9644396326f343f5df0c09/Sensor_luz_porc/'
links2 = 'https://costaricamakers.com/pvcloud/backend/vse.php/appdata_write_get/101/95b8bd7b72f37a29ae9644396326f343f5df0c09/Sensor_temperatura_C/'
links3 = 'https://costaricamakers.com/pvcloud/backend/vse.php/appdata_write_get/101/95b8bd7b72f37a29ae9644396326f343f5df0c09/Sensor_sonido_porc/'
#miap2
#links1 = 'https://costaricamakers.com/pvcloud/backend/vse.php/appdata_write_get/105/1353cf7b0e96acfb3917599df7289611bd92c9b0/Sensor_luz_porc/'
#links2 = 'https://costaricamakers.com/pvcloud/backend/vse.php/appdata_write_get/105/1353cf7b0e96acfb3917599df7289611bd92c9b0/Sensor_temperatura_C/'
#links3 = 'https://costaricamakers.com/pvcloud/backend/vse.php/appdata_write_get/105/1353cf7b0e96acfb3917599df7289611bd92c9b0/Sensor_sonido_porc/'
link = 'https://costaricamakers.com/pvcloud/backend/vse.php/appdata_write_get/104/d063c414e35456bb54db9c4589699af6869bd272/'

sen1 = '"Sensor luz %:"'
sen2 = '"Sensor temperatura °C:"'
sen3 = '"Sensor sonido %:"'
pvc = 'pvcloud write '

#os.system(init)

try:
  while(1):
    a0 = mraa.Aio(0)#luz
    a1 = mraa.Aio(1)#temperatura
    a2 = mraa.Aio(2)#sonido
    
    r = 1023.0000/a1.read()-1
    r = r*r0
    temperatura = 1/(math.log(r/r0)/B+1/298.15)-273.15
    sonido = a2.read()
    luz = a0.read()
    sonido = porcentaje(850, sonido)
    luz = porcentaje(800,luz)
    unido = '{"Sensor_Luz": "'+str(luz)+'", "Sensor_Temperatura":"'+str(temperatura)+'", "Sensor_sonido":"'+str(sonido)+'"}'
    print unido
    print1 = pvc+" "+sen1+" "+'"'+str(luz)+'"'
    print2 = pvc+" "+sen2+" "+'"'+str(temperatura)+'"'
    print3 = pvc+" "+sen3+" "+'"'+str(sonido)+'"'
    http1 = links1 + str(luz)
    http2 = links2 + str(temperatura)
    http3 = links3 + str(sonido)
    unido = link + unido
    print unido
    contents1 = urllib2.urlopen(http1)
    contents2 = urllib2.urlopen(http2)
    contents3 = urllib2.urlopen(http3)
    #contents4 = urllib2.urlopen(unido)
    print print1
    print print2
    print print3
    #os.system(print1)
    #os.system(print2)
    #os.system(print3)
except KeyboardInterrupt:
  GPIO.cleanup()
  

