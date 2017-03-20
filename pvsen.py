#!/usr/bin/python

import os, time, mraa
from ubidots import ApiClient#solo necesario para el call GPIO.cleanup()

init = 'pvcloud init "https://costaricamakers.com/pvcloud/backend/vse.php" 104 d063c414e35456bb54db9c4589699af6869bd272 "Robinson"'
sen1 = '"Sensor de luz"'
sen2 = '"Sensor de temperatura"'
sen3 = '"Potenciometro"'
pvc = 'pvcloud write '

os.system(init)

try:
  while(1):
    a0 = mraa.Aio(0)
    a1 = mraa.Aio(1)
    a2 = mraa.Aio(2)
    print1 = pvc+" "+sen1+" "+'"'+str(a0.read())+'"'
    print2 = pvc+" "+sen2+" "+'"'+str(a1.read())+'"'
    print3 = pvc+" "+sen3+" "+'"'+str(a2.read())+'"'
    print print1
    print print2
    print print3
    os.system(print1)
    os.system(print2)
    os.system(print3)
    
except KeyboardInterrupt:
  GPIO.cleanup()
