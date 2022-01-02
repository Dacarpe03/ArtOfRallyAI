import numpy as np
import cv2
import time
import os
# 1280 x 800 game resolution
# image = grab_screen(region=(550, 300, 1349, 749))
from utils.grab_screen import grab_screen

while True:
    last_time = time.time()
    image = grab_screen(region=(550, 300, 1349, 749))
    # This line makes edge detection worse in "Art of Rally"
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, threshold1=119, threshold2=250)
    image = cv2.resize(image, (224, 224))
    cv2.imshow("Image", image)
    cv2.waitKey(1)
    print('loop took {} seconds'.format(time.time() - last_time))