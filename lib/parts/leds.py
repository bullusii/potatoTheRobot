import RPi.GPIO as GPIO

class theLeds:
    def __init__(self, config, GPIO, debug):
        GPIO.setup(config['redLedPin'], GPIO.OUT)
        GPIO.output(config['redLedPin'],GPIO.LOW) ##SET HIGH TO TURN OFF
        GPIO.setup(config['greenLedPin'], GPIO.OUT)
        GPIO.output(config['greenLedPin'],GPIO.LOW) ##SET HIGH TO TURN OFF
        GPIO.setup(config['blueLedPin'], GPIO.OUT)
        GPIO.output(config['blueLedPin'],GPIO.LOW) ##SET HIGH TO TURN OFF

        pause = config['pause']
        enableMotionDetection = config['enableMotionDetection']

        self.config = config
        self.redLedPin = config['redLedPin']
        self.greenLedPin = config['greenLedPin']
        self.blueLedPin = config['blueLedPin']
        self.debug = debug

    ## Define Used Functions
    def setLed(self,color):
        if self.config['enableLeds'] == False:
            return None
        else:
            GPIO.output(self.redLedPin,GPIO.LOW)
            GPIO.output(self.greenLedPin,GPIO.LOW)
            GPIO.output(self.blueLedPin,GPIO.LOW)

            red = green = blue = 0
            if self.debug == 2:
                print("COLOR INPUT:" + color)
            no_match = 0
            if color == 'red':
                red = 1
            elif color == 'green':
                green = 1
            elif color == 'blue':
                blue = 1
            elif color == 'white':
                red = green = blue = 1
            elif color == 'purple':
                red = blue = 1
            elif color == 'yellow':
                red = green = 1
            elif color == 'off':
                red = green = blue = 0
            else:
                no_match = 1
                if debug == 1:
                    print("No match for color: " + color)

            if no_match == 0:
                if self.debug == 2:
                    print("PIN:" + str(self.redLedPin) + " :: VALUE:" + str(red))
                    print("PIN:" + str(self.blueLedPin) + " :: VALUE:" + str(blue))
                    print("PIN:" + str(self.greenLedPin) + " :: VALUE:" + str(green))
                if red == 1:
                    GPIO.output(self.redLedPin,GPIO.HIGH)
                if blue == 1:
                    GPIO.output(self.blueLedPin,GPIO.HIGH)
                if green == 1:
                    GPIO.output(self.greenLedPin,GPIO.HIGH)

    def set_mode_color(self,pause):
        if self.config['enableLeds'] == False:
            return None
        else:
            ## Motion Detection Mode
            if pause == False and self.config['enableMotionDetection'] == True:
                self.setLed('red')
            else:
                self.setLed('blue')
