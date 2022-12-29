#!/usr/bin/python
import RPi.GPIO as GPIO
import time

pir_sensor = 32

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_sensor, GPIO.IN)

current_state = 0

try:
    while True:
        time.sleep(0.1)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            print("GPIO pin %s is %s" % (pir_sensor, current_state))
            time.sleep(5)
except KeyboardInterrupt: ## if control + c is hit
    pass
finally:
    GPIO.cleanup()
