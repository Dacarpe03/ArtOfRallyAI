import cv2
import numpy as np
import random

data = np.load("../data/training_data.npy", allow_pickle=True)
targets = np.load("../data/keys_data.npy", allow_pickle=True)

print(f'Image Data Shape: {data.shape}')
print(f'targets Shape: {targets.shape}')

# Lets see how many of each type of move we have.
unique_elements, counts = np.unique(targets, return_counts=True)
print(np.asarray((unique_elements, counts)))

# Store both data and targets in a list.
# We may want to shuffle down the road.

holder_list = []
for i, image in enumerate(data):
    holder_list.append([data[i], targets[i]])

random.shuffle(holder_list)

count_left = 0
count_right = 0
count_nothing = 0

for data in holder_list:
    if data[1] == 'A':
        count_left += 1
        cv2.imwrite(f"C:/Users/dcarm/Desktop/artofrallyimages/Left/H7-l{count_left}.png", data[0])
    elif data[1] == 'D':
        count_right += 1
        cv2.imwrite(f"C:/Users/dcarm/Desktop/artofrallyimages/Right/H7-r{count_right}.png", data[0])
    elif data[1] == 'N':
        count_nothing += 1
        cv2.imwrite(f"C:/Users/dcarm/Desktop/artofrallyimages/Nothing/H7-u{count_nothing}.png", data[0])