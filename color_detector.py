#!/usr/bin/env python3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import cv2
from time import sleep
from scipy.stats import mode

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
    print("Frame " + str(i))
    
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
        hsv_splits = []
        for split in splits:
            split_color = int(mode(split, axis=None).mode)
            split_colors.append(split_color)
            hsv_splits.append([split_color, 1, 1])

        print(split_colors)
        print(hsv_splits)
        rgb_splits = matplotlib.colors.hsv_to_rgb(hsv_splits)
        print(rgb_splits)
        plt.imshow(rgb_splits)

    sleep(1)
    i += 1