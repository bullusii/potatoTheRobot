#!/usr/bin/python

### EXPECT AT LEAST 1 ARGUMENT AS BODY
## IE ./potatoSay "I like coffee"
## you can also add a title for easy QR IE ./potatoSay "I like you" "Clue 1"
## INPUTS ARE VALIDATED IN validate_inputs from helper

##TODO - on failures write what expected of input or move to CLI Tools
##Some of these .lowers() are probably unneccesary

import os
import sys
from time import sleep

current_directory = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, current_directory + '/lib/')

from resemble import Resemble
from potatoSayHelper import *
from voiceDB import *
from loader import *

## LOADING ALL ENVS
loader = theLoader(current_directory + '/.potatoGlobalEnv')
config = loader.getConfig()
helper = potatoSayHelper(config, config['debugSay'])


## SET BODY and TITLE
(body, title) = helper.validate_inputs(sys.argv)
voiceDB = theVoiceDB(config, config['debugSay'])

try:
    ### CHECK IF THE AUDIO FILE EXISTS IN DB BY CHECKING TITLE
    soundFile = voiceDB.get_local_sound_file(body.lower(), 'title')
    if soundFile != None: ##IF EXISTS JUST SEND THE COMMAND
        print("WARNING Saying EXISTS - just sending command")
        helper.setCommand(body.lower())
        print ("COMMAND SENT - EXITING")
    else:
        raise Exception("No Existing File")
except:
    ### IF IT DOESNT EXIST IN DB: WE - CREATE WITH RESEMBLE.AI & UPDATE voiceDB
    Resemble.api_key(config['token'])

    if config['debugSay'] == 1:
        print("Sending query to resemble.ai...")

    ## MAKE REQUEST TO Resmble.ai
    response_raw = Resemble.v2.clips.create_async(
        config['project_uuid'],
        config['voice_uuid'],
        config['callback_uri'],
        body,
        title,
        config['sample_rate'],
        config['output_format'],
        config['precision'],
        config['include_timestamps'],
        config['is_public'],
        config['is_archived']
    )

    if config['debugSay'] == 1:
        print("RESPONSE:")
        print(response_raw)

    sleep(2)
    clip_id = response_raw['item']['uuid']
    sleep(1)
    voiceDB.insert_sound_file(clip_id, body.lower(),title)
