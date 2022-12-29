#!/usr/bin/python

import cv2
import pyzbar.pyzbar as pyzbar

# Open camera
camera = cv2.VideoCapture(0)

while True:
    # Capture frame
    _, frame = camera.read()

    # Decode QR codes in frame
    decoded_objects = pyzbar.decode(frame)

    # Print QR code data
    for obj in decoded_objects:
        print(obj.data)

    # Display frame
    #cv2.imshow("Frame", frame)

    # Break loop if user hits 'q'
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Release camera
camera.release()
cv2.destroyAllWindows()
