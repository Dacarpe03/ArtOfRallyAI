import numpy as np
import cv2
import time
import os
# 1280 x 800 game resolution
# SECOND CAMERA IN GAME
# image = grab_screen(region=(550, 300, 1349, 749))
from utils.grab_screen import grab_screen
from utils.getkeys import key_check

file_name = "C:/Users/dcarm/ArtOfRallyAI/data/training_data.npy"
file_name2 = "C:/Users/dcarm/ArtOfRallyAI/data/keys_data.npy"


def save_data(image_data, targets):
    np.save(file_name, image_data)
    np.save(file_name2, targets)


image_data = []
keys_pressed = []

while True:
    keys = key_check()
    if keys == "H":
        break
keys = "N"

while True:
    last_time = time.time()
    image = grab_screen(region=(550, 300, 1349, 749))
    # This line makes edge detection worse in "Art of Rally"
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, threshold1=119, threshold2=250)
    image = cv2.resize(image, (224, 224))
    cv2.imshow("Image", image)
    cv2.waitKey(1)

    image = np.array(image)
    image_data.append(image)

    keys = key_check()
    keys_pressed.append(keys)
    if keys == 'H':
        break
    print(f"{keys} pressed")
    # print('loop took {} seconds'.format(time.time() - last_time))

save_data(image_data, keys_pressed)