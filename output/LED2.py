import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED_Green=12
LED_Red=32
LED_Yellow=33

GPIO.setup(LED_Green, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_Red, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_Yellow, GPIO.OUT, initial=GPIO.LOW)

def main():
    while 1:
        GPIO.output(LED_Green, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(LED_Green, GPIO.LOW)
        
        GPIO.output(LED_Yellow, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_Yellow, GPIO.LOW)

        GPIO.output(LED_Red, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(LED_Red, GPIO.LOW)

if __name__=='__main__':
    main()
