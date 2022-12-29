#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

redLedPin = 11 #12 Straight across skip one
greenLedPin = 13 #16
blueLedPin = 15 #18
debug = 1

GPIO.setmode(GPIO.BOARD)

GPIO.setup(redLedPin, GPIO.OUT)
GPIO.output(redLedPin,GPIO.LOW) ##SET HIGH TO TURN OFF
GPIO.setup(greenLedPin, GPIO.OUT)
GPIO.output(greenLedPin,GPIO.LOW) ##SET HIGH TO TURN OFF
GPIO.setup(blueLedPin, GPIO.OUT)
GPIO.output(blueLedPin,GPIO.LOW) ##SET HIGH TO TURN OFF

def setLed(color):
    GPIO.output(redLedPin,GPIO.LOW)
    GPIO.output(greenLedPin,GPIO.LOW)
    GPIO.output(blueLedPin,GPIO.LOW)

    red = green = blue = 0
    print("INPUT:#" + color + "#")
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
    else:
        no_match = 1
        if debug == 1:
            print("No match for color: " + color)

    if no_match == 0:
        print("PIN:" + str(redLedPin) + " :: VALUE:" + str(red))
        print("PIN:" + str(blueLedPin) + " :: VALUE:" + str(blue))
        print("PIN:" + str(greenLedPin) + " :: VALUE:" + str(green))
        if red == 1:
            GPIO.output(redLedPin,GPIO.HIGH)
        if blue == 1:
            GPIO.output(blueLedPin,GPIO.HIGH)
        if green == 1:
            GPIO.output(greenLedPin,GPIO.HIGH)


try:
    while True:
        colorArray = ['red', 'green', 'blue', 'white', 'purple','yellow','pigfeet','white','pigfeet']
        for color in colorArray:
            setLed(color)
            sleep(2)
        #print("ALL HIGH")
        #GPIO.output(redLedPin,GPIO.HIGH)
        #GPIO.output(blueLedPin,GPIO.HIGH)
        #GPIO.output(greenLedPin,GPIO.HIGH)
        #sleep(10)
except KeyboardInterrupt:
    GPIO.cleanup()
