import os
import cv2
from PIL import Image
import numpy as np
# 

# 
data=[]
labels=[]
# 
# ----------------
# LABELS
# Cat 0
# Dog 1
# Monkey 2
# Parrot 3
# Elephant 4
# Bear 5
# ----------------

# Cat 0
cats = os.listdir(os.getcwd() + "/CNN/data/cat")
for x in cats:
    imag=cv2.imread(os.getcwd() + "/CNN/data/cat/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(0)

# Dog 1
dogs = os.listdir(os.getcwd() + "/CNN/data/dog/")
for x in dogs:
    imag=cv2.imread(os.getcwd() + "/CNN/data/dog/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(1)

# Monkey 2
monkeys = os.listdir(os.getcwd() + "/CNN/data/monkey/")
for x in monkeys:
    imag=cv2.imread(os.getcwd() + "/CNN/data/monkey/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(2)

# Parrot 3
parrots = os.listdir(os.getcwd() + "/CNN/data/parrot/")
for x in parrots:
    imag=cv2.imread(os.getcwd() + "/CNN/data/parrot/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(3)

# Elephant 4
elephants = os.listdir(os.getcwd() + "/CNN/data/elephant/")
for x in elephants:
    imag=cv2.imread(os.getcwd() + "/CNN/data/elephant/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(4)

# Bear 5
bears = os.listdir(os.getcwd() + "/CNN/data/bear/")
for x in bears:
    imag=cv2.imread(os.getcwd() + "/CNN/data/bear/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(5)



animals=np.array(data)
labels=np.array(labels)
# 
np.save("animals",animals)
np.save("labels",labels)