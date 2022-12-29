import RPi.GPIO as GPIO

class theMotionDetection:
    def __init__(self, config, GPIO, debug):
        self.motionSensor = GPIO.setup(config['motionSensorPin'], GPIO.IN)
        self.debug = debug
        self.motionSensorPin = config['motionSensorPin']
        self.config = config


    def getStatus(self):
        if self.config['enableMotionDetection'] == True:
            return GPIO.input(self.motionSensorPin)
        else:
            return 0
