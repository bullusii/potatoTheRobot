from servos import *

class theMouth:
    def __init__(self, config, GPIO, debug):
        GPIO.setup(config['servoMouthPin'], GPIO.OUT)

        self.mouth = GPIO.PWM(config['servoMouthPin'],50)
        self.config = config
        self.mouth.start(0)
        self.debug = debug

    def reset(self):
        sendAngle(self.mouth, self.config['minJaw'])


    def move(self, angle):
        sendAngle(self.mouth, angle)

    def cleanUp(self):
        self.mouth.ChangeDutyCycle(0)
        self.mouth.stop()
