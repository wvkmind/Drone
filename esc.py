import RPi.GPIO as gpio
import time,sys
pin=16
gpio.setmode(gpio.BOARD)
gpio.setup(pin,gpio.OUT)
p=gpio.PWM(pin,400)
p.start(0)
dc=10
for i in range(40):
  dc += 2
  print('dc:',dc)
  p.ChangeDutyCycle(dc)
  time.sleep(0.3);
p.stop()
gpio.cleanup()
