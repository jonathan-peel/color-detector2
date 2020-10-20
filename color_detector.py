#!/usr/bin/env python3

import numpy as np
import matplotlib as plt
import os
import cv2
from time import sleep

# set cap to continuously capture images from the camera
cap = cv2.VideoCapture(2)

# Find number of splits input at runtime
n_splits = os.environ["N_SPLITS"]
try:
    n_splits = int(n_splits) # Rounds to the nearest integer
except ValueError:
    print("Please input an integer as -e N_SPLITS=<integer>, defaulting to N_SPLITS=1")
    n_splits = 1
    
i = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # ret variable is true if the frame was captured sucessfully and false otherwise
    if (not ret):
        print("Frame not captured. Make sure nothing else is using the camera!")
    else:
        # frame variable is the camera image in RGB as a numpy array
        frame_hsv = plt.colors.rgb_to_hsv(frame)
        frame_hue = frame_hsv[:, :, 2]

        # Divide the frame into n_splits sections
        # frame_height = frame_hue.shape[0]
        # split_height = round(frame_height / n_splits)

        # splits = np.array_split(frame_hue, 7)

        for split in splits:
            


        print(frame_hue)


    sleep(1)
    i += 1
    print("Frame " + str(i))