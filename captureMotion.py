from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

camera = PiCamera()
pir = MotionSensor(4)

while True:
	pir.wait_for_motion()
	camera.start_preview()
	camera.capture('/home/pi/Desktop/PicturesFromPi/image%s.jpg')
	sleep(3)
	pir.wait_for_no_motion()
	camera.stop_preview()
