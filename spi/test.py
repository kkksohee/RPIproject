#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import re
import time
import argparse

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT


def demo(n, block_orientation, rotate, inreverse):
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=n or 1, block_orientation=block_orientation,
                     rotate=rotate or 0, blocks_arranged_in_reverse_order=inreverse)
    print("Created device")

    # start demo

    #words= ['0','1','2','3','4','5','6','7','8','9']
    words= ['O','X']
    virtual = viewport(device, width=device.width, height=len(words) * 8)

    #with canvas(virtual) as draw:
    #    for i, word in enumerate(words):
    #        text(draw, (0, i * 8), word, fill="white", font=proportional(CP437_FONT))
    #        time.sleep(0.1)


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

#    device.contrast(0x80)


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
