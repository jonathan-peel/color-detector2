#!/usr/bin/env python3

import numpy as np
import cv2
from time import sleep

cap = cv2.VideoCapture(2)
i = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #Put here your code!
    # You can now treat output as a normal numpy array
    # Do your magic here

    sleep(1)
    i += 1
    print("iteration" + str(i))