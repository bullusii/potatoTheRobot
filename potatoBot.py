#!/usr/bin/python
from time import sleep
import time
import os
import sys
from pathlib import Path
import RPi.GPIO as GPIO

## LOADING ALL ENVS
current_directory = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, current_directory + '/lib/')
sys.path.insert(1, current_directory + '/lib/parts')

## LOAD LOCAL LIBS
from loader import *
from leds import *
from motion import *
from mouth import *
from camera import *
from neck import *
from voiceDB import *
from potatoHead import *
from commands import *
from schedule import *

loader = theLoader(current_directory + '/.potatoGlobalEnv')
config = loader.getConfig()

## SET FOR BOARD
GPIO.setmode(GPIO.BOARD)

## INITIALIZE PARTS
neck = theNeck(config, GPIO, config['debugBot']) if config['enableNeck'] else None
mouth = theMouth(config, GPIO, config['debugBot']) if config['enableMouth'] else None
leds =  theLeds(config, GPIO, config['debugBot']) if config['enableLeds'] else None
voiceDB = theVoiceDB(config, config['debugBot'])

motionDetection = theMotionDetection(config, GPIO, config['debugBot']) if config['enableMotionDetection'] else None
potatoHead = thePotatoHead(config, mouth, neck, leds, config['debugBot'])
commands = theCommands(config, voiceDB, leds, potatoHead, config['debugBot'])
schedule = theSchedule(config, voiceDB, potatoHead, config['debugBot'])

camera = theCamera(config, voiceDB, leds, potatoHead, config['debugBot'])

## SET PAUSE MODE
pause = config['pause']

## Initialize Local Vars
lastSounds = None
lastMode = None
soundList = None
qrMessage = None
limiter = 0

## Showing that potatoBot.py is running - in blue
leds.setLed('blue')

try:
    while True:
        ### SHOWING MODE - RED is MOTION SENSING
        leds.set_mode_color(pause)
        motionSensor = motionDetection.getStatus()

        ### Get command every 5 loops
        (limiter, command) = commands.throttle(limiter)
        
        ### Check if anything is scheduled
        schedule.checkSchedule()

        ######################## QR CODE STUFF
        if config['enableCamera'] == True:
            # Capture frame
            decoded_objects = camera.checkFrame(qrMessage)
            qrMessage = camera.analyizeQRCode(decoded_objects)
            decoded_objects = None
        ################################ QR CODE

        ## If a command happens will execute here - return current pause value
        pause = commands.execute_command(command, pause)
        ### DEBUG OUTPUT
        print("Sensor Value: " + str(motionSensor)) if config['debugBot'] == 2 else None
        print("Motion Detected!") if config['debugBot'] == 1 and motionSensor == 1 else None

        ## When there's movement and not on pause mode
        if motionSensor == 1 and pause == 0 and  config['enableMotionDetection'] == True:
            leds.setLed('red')

            (soundList, lastMode) = commands.createSoundList(lastMode, lastSounds)
            lastSounds = potatoHead.talkSmack(config['scareDelayTime'], soundList)
            potatoHead.resetServos()

        else:
            ## WAITING
            print(".", end='', flush=True) if config['debugBot'] >= 1 else None

            sleep(config['loopDelayTime'])

            if pause == 1 or motionSensor == 0 or config['enableMotionDetection'] == True:
                leds.setLed('blue')
### quite out
except Exception:
#except KeyboardInterrupt: # If CTRL+C is pressed Exit Cleanly
    potatoHead.cleanUp()
    leds.setLed('off')
    GPIO.cleanup()
    camera.cleanUp()
    traceback.print_exc()
