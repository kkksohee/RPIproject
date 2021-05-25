import RPI.GPIO as GPIO

import time

GPIO.setwarmimgs(False)
GPIO.setmode(GPIE.BOARD)

LED=10

def main():
    GPIO.setup(LED,GPRO.OUT)

    PWM_LED=GPIO.PWM(LED,50)
    PwM_LED.start(0)

    while 1:
        Duty=input()
        duty=int(Duty)
        PWM_LED.ChangeDutyCycle(duty)

if __name__=='__main__':
    main()
