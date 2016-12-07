from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.resolution = (1900, 1080)
camera.framerate = 15
camera.start_preview()
camera.awb_mode = 'sunlight'
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = "Hi, Welcome to our picture mode!"

for i in range(3):
	sleep(5)
	camera.capture('/home/pi/Desktop/PicturesFromPi/image%s.jpg' % i)
camera.stop_preview()
