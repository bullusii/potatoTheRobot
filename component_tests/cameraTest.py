#!/usr/bin/python
from picamera import PiCamera
import time

camera = PiCamera()
time.sleep(2)
camera.capture("/home/bullusii/work/santaBotV1/tests/testIMG.jpg")
print("Done.")
