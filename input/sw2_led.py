import RPi.GPIO as GPIO

import time 

LED=12
Switch1=16
Switch2=18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def main():
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Switch1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Switch2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    while True:
        if GPIO.input(Switch1)==GPIO.HIGH:
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(1)
            print("LED on")

        elif GPIO.input(Switch2)==GPIO.HIGH:
            GPIO.output(LED, GPIO.LOW)
            print("LED off")

if __name__=='__main__':
    main()
