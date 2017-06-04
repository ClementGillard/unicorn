#!/usr/bin/python3
# displays a scrolling rainbow using math, and exits

import unicornhat as u
import math, time

u.brightness(0.5)
for n in range(15):
    for x in range(max(0, n - 7), min(8, n + 1)):
        r = int((math.cos((n - x) * math.pi / 4) + 1) * 127)
        g = int((math.cos((n - x - 8.0 / 3.0) * math.pi / 4) + 1) * 127)
        b = int((math.cos((n - x + 8.0 / 3.0) * math.pi / 4) + 1) * 127)
        for y in range(8):
            u.set_pixel(x,y,r,g,b)
    u.show()
    time.sleep(0.1)
    u.clear()
