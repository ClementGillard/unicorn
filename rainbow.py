#!/usr/bin/python3
# displays a continuous scrolling rainbow using HSV

import unicornhat as u
import colorsys, time

u.brightness(0.5)
i = 0.0
while True:
    i -= 0.002
    for x in range(8):
        r,g,b = colorsys.hsv_to_rgb((i + x / 8.0) % 1,1,1)
        for y in range(8):
            u.set_pixel(x,y,int(r*255),int(g*255),int(b*255))
    u.show()
