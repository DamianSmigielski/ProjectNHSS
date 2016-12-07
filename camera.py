#!/usr/bin/env python

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180
camera.start_preview(alpha=200)
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
