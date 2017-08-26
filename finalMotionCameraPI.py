import argparse
from picamera import PiCamera, Color
from time import sleep
from gpiozero import MotionSensor
from datetime import datetime
import subprocess

# Create camera object
#camera = PiCamera()

# Create motion sensor object, connected to pin 18
pir = MotionSensor(18)

class UserInput(object):
    """Class to store user input variables received from command line or default"""
    def __init__(self):
        self.args = command_line_parser()
        self.cameraMode = self.args.cameraMode

def command_line_parser():
    """This function will specify different command line arguments and either take its value from command line or use default"""
    cmd_parser = argparse.ArgumentParser()
    cmd_parser.add_argument("-m", "--cameraMode", help="cameraMode 0 - preview camera 1 - save image 2 - recordVideo 3 - detect motion 4 - motion image 5 - record motion 6 - run stream....(Default: 0) ", type=int, default=0)
	
    args = cmd_parser.parse_args()
    return args


# Function to preview the camera
def previewCamera():
    print("Motion Detected!")

    camera.rotation = 180
    camera.resolution = (1900, 1080)
    camera.framerate = 15
    camera.annotate_text = "Camera Preview"
    camera.start_preview()
    sleep(10)
    camer.stop_preview
	
# Function to take pictures
def saveImage():
    camera.rotation = 180
    camera.resolution = (1900, 1080)
    camera.framerate = 15
    camera.annotate_text = "Picture Mode"
    
    for i in range(3):
            sleep(3)
            camera.capture('/home/pi/Desktop/PicturesFromPi/image%s.jpg' % i)
            camera.stop_preview
		
# Function to record video
def recordVid():
    camera.rotation = 180
    camera.resolution = (1900, 1080)
    camera.framerate = 15
    camera.annotate_text = "Video Mode"
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/VideosFromPi/video.h264')
    sleep(10)
    camera.stop_recording()
    camera.stop_preview
	
# Function to detect motion
def detectMotion():
    while True:
	if pir.motion_detected:
	    print("Motion Detected!")
	    sleep(0.1)
	else:
	    print("Nothing Detected!")
	    sleep(0.1)
			
			
# Function to take snapshots while motion detected
def motionImage():
    while True:
	pir.wait_for_motion()
	camera.start_preview()
        sleep(1)
	camera.capture('/home/pi/Desktop/PicturesFromPi/images.jpg')
	pir.wait_for_no_motion()
	camera.stop_preview()

# Function to record video when motion detected
def motionVid():
    while True:
        pir.wait_for_motion()
        camera.start_preview()
        sleep(1)
        camera.start_recording('/home/pi/Desktop/VideosFromPi/motionVi.h264')
        pir.wait_for_no_motion()
        camera.stop_recording()
        camera.stop_preview()
        
# Function to run the live streaming script
def cameraStream():
    subprocess.call("./piCameraStream.sh",shell=True)


def main():
    """Main Function all main functions are called from this method"""
    user_input = UserInput()
    print('user input {0}'.format(user_input.cameraMode))
    if user_input.cameraMode == 0:
        previewCamera()
    if user_input.cameraMode == 1:
        saveImage()
    if user_input.cameraMode == 2:
        recordVid()
    if user_input.cameraMode == 3:
        detectMotion()
    if user_input.cameraMode == 4:
        motionImage()
    if user_input.cameraMode == 5:
        motionVid()
    if user_input.cameraMode == 6:
        cameraStream()
    	
if __name__ == '__main__':
    main()
