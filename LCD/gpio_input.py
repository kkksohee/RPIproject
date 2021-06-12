import RPi.GPIO as GPIO
import time
import I2C_driver as LCD

Switch=10
LED=12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def main():
    GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

    mylcd=LCD.lcd()
    
    while True:
    
        if GPIO.input(Switch)==GPIO.HIGH:
            print("Button was pushed!")
            GPIO.output(LED, GPIO.HIGH)
            mylcd.lcd_display_string("pushed",1)
            time.sleep(1)
            mylcd.lcd_clear()
            #LED on display
        else:
            print("Button was not pushed!")
            GPIO.output(LED, GPIO.LOW)
            mylcd.lcd_display_string("not pushed",2)
            time.sleep(1)
            mylcd.lcd_clear()
            #LED off display
    time.sleep(1)

if __name__=='__main__':
    main()


