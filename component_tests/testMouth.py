#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
from bandpassFilter import BFilter
import pygame

GPIO.setmode(GPIO.BOARD)

## Pin Definitions
servoMouthPin = 36
GPIO.setup(servoMouthPin, GPIO.OUT)
mouth = GPIO.PWM(servoMouthPin,50)
mouth.start(0)


pygame.mixer.init()

def talkSmack(mouth, songFile):
    if debug == 1:
        print("playing: " + songFile)
    pygame.mixer.music.load(songFile)
    pygame.mixer.music.set_volume(.6)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        moveMouth(mouth)

def moveMouth(mouth):
    moving = 0


def play_vocal_track(self, filename=None):
        # Used for both threshold (Scary Terry style) and multi-level (jawduino style)
        def get_avg(levels, channels):
            """Gets and returns the average volume for the frame (chunk).
            for stereo channels, only looks at the right channel (channel 1)"""
            # Apply bandpass filter if STYLE=2
            if c.STYLE == 2:
                levels = self.bp.filter_data(levels)
            levels = np.absolute(levels)
            if channels == 1:
                avg_volume = np.sum(levels)//len(levels)
            elif channels == 2:
                rightLevels = levels[1::2]
                avg_volume = np.sum(rightLevels)//len(rightLevels)
            return(avg_volume)






def sendAngle(servo, angle):
    angle = servo.ChangeDutyCycle(1+(angle/18))
    sleep(0.5)
    servo.ChangeDutyCycle(0)

min_jaw = 30
max_jaw = 270

bp = BPFilter()


##mouth previous range was 30 - 275
sendAngle(mouth, 30)
sleep(1)
sendAngle(mouth, 270)
sleep(1)
sendAngle(mouth, 30)
sleep(1)
sendAngle(mouth, 270)

mouth.stop()
GPIO.cleanup()
print("COMPLETE")
