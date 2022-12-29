from servos import *

class theNeck:
    def __init__(self, config, GPIO, debug):
        self.config = config

        GPIO.setup(config['servoLeftNeckPin'], GPIO.OUT)
        GPIO.setup(config['servoRightNeckPin'], GPIO.OUT)

        self.leftNeck = GPIO.PWM(config['servoLeftNeckPin'],50)
        self.rightNeck = GPIO.PWM(config['servoRightNeckPin'],50)

        self.leftNeck.start(0)
        self.rightNeck.start(0)

        self.debug = debug

        self.reset()

    def reset(self):
        sendAngle(self.leftNeck, self.config['leftNeckMin'])
        sendAngle(self.rightNeck, self.config['rightNeckMin'])


    def move(self, way):
        if way == 'left':
            self.leftNeck.ChangeDutyCycle(self.config['turnLeftLeft'])
            self.rightNeck.ChangeDutyCycle(self.config['turnLeftRight'])
        if way == 'right':
            self.leftNeck.ChangeDutyCycle(self.config['turnRightLeft'])
            self.rightNeck.ChangeDutyCycle(self.config['turnRightRight'])

    def cleanUp(self):
        self.leftNeck.ChangeDutyCycle(0)
        self.rightNeck.ChangeDutyCycle(0)
        self.leftNeck.stop()
        self.rightNeck.stop()
