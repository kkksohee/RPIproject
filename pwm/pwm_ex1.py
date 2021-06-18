import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD)

LED = 12
Switch= 16

Duty_ratio = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 
15, 20, 30, 50, 70, 100]

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def main():
  PWM_led = GPIO.PWM(LED, 500)
  PWM_led.start(0)
  
  while 1:
    if GPIO.input(Switch)==GPIO.HIGH:
      for val in Duty_ratio :
        PWM_led.ChangeDutyCycle(val)
        time.sleep(0.5)
    else :
      GPIO.output(LED, GPIO.LOW)

if __name__=="__main__":
  main()
        

