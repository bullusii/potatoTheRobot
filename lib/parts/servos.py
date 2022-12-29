from time import sleep

## moving servos
def sendAngle(servo, angle):
    angle = servo.ChangeDutyCycle(1+(angle/18))
    sleep(0.01)
    servo.ChangeDutyCycle(0)
