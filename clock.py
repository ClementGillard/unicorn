#!/usr/bin/python
# my own attempt at displaying a clock. WIP

import unicornhat as u
import time, math

u.brightness(0.5)

def line(x1, y1, x2, y2, color=(255, 255, 255)):
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    u.set_pixel(x1, y1, *color)
    while x1 != x2 or y1 != y2:
        e = 2 * err
        if e > -dy:
            err -= dy
            x1 += sx
        if e < dx:
            err += dx
            y1 += sy
        u.set_pixel(x1, y1, *color)

def circle(color=(255, 255, 255)):
    line(0.0, 2.0, 0.0, 5.0, color)
    line(2.0, 0.0, 5.0, 0.0, color)
    line(7.0, 2.0, 7.0, 5.0, color)
    line(2.0, 7.0, 5.0, 7.0, color)
    r, g, b = color
    u.set_pixel(1, 1, r, g, b)
    u.set_pixel(1, 6, r, g, b)
    u.set_pixel(6, 6, r, g, b)
    u.set_pixel(6, 1, r, g, b)

def getX(angle, length):
    return int(round(3.5+length*math.cos(angle)))

def getY(angle, length):
    return int(round(3.5+length*math.sin(angle)))

while True:
    currenttime = time.localtime()
    currenthour = currenttime.tm_hour
    currentmin = currenttime.tm_min
    currentsec = currenttime.tm_sec

    ah = (1 + currenthour / 6.0) * math.pi
    am = (1 + currentmin / 30.0) * math.pi
    asec = (1 + currentsec / 30.0) * math.pi

    circle((255, 0, 255))

    line(getX(asec, 0.5), getY(asec, 0.5),
         getX(asec, 3.5), getY(asec, 3.5),
         (255, 0, 0))
    line(getX(am, 0.5), getY(am, 0.5), getX(am, 3.5), getY(am, 3.5), (0, 255, 0))
    line(getX(ah, 0.5), getY(ah, 0.5), getX(ah, 2), getY(ah, 2), (0, 0, 255))

    u.set_pixel(getX(asec, 3.5), getY(asec, 3.5), 255, 0, 0) # ensure at least one pixel shows the seconds

    u.show()
    time.sleep(1)
    u.clear()
