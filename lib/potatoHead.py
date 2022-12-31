import os
import pygame
from time import sleep
from pathlib import Path
from random import *

class thePotatoHead:
    def __init__(self,config,mouth, neck, leds, debug):
        self.debug = debug
        self.mouth = mouth
        self.neck = neck
        self.leds = leds
        self.config = config
        if config['enableAudio'] == True:
            pygame.mixer.init()
            pygame.mixer.music.set_volume(1)
            pygame.mixer.Channel(0).set_volume(1)


    ### moving mouth and neck servos together while sound is happening
    def servoTalking(self, scareDelayTime):
        moving = randint(1,5)
        for pos in range (self.config['minJaw'],self.config['maxJaw'],5):
            self.mouth.move(pos)
            if pos == self.config['jawTrigger1'] and (moving == 1 or moving == 4):
                self.neck.move("right")

        for pos in range (self.config['maxJaw'],self.config['minJaw'],-5):
            self.mouth.move(pos)
            if pos == self.config['jawTrigger2'] and (moving == 3 or moving == 5):
                self.neck.move("left")

        sleep(0.15)

        self.resetServos()

        sleep(scareDelayTime)
        return False

    def resetServos(self):
        self.mouth.reset()
        self.neck.reset()

    ## FUnctiont that ties AUdio with movment
    def talkSmack(self,scareDelayTime, songs):
        print("Calling talkSmack") if self.debug == 1 else None
        mouthBusy = False
        songFile = os.path.dirname(os.path.realpath(__file__)) + '/../sound/' + songs[0]
        print("playing: " + songFile) if self.debug == 1 else None

        ## Play intro sound and wait 3 seconds
        if self.config['enableAudio'] == True:
            introSoundFile = os.path.dirname(os.path.realpath(__file__)) + '/../sound/intros/ominouslaugh.ogg'
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(introSoundFile))
            sleep(4)

        if self.config['enableAudio'] == True:
            pygame.mixer.music.load(songFile)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                if mouthBusy == False:
                    mouthBusy = True
                    mouthBusy = self.servoTalking(0.2)

        self.leds.setLed('purple')

        sleep(scareDelayTime)

        if len(songs) == 1:
            return None
        else:
            songs.remove(songs[0])
            return songs

    def cleanUp(self):
        self.mouth.cleanUp()
        self.neck.cleanUp()
