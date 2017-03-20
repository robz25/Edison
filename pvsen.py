
#!/usr/bin/python
# -*- coding: latin-1 -*-
# -*- coding: utf-8  -*-
#Script de Python para enviar datos de sensores a PVcloud usando Edison
#Autor Robin Gonzalez

import os, time, mraa, math
from ubidots import ApiClient#solo necesario para el call GPIO.cleanup()

#Variables de conversion
#ref: http://wiki.seeed.cc/Grove-Temperature_Sensor_V1.2/
B = 4275.0000
r0 = 100000.0000#resisterncia desconectado

init = 'pvcloud init "https://costaricamakers.com/pvcloud/backend/vse.php" 104 d063c414e35456bb54db9c4589699af6869bd272 "Robinson"'
sen1 = '"Sensor de luz"'
sen2 = '"Temperatura °C:"'
sen3 = '"Potenciometro"'
pvc = 'pvcloud write '

os.system(init)
loop = 0
try:
  while(1):
    a0 = mraa.Aio(0)
    a1 = mraa.Aio(1)
    a2 = mraa.Aio(2)
    
    r = 1023.0000/a1.read()-1
    print "r ", r
    r = r*r0
    print "r ", r
    print " r/r0 ", r/r0
    temperatura = 1/(math.log(r/r0)/B+1/298.15)-273.15
    print "Temperatura: ",temperatura
    time.sleep(1)
        
   #print1 = pvc+" "+sen1+" "+'"'+str(a0.read())+'"'
    #print2 = pvc+" "+sen2+" "+'"'+str(temperatura)+'"'
    #print3 = pvc+" "+sen3+" "+'"'+str(a2.read())+'"'
    #print print1
    #print print2
    #print print3
    #os.system(print1)
    #os.system(print2)
    #os.system(print3)
    loop = loop +1
    print "loop  ", loop
except KeyboardInterrupt:
  GPIO.cleanup()
