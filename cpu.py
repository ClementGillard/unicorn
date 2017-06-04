#!/usr/bin/python3
# an equivalent to htop using the Unicorn HAT

import unicornhat as u
import psutil, os

u.rotation(0)
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

GREEN = (0, 255, 0)
ORANGE = (255, 150, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
colors = [GREEN, GREEN, GREEN, GREEN, ORANGE, ORANGE, RED, RED]

while True:
    usage = psutil.cpu_percent(2, True) # this acts as a sleep
    mem = psutil.virtual_memory()
    nb = psutil.cpu_count()
    load = os.getloadavg()
    with open("/sys/class/thermal/thermal_zone0/temp") as f:
        temp = int(f.read().strip()) / 1000
    u.clear()
    ### CPU usage
    for i in range(0, nb):
        t = int(round(usage[i] / 100 * 8))
        for x in range(0, t):
            c = colors[x]
            u.set_pixel(7 - i, x, *c)
    ### RAM usage
    t1 = int(round((mem.total - mem.available) / mem.total * 8))
    t2 = int(round(mem.used / mem.total * 8))
    for x in range(0, t2):
        c = GREEN if x < t1 else ORANGE
        u.set_pixel(3, x, *c)
    ### Load
    for i in range(3):
        t = min(int(round(load[i] / nb * 4)), 4)
        c = GREEN if load[i] < nb / 2 else ORANGE if load[i] < nb else RED
        for x in range(0, t):
            u.set_pixel(i, 7 - x, *c)
    ### CPU temperature
    h = (240 - 3 * temp) / 360 % 1 # 0 -> blue, 40 -> green, 60 -> yellow, 80 -> red
    u.set_pixel_hsv(0, 0, h, 1, 1)
    u.set_pixel_hsv(0, 1, h, 1, 1)
    u.set_pixel_hsv(1, 0, h, 1, 1)
    u.set_pixel_hsv(1, 1, h, 1, 1)

    u.show()

