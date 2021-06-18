import RPi.GPIO as GPIO

Switch=10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(Switch)==GPIO.HIGH:
        print("Button was pushed!")

    else:
        print("Button was not pushed!")

