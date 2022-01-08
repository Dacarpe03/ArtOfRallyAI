import random
import time

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

from utils.getkeys import key_check
import pydirectinput
import keyboard
import cv2
from utils.grab_screen import grab_screen
from fastai.vision.all import *
def label_func(x): return x.parent.name
learn_inf = load_learner("C:/Users/dcarm/ArtOfRallyAI/rallyai20000.pkl")
print("Loaded learner")

sleepy = 0.1
keyboard.wait('H')

time.sleep(sleepy)

# Hold down W no matter what!
keyboard.press('w')

# Randomly pick action then sleep.
# 0 do nothing release everything ( except W )
# 1 hold left
# 2 hold right
# 3 Press Jump

while True:
    image = grab_screen(region=(550, 300, 1349, 749))
    image = cv2.Canny(image, threshold1=119, threshold2=250)
    image = cv2.resize(image, (224, 224))
    # cv2.imshow("Fall", image)
    # cv2.waitKey(1)
    start_time = time.time()
    result = learn_inf.predict(image)
    action = result[0]
    # print(result[2][0].item(), result[2][1].item(), result[2][2].item(), result[2][3].item())

    # action = random.randint(0,3)
    if action == "Nothing":
        print("Nothing")
        # print("Doing nothing....")
        keyboard.release("a")
        keyboard.release("d")
        time.sleep(sleepy)

    elif action == "Left":
        print(f"LEFT! - {result[1]}")
        keyboard.release("d")
        keyboard.press("a")

    elif action == "Right":
        print(f"Right! - {result[1]}")
        keyboard.release("a")
        keyboard.press("d")


    # End simulation by hitting h
    keys = key_check()
    if keys == "M":
        break
