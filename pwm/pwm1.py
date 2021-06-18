import RPi.GPIO as GPIO #import Raspberry pi GPIO library
import time

LED=12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  #Use physical pin numbering

GPIO.setup(LED, GPIO.OUT,initial=GPIO.LOW)

Duty_ratio=[0,1,2,3,4,5,6,7,8,9,10,12,13,15,20,30,50,70,100]

PWM_LED=GPIO.PWM(LED, 500)
PWM_LED.start(0)

try:
    while True:
        for val in Duty_ratio:
            PWM_LED.ChangeDutyCycle(val)
            time.sleep(0.5)

finally:
    PWM_LED.stop()
    GPIO.cleanup()

