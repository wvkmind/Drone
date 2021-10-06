import RPi.GPIO as gpio
import time,sys
time.sleep(10)
class Motor(object):
  def __init__(self, pin_number, hz):
    self.hz = hz
    self.pin_number = pin_number
    self.duty_cycle = 0
    
  def start(self):
    gpio.setmode(gpio.BOARD)
    gpio.setup(self.pin_number,gpio.OUT)
    
    self.port=gpio.PWM(self.pin_number,self.hz)
    #self.port.stop()
    self.port.start(0)
    time.sleep(2.5)
    #gpio.output(self.pin_number,gpio.LOW)
    #time.sleep(3)
    #gpio.output(self.pin_number,gpio.HIGH)
    #time.sleep(3)
    print("1")
    self.port.ChangeDutyCycle(50)
    print("2")
    #print("96-")
    time.sleep(2.5)
    #print("3")
    #self.port.ChangeDutyCycle(100)
    #print("4")
    #time.sleep(6)
    #time.sleep(3)
    #print("set hi")
    #self.change_duty_cycle(50)
    #time.sleep(6);
    #print("set low")
    #self.change_duty_cycle(50)
    #time.sleep(4);
    #self.change_duty_cycle(40)
    #time.sleep(6)
  

  def restart(self):
    self.shutdown()
    self.start()

  def change_duty_cycle(self,duty_cycle):
    self.duty_cycle = duty_cycle
    self.port.ChangeDutyCycle(self.duty_cycle)

  def shutdown(self):
    self.duty_cycle = 0
    self.port.stop()
    gpio.cleanup(self.pin_number)

  def test(self):
    for dc in range(50, 76, 1):
      self.port.ChangeDutyCycle(dc)
      print("dc:"+str(dc))
      time.sleep(0.3);
    #for dc in range(80, 40, -1):
      #motor.change_duty_cycle(dc)
      #print("dc:"+str(dc))
      #time.sleep(0.3);


motor = Motor(16,400)
motor.start()
#motor.test_add_step_1()
#motor.test_dec_step_1()
#while(1):
#motor.set_speed(70)
motor.test()
#motor.set_speed(100)
time.sleep(10)

motor.shutdown()

