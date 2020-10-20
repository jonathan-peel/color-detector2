#!/usr/bin/env python3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import cv2
from time import sleep
from scipy.stats import mode

""" This program calculates the most present color of a duckiebot frame,
    recorded once a second. The most present color is represented by 
    the mode of the pixel hues, rounded to the nearest 10. This better
    represents human vision than averaging. Each frame is divided into 
    N_SPLITS sections, which is an environment variable set at runtime.
"""

# set cap to continuously capture images from the camera
cap = cv2.VideoCapture(2)

# Find number of splits input at runtime
n_splits = os.environ["N_SPLITS"]
try:
    n_splits = int(n_splits) # Rounds to the nearest integer
except ValueError:
    print("Please input an integer representing number of splits as -e \
N_SPLITS=<integer>, defaulting to N_SPLITS=1")
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
        frame_hsv = matplotlib.colors.rgb_to_hsv(frame)
        frame_hue = frame_hsv[:, :, 2]

        # Quantise each pixel's hue to the closest 10 degrees
        frame_hue = np.round(frame_hue, -1)

        # Divide the frame into n_splits sections
        splits = np.array_split(frame_hue, n_splits)

        # For each split, find the most present (modal) color
        split_colors = []
        for split in splits:
            split_color = int(mode(split, axis=None).mode)
            split_colors.append(split_color)

        # Print the most present colors, listed by split
        print("The most present hues for each splits 1 to {} of frame {} are \
listed below in degrees.".format(n_splits, i))
        print(split_colors)

    sleep(1)
    i += 1