import cv2 ## For Camera Functions
import pyzbar.pyzbar as pyzbar ## To recognize QR Codes

class theCamera:
    def __init__(self, config, voiceDB, leds, potatoHead, debug):
        self.camera = cv2.VideoCapture(0)
        self.voiceDB = voiceDB
        self.leds = leds
        self.potatoHead = potatoHead
        self.debug = debug
        self.config = config


    def checkFrame(self,qrMessage):
        decoded_objects = None
        if qrMessage is None:
            _, frame = self.camera.read()
            if self.config['cameraDebug'] == True:
                cv2.imshow("Frame", frame)
            # Decode QR codes in frame
            decoded_objects = pyzbar.decode(frame)
        return decoded_objects


    def analyizeQRCode(self,decoded_objects):
        for obj in decoded_objects:
            if obj.data:
                encoding = 'utf-8'
                qrMessage = obj.data.decode(encoding).lower().strip()

                ## Disable Camera While Processing QR Code
                self.camera.release()

                print(qrMessage) if self.debug == 1 else None

                try:
                    localSoundPath = self.voiceDB.get_voice_data(qrMessage, 'title', 'local_path')
                    print(localSoundPath) if self.debug == 1 else None

                    curatedSoundFile = localSoundPath.split("sound/")[1]
                    soundListTmp = [curatedSoundFile]

                    ## play chime sound :: TODO
                    self.leds.setLed('green')
                    self.potatoHead.talkSmack(5, soundListTmp)
                except:
                    ### FUTURE DEV ::  IF DOES NOT EXIST - CREATE IT - THEN SAY IT
                    self.leds.setLed('purple')

                    print("No sound file found for text: " + qrMessage)
                    print("In the future we could generate this with resemble.ai and play it")

            ##Re:Enable Camera
            qrMessage = None
            self.camera = cv2.VideoCapture(0)
            return None

    def cleanUp(self):
        self.camera.release()
        cv2.destroyAllWindows()
