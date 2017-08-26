from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

pir = MotionSensor(18)

while True:
    if pir.motion_detected:
        print("Motion Detected!")
		sleep(0.1)
    else:
		print("Nothing Dected!")
		sleep(0.1)		
