import RPi.GPIO as GPIO

import time

LED_g=12
LED_r=32
LED_y=33
Switch=16

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def main():
    GPIO.setup([LED_g, LED_r, LED_y], GPIO.OUT, initial=GPIO.LOW)
    #GPIO.setup(LED_r, GPIO.OUT, initial=GPIO.LOW)
    #GPIO.setup(LED_y, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    while True:
        if GPIO.input(Switch)==GPIO.HIGH:
            GPIO.output(LED_r, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_g, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_y, GPIO.HIGH)
            time.sleep(0.5)
        else:
            GPIO.output([LED_r, LED_g, LED_y], GPIO.LOW)

if __name__=='__main__':
    main()

