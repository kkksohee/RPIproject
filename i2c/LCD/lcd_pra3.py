import RPi.GPIO as GPIO
import I2C_driver as LCD 
from time import*

led_g=12
led_r=32
led_y=33
Switch1=16
Switch2=18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def main():
  GPIO.setup([Switch1, Switch2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup([led_g, led_r,led_y], GPIO.OUT, initial=GPIO.LOW)
  
  Duty_ratio=[1,10,30,50,80,100]
  
  mylcd=LCD.lcd()
  
  PWM_led_g=GPIO.PWM(led_g,500)
  PWM_led_g.start(0)
  PWM_led_y=GPIO.PWM(led_y,500)
  PWM_led_y.start(0)
    
  while 1:
      if GPIO.input(Switch1)==GPIO.HIGH:
        for val in Duty_ratio:
          mylcd.lcd_display_string("green on",1)
          mylcd.lcd_display_string("yellow on",2)
          PWM_led_g.ChangeDutyCycle(val)
          PWM_led_y.ChangeDutyCycle(val)
          sleep(0.5)
          mylcd.lcd_clear()
          
          

          #mylcd.lcd_display_string("yellow on",2)
          #PWM_led_y.ChangeDutyCycle(val)
          #sleep(0.5)
          #PWM_led_y.stop()
          #mylcd.lcd_clear()
          

      
      elif GPIO.input(Switch2)==GPIO.HIGH:
        GPIO.output(led_r, GPIO.HIGH)
        mylcd.lcd_display_string("red on",1)
        sleep(1)
        GPIO.output(led_r, GPIO.LOW)
        mylcd.lcd_clear()

if __name__=="__main__":
    main()
