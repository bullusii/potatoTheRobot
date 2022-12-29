#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
#from gpiozero import Servo
#import math
#from gpiozero.pins.pigpio import PiGPIOFactory

GPIO.setmode(GPIO.BOARD)

## Pin Definitions
servoMouthPin = 36
leftNeckPin = 38
rightNeckPin = 40

#mouth = Servo(servoMouthPin)
#factory = PiGPIOFactory()

GPIO.setup(servoMouthPin, GPIO.OUT)
GPIO.setup(leftNeckPin, GPIO.OUT)
GPIO.setup(rightNeckPin, GPIO.OUT)

mouth = GPIO.PWM(servoMouthPin,50)
leftNeck = GPIO.PWM(leftNeckPin,50)
rightNeck = GPIO.PWM(rightNeckPin,50)

#mouth = AngularServo(servoMouthPin, min_angle=0, max_angle=180)
#mouth = Servo(servoMouthPin, pin_factory=factory)
#mouth.max()
#mouth.value = math.sin(math.radians(150))
#pwm.set_servo_pulsewidth( servoMouthPin, 800 );
#mouth.angle(50)

mouth.start(0)
leftNeck.start(0)
rightNeck.start(0)
sleep(2)
duty = 2



def sendAngle(servo, angle):
    angle = servo.ChangeDutyCycle(2+(angle/18))
    sleep(0.5)
    servo.ChangeDutyCycle(0)

sendAngle(mouth, 120)
sendAngle(leftNeck, 60)
sendAngle(rightNeck, 60)
#mouth.ChangeDutyCycle(10)

mouth.stop()
leftNeck.stop()
rightNeck.stop()
GPIO.cleanup()
print("COMPLETE")
