import os
from time import sleep
from pathlib import Path
from random import *

class theCommands:
    def __init__(self, config, voiceDB, leds, potatoHead, debug):
        self.config = config
        self.leds = leds
        self.potatoHead = potatoHead
        self.voiceDB = voiceDB
        self.debug = debug


    def execute_command(self, command, pause):
        if command ==  'sing':
            self.leds.setLed('yellow')
            soundListTmp = self.createSounds('sing')
            self.resetCommand()
            self.potatoHead.talkSmack(5, soundListTmp)
        elif command ==  'on':
            self.leds.setLed('red')
            self.resetCommand()
            pause = 0
        elif command == 'off':
            self.leds.setLed('blue')
            self.resetCommand()
            pause = 1
        elif command == 'joke':
            self.leds.setLed('yellow')
            soundListTmp = self.createSounds('joke')
            self.resetCommand()
            self.potatoHead.talkSmack(5, soundListTmp)
        elif "downloadClip" in command:
            self.leds.setLed('white')
            (soundListTmp, playOnDownload) = self.processDownload(command)
            self.resetCommand()
            print("PlayOnDownload: " + str(playOnDownload)) if self.debug == 1 else None
            if playOnDownload == 1 or playOnDownload == '1':
                self.potatoHead.talkSmack(.5, soundListTmp)
        elif "SayThis" in command:
            try:
                message = command.split("#SayThis#")[1]
                soundFile = self.voiceDB.get_voice_data(message, 'text','local_path')
                curatedSoundFile = soundFile.split("sound/")[1]
                soundListTmp = [curatedSoundFile]
                self.leds.setLed('green')
                self.resetCommand()
                self.potatoHead.talkSmack(5, soundListTmp)
            except:
                print("ERROR: Say command not in DB: " + command)
                self.leds.setLed('red')
        else:
            print("No command matched") if self.debug == 2 else None

        return pause

    def processDownload(self,command):
        clip_id = command.split("#")[1]
        clip_name = command.split("#")[2].split('/')[2]
        clip_local_path = os.path.dirname(os.path.realpath(__file__)) + '/../sound/clips/' + clip_name
        ## Copy file to local
        if self.debug == 1:
            print("COMMAND TO DL A CLIP INITIATED")
        commandEx = "aws s3 cp s3://skelly-api/clips/" + clip_name + " " + clip_local_path + " && chmod +x " + clip_local_path
        os.popen(commandEx)

        ## UPDATE DATABASE with paths for caching
        s3_path = 's3://skelly-api/clips/' + clip_name
        playOnDownload = self.voiceDB.update_sound(s3_path, clip_local_path, clip_id)
        soundListTmp = ['clips/' + clip_name]
        playOnDownload = self.voiceDB.get_playOnDownload(clip_id)
        ### Delay to allow file placement
        sleep(5)
        return soundListTmp, playOnDownload

    def getMode(self):
        command = "curl -s " + self.config['get_mode_url'] + " | awk -F '\"' '{ print $4 }'"
        resp = os.popen(command).read()
        mode = resp.replace('\n', '')
        return mode

    def getCommand(self):
        command = "curl -s " + self.config['get_command_url'] + " | awk -F '\"' '{ print $4 }'"
        resp = os.popen(command).read()
        mode = resp.replace('\n', '')
        return mode

    def resetCommand(self):
        command = "curl -s " + self.config['reset_command_url']
        os.popen(command).read()

    def createSounds(self, mode):
        dir_path = os.path.dirname(os.path.realpath(__file__)) + '/../sound/' + mode
        command = "ls " + dir_path + " | wc -l | xargs"
        numberOfSongs = os.popen(command).read()
        songs = []
        for pos in range (1,(int(numberOfSongs) + 1),1):
            songs.append(mode + '/' + str(pos) + '.mp3')
        shuffle(songs)
        return songs

    def throttle(self, limiter):
        if limiter == 5:
            command = self.getCommand()
            limiter = 0
        else:
            command = "NONE"

        limiter += 1

        return [limiter, command]


    def createSoundList(self, lastMode, lastSounds):
        mode = self.getMode()
        if mode == lastMode:
            lastMode = mode
            try:
                if len(lastSounds) == 0 or lastSounds == None:
                    soundList = self.createSounds(mode)
                else:
                    soundList = lastSounds
            except:
                soundList = self.createSounds(mode)
        else:
            soundList = self.createSounds(mode)
            lastMode = mode

        print(soundList) if debug >= 1 else None

        return [soundList, lastMode]
