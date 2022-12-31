#!/usr/bin/python
import os
import sys
from datetime import datetime
from time import sleep

current_directory = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, current_directory + '/../lib/')

from voiceDB import *
from loader import *
from scheduleEventHelper import *
from voiceDB import *

## LOADING ALL ENVS
loader = theLoader(current_directory + '/../.potatoGlobalEnv')
config = loader.getConfig()
voiceDB = theVoiceDB(config, config['debugScheduledEvent'])

helper = scheduleEventHelper(config, config['debugScheduledEvent'])

events = voiceDB.get_all_events()
helper.printEvents(events)
