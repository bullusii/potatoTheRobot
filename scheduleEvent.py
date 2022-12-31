#!/usr/bin/python
import os
import sys
from datetime import datetime
from time import sleep

current_directory = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, current_directory + '/lib/')

from voiceDB import *
from loader import *
from scheduleEventHelper import *
from voiceDB import *

## LOADING ALL ENVS
loader = theLoader(current_directory + '/.potatoGlobalEnv')
config = loader.getConfig()
voiceDB = theVoiceDB(config, config['debugScheduledEvent'])

helper = scheduleEventHelper(config, config['debugScheduledEvent'])

wizard = None
goodDate = None
goodType = None
goodMessage = None
goodStored = None

while wizard == None:
    while goodDate == None:
        inputDate = input("When do you want to schedule a message? [EX. MM-DD-YY HH:MM] (24 hour time)\n> ")
        goodDate = helper.evaluateDate(inputDate)
        ## Timezone / Repeat - maybe in future

    ## GET MESSAGE TYPE
    while goodType == None:
        inputType = input("Do you want to create a [n]ew message or use a [s]tored one? (s or n)\n> ")
        goodType = helper.evaluateType(inputType)

    ##NEW MESSAGE
    if goodType == 'n':
        while goodMessage == None:
            inputMessage = input("What would you like potato to say? (no special characters besides.)\n> ")
            goodMessage = helper.evaluateMessage(inputMessage)

        command = current_directory + "/potatoSay.py \"" + goodMessage + "\""
        output = os.popen(command).read()
        print(output)

        ## now find id for insert to schedule
        local_path = None
        while local_path == None or local_path == 'TBD':
            print("Waiting for file to download...")
            local_path = voiceDB.get_voice_data(goodMessage, 'text','local_path')
            sleep(1.3)


    ##Stored TYPE
    elif goodType == 's':
        while goodMessage == None:
            sayings = voiceDB.get_all_sayings()
            helper.build_stored_menu(sayings)
            goodStoredValue = input("Select a stored saying: (number)\n> ")
            (local_path, goodMessage) = helper.validateStoredValue(goodStoredValue, sayings)


    ## NOW INSERT
    if local_path != None and goodMessage != None and goodDate != None:
        #try:
        voiceDB.insertScheduledEvent(goodDate, local_path, goodMessage)
        #except Exception:
        #    print("ERROR:Failed to INSERT Scheduled Event")
        #    traceback.print_exc()
        wizard = True
