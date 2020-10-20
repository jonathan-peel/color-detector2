#!/usr/bin/env python3

import numpy as np
import os
import cv2
from time import sleep

# set cap to continuously capture images from the camera
cap = cv2.VideoCapture(2)

# Find number of splits input at runtime
n_splits = os.environ["N_SPLITS"]
# Environment variables are returned as strings
try:
    n_splits = int(n_splits) # Rounds to the nearest integer
except ValueError:
    print("Please input an integer as -e N_SPLITS=<integer>, defaulting to N_SPLITS=1")
    n_splits = 1
    
i = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # frame variable is the camera image as a numpy array
    # ret is true if the frame was captured sucessfully and false otherwise

    sleep(1)
    i += 1
    print("Frame " + str(i))