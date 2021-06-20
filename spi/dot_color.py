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


 serial = spi(port=0, device=0, gpio=noop())
 device = max7219(serial, cascaded=n or 1, block_orientation=block_orientation,
                     rotate=rotate or 0, blocks_arranged_in_reverse_order=inreverse)

def rotate(l):
    return l[-1:] + l[:-1]


def main():
    colors = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
        "white"
    ]

    for color in colors:
        with canvas(device) as draw:
            draw.line(device.bounding_box, fill=color)
        time.sleep(2)

    device.contrast(0x30)
    for _ in range(80):
        with canvas(device) as draw:
            for x, color in enumerate(colors):
                draw.point((x, 0), fill=color)

        colors = rotate(colors)
        time.sleep(0.2)

    time.sleep(4)

    device.contrast(0x80)
    time.sleep(1)
    device.contrast(0x10)
    time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
