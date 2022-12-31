from datetime import datetime


class theSchedule:
    def __init__(self,config,voiceDB, potatoHead,debug):
        self.config = config
        self.debug = debug
        self.potatoHead = potatoHead
        self.voiceDB = voiceDB


    def checkSchedule(self):
        currentDate = datetime.now()
        print("CHECKING FOR EVENT @: " + str(currentDate.hour) + ":" + str(currentDate.minute)) if self.debug == 2 else None

        try:
            (id, eventSoundFilePath) = self.voiceDB.getScheduledEvent()
            curatedSoundFilePath = eventSoundFilePath.split("sound/")[1]
            print("EVENT FOUND: Playing: " + curatedSoundFilePath) if self.debug == 1 else None
            self.voiceDB.updateScheduledEvent(id)
            self.potatoHead.talkSmack(5, [curatedSoundFilePath])
        except:
            print("No Events") if self.debug == 2 else None
            return None
