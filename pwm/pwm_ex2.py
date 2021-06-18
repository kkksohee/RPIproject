import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led_g=12
led_r=32
Switch_1=16
Switch_2=18

Duty_ratio=[10,20,30,40,50,80,100]

GPIO.setup([led_g, led_r], GPIO.OUT, initial =GPIO.LOW)
GPIO.setup([Switch_1, Switch_2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def main():
    PWM_led_g=GPIO.PWM(led_g,500)
    PWM_led_g.start(0)
    PWM_led_r=GPIO.PWM(led_r,500)
    PWM_led_r.start(0)

    while 1:
        if GPIO.input(Switch_1)==GPIO.HIGH:
            for val in Duty_ratio:
                PWM_led_r.ChangeDutyCycle(val)
        elif GPIO.input(Switch_2)==GPIO.HIGH:
            for val in Duty_ratio:
                PWM_led_g.ChangeDutyCycle(val)

if __name__=="__main__":
    main()

