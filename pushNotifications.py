from time import sleep
from gpiozero import MotionSensor
import httplib, urllib
import RPi.GPIO as GPIO

# Setup GPIO  using Broadcom SOC channel
GPIO.setmode(GPIO.BCM)

# Motion sensor connected to pin 18
PIR = 18

# Set to pull-up (nc pos for pir)
GPIO.setup(PIR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Pushover API setup
PUSH_TOKEN = "a5iwmevgrigrnqcmpg62syc7r9jrhk" 
PUSH_USER = "umfeijhdu5kvzepjgonimf149zrqnj"
PUSH_MSG = "Motion Detected!"

# Function to send push message using Pushover
def sendNotif( msg ):
    c = httplib.HTTPSConnection("api.pushover.net:443")
    c.request("POST", "/1/messages.json",
              urllib.urlencode({
                  "token": PUSH_TOKEN,
                  "user": PUSH_USER,
                  "message": msg,
            }), { "Content-type": "application/x-www-form-urlencoded" })

    c.getresponse()
    return

try:
    while True:
        GPIO.wait_for_edge(PIR, GPIO.RISING)
        print(PUSH_MSG)
        sendNotif(PUSH_MSG)
        sleep(5)

except KeyboardInterrupt:
        GPIO.cleanup()


GPIO.cleanup()

        
