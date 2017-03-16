import os, time, mraa

string init = 'pvcloud init "https://costaricamakers.com/pvcloud/backend/vse.php" 104 d063c414e35456bb54db9c4589699af6869bd272 "Robinson"'
sen1 = '"Sensor de luz"'
sen2 = '"Sensor de temperatura"'
pvc = 'pvcloud write '

os.system(init)

try:
  while(TRUE):
    a0 = mraa.Aio(0)
    a1 = mraa.Aio(1)
    os.system(pvc+" "+sen1+" "+"+a0+")
    os.system(pvc+" "+sen2+" "+"+a1+")
    
except KeyboardInterrupt:
  GPIO.cleanup()
