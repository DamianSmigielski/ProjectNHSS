from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep


camera = PiCamera()
pir = MotionSensor(4)
while True:
    if pir.motion_detected:
        print("Motion Detected!")
	camera.start_preview()
	sleep(2)
    else:
	print("Looking For Motion!")
	camera.stop_preview()
	sleep(2)
