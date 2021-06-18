import RPi.GPIO as GPIO

import time 

LED=12
Switch=16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def main():
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    while True:
        if GPIO.input(Switch)==GPIO.HIGH:
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(1)
            print("Button was pushed!")

        else:
            GPIO.output(LED, GPIO.LOW)
            print("Button was not pushed!")

if __name__=='__main__':
    main()
