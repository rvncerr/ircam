#!/usr/bin/env python3

from time import sleep
from datetime import datetime, timedelta
from picamera import PiCamera
from fractions import Fraction

camera = PiCamera()
# camera.resolution = (3280, 2464) 
camera.resolution = camera.MAX_RESOLUTION
camera.framerate = Fraction(1, 6)
camera.shutter_speed = 6000000
camera.iso = 800

sleep(30)

camera.exposure_mode = 'off'

for filename in camera.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M-%S}.png'):
	print('Captured %s' % filename)
	sleep(1)
