import os
from datetime import datetime

class scheduleEventHelper:
    def __init__(self, config, debug):
        self.config = config
        self.debug = debug


    def evaluateDate(self, inputDate):
        try:
            date = datetime.strptime(inputDate, '%m-%d-%y %H:%M')
            dateNow = datetime.now()
            if date > dateNow:
                return date
            else:
                print("ERROR: Date has already passed.")
                return None
        except:
            print("Date should be in format MM-DD-YY HH:MM. Try Again...")
            return None


    def evaluateType(self, inputType):
        print(inputType)
        if inputType == 'n' or inputType == 's':
            return inputType
        else:
            print("Input should be 'n' for New or 's' for stored. Try Again...")
            return None


    def evaluateMessage(self, message):
        if "'" in message:
            print("Please remove appostrophies or special characters")
            return None
        else:
            return message.lower()

    def build_stored_menu(self, sayings):
        selector = 1
        for saying in sayings:
            print("[" + str(selector) +  "] - '" + saying[0] + "'")
            selector += 1

    def validateStoredValue(self, storedValue, sayings):
        try:
            index = int(storedValue) - 1
            goodValue = sayings[index]
            return (goodValue[1], goodValue[0])
        except:
            return None

    def printEvents(self, events):
        for event in events:
            hour = "0" + str(event[1]) if event[1] < 10 else str(event[1])
            minute = "0" + str(event[2]) if event[2] < 10 else str(event[2])
            print(event[0] + " " + str(event[1]) + ":" + str(event[2]) + " - '" + event[3] + "'\n") 
