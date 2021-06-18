import RPi.GPIO as GPIO

import time 

LED=12
Switch=16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def main():
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    state=0
    
    while True:
        if GPIO.input(Switch)==GPIO.HIGH:   #sw push
            if (state==1):  
                state=0
            elif (state==0):
                state=1
        if (state==1):
            print('LED on')
            GPIO.output(LED, GPIO.HIGH)
        elif (state ==0):
            print('LED off')
            GPIO.output(LED, GPIO.LOW)
        time.sleep(0.5)


if __name__=='__main__':
    main()
