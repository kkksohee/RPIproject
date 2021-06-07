import RPi.GPIO as GPIO
import time
import I2C_driver as LCD

Switch=10
LED=12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

mclcd= LCD.lcd()
while True:
    
    if GPIO.input(Switch)==GPIO.HIGH:
        print("Button was pushed!")
        GPIO.output(LED, GPIO.HIGH)
        #LED on display
    else:
        print("Button was not pushed!")
        GPIO.output(LED, GPIO.LOW)
        #LED off display
    time.sleep(1)

