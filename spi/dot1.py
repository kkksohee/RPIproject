#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import re
import time
import argparse

import RPi.GPIO as GPIO
import I2C_driver as LCD

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

Switch1=16
Switch2=18
LED_g=12
LED_r=32

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup([Switch1,Switch2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup([LED_g,LED_r], GPIO.OUT, initial=GPIO.LOW)

mylcd=LCD.lcd()
    
def demo(n, block_orientation, rotate, inreverse):
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=n or 1, block_orientation=block_orientation,
                     rotate=rotate or 0, blocks_arranged_in_reverse_order=inreverse)
    print("Created device")
    
    while True:
    
      #Switch1 push    
      if GPIO.input(Switch1)==GPIO.HIGH:
        with canvas(device) as draw:
          #text(draw, (0, 0), "A", fill="white")
          text(draw, (0, 0), 'O', fill="white",font=proportional(CP437_FONT))
          time.sleep(1)
          
        print("Button was pushed!")
        GPIO.output(LED_g, GPIO.HIGH)
        mylcd.lcd_display_string("pushed",1)
        time.sleep(1)
        mylcd.lcd_clear()
        #LED on display
        
        #Switch1 not push
        else:
          print("Button was not pushed!")
          GPIO.output(LED_r, GPIO.LOW)
          mylcd.lcd_display_string("not pushed",2)
          time.sleep(1)
          mylcd.lcd_clear()
          #LED off display
    time.sleep(1)

    '''# start demo
    msg = "0123456789"
    print(msg)
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    time.sleep(1)

    show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0)
    time.sleep(1)

    show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.1)

    #words= ['0','1','2','3','4','5','6','7','8','9']
    words= ['O','X']
    virtual = viewport(device, width=device.width, height=len(words) * 8)
    with canvas(virtual) as draw:
        for i, word in enumerate(words):
            text(draw, (0, i * 8), word, fill="white", font=proportional(CP437_FONT))
            time.sleep(0.1)

    for i in range(virtual.height - device.height):
        virtual.set_position((0, i))
        time.sleep(0.1)

    show_message(device, msg, fill="white")

    time.sleep(0.5)

    print('Canvas')
    for i in words:
        print(i, type(i))
        with canvas(device) as draw:
            #text(draw, (0, 0), "A", fill="white")
            text(draw, (0, 0), i, fill="white")
            
        time.sleep(0.1)
            
        for _ in range(5):
            for intensity in range(16):
                device.contrast(intensity * 16)
                time.sleep(0.5)

    device.contrast(0x80)
    time.sleep(1)

    show_message(device, msg, fill="white", font=SINCLAIR_FONT)

    time.sleep(1)
    show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT))

    time.sleep(1)
    show_message(device, msg, fill="white", font=proportional(TINY_FONT))

    time.sleep(1)
    show_message(device, msg)

    time.sleep(1)
    for x in range(256):
        with canvas(device) as draw:
            text(draw, (0, 0), chr(x), fill="white")
            time.sleep(0.1)'''


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--cascaded', '-n', type=int, default=1, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=0, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3], help='Rotate display 0=0??, 1=90??, 2=180??, 3=270??')
    parser.add_argument('--reverse-order', type=bool, default=False, help='Set to true if blocks are in reverse order')

    args = parser.parse_args()

    try:
        demo(args.cascaded, args.block_orientation, args.rotate, args.reverse_order)
    except KeyboardInterrupt:
        pass
