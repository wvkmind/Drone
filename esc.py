import RPi.GPIO as gpio
import time,sys
class Motor(object):
  def __init__(self, pin_number, hz):
    self.hz = hz
    self.pin_number = pin_number
    self.duty_cycle = 0
    
  def start(self):
    gpio.setmode(gpio.BOARD)
    gpio.setup(self.pin_number,gpio.OUT)
    self.port=gpio.PWM(self.pin_number,self.hz)
    self.port.start(0)
    self.duty_cycle = 50
    self.change_duty_cycle()
    time.sleep(4)
    self.duty_cycle = 51
    self.change_duty_cycle()
    time.sleep(5)

  def restart(self):
    self.shutdown()
    self.start()

  def change_duty_cycle(self):
    self.port.ChangeDutyCycle(self.duty_cycle)

  def shutdown(self):
    self.duty_cycle = 0
    self.port.stop()
    gpio.cleanup(self.pin_number)

  def set_speed(self,speed):
    self.duty_cycle = speed / 2.0 + 50
    if(self.duty_cycle < 50):
      self.duty_cycle = 50
    elif(self.duty_cycle > 100):
      self.duty_cycle = 100
    self.change_duty_cycle()

  def test_add_step_1(self):
    for i in range(1,101):
      self.set_speed(i)
      time.sleep(1)

  def test_dec_step_1(self):
    for i in range(100):
      self.set_speed(100-i)
      time.sleep(1)

motor = Motor(16,400)
motor.start()
#motor.test_add_step_1()
#motor.test_dec_step_1()
#while(1):
motor.set_speed(50)

time.sleep(20)

motor.shutdown()

