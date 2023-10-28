"""
Created by: Liya G
Created on: Oct 2023
This module is a Micro:bit MicroPython program that detects distance with sonar and lights up LEDs.
"""

from microbit import *
import neopixel
from machine import time_pulse_us

# variables
neopixel_strip = neopixel.NeoPixel(pin16, 4)

# choose pins
trig = pin1
echo = pin2

# setup
trig.write_digital(0)
echo.read_digital()

display.clear()
display.show(Image.CONFUSED)

# clean up
neopixel_strip[0] = (0, 0, 0)
neopixel_strip[1] = (0, 0, 0)
neopixel_strip[2] = (0, 0, 0)
neopixel_strip[3] = (0, 0, 0)
print(neopixel_strip[0])
print(neopixel_strip[1])
print(neopixel_strip[2])
print(neopixel_strip[3])
neopixel_strip.show()

# loop
while True:
    display.clear()

    # output
    trig.write_digital(1)
    trig.write_digital(0)

    # Measure the echo pulse in miroseconds then convert to seconds
    micros = time_pulse_us(echo, 1)
    t_echo = micros / 1000000

    # Calculate distance in cm
    dist_cm = (t_echo / 2) * 34300
    display.scroll(str(int(dist_cm)))

    # if distance < 10, light up neopixels red
    if dist_cm < 10:
        neopixel_strip[0] = (255, 0, 0)
        neopixel_strip[1] = (255, 0, 0)
        neopixel_strip[2] = (255, 0, 0)
        neopixel_strip[3] = (255, 0, 0)
        print(neopixel_strip[0])
        print(neopixel_strip[1])
        print(neopixel_strip[2])
        print(neopixel_strip[3])
        neopixel_strip.show()
        sleep(3000)
        display.show(Image.BUTTERFLY)

    # if distance > 10, light up neopixels green
    else:
        neopixel_strip[0] = (0, 255, 0)
        neopixel_strip[1] = (0, 255, 0)
        neopixel_strip[2] = (0, 255, 0)
        neopixel_strip[3] = (0, 255, 0)
        print(neopixel_strip[0])
        print(neopixel_strip[1])
        print(neopixel_strip[2])
        print(neopixel_strip[3])
        neopixel_strip.show()
        sleep(3000)
        display.show(Image.BUTTERFLY)
