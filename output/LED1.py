import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED = 12
 
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

def main():
    while 1:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(1)

if __name__=='__main__':
    main()
