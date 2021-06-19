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
  GPIO.setup([led_g, led_r, led_y], GPIO.OUT, initial=GPIO.LOW)
  
  mylcd=LCD.lcd()
  
  while 1:
      if GPIO.input(Switch1)==GPIO.HIGH:
        GPIO.output(led_r,GPIO.HIGH)
        mylcd.lcd_display_string("red on",1)
        sleep(1)
        GPIO.output(led_r, GPIO.LOW)
        mylcd.lcd_clear()

        GPIO.output(led_g, GPIO.HIGH)
        mylcd.lcd_display_string("geen on",2)
        sleep(1)
        GPIO.output(led_g, GPIO.LOW)
        mylcd.lcd_clear()

      elif GPIO.input(Switch2)==GPIO.HIGH:
        GPIO.output(led_y, GPIO.HIGH)
        mylcd.lcd_display_string("yellow on",1)
        sleep(1)
        GPIO.output(led_y, GPIO.LOW)
        mylcd.lcd_clear()

if __name__=="__main__":
    main()
