from PIL import Image
from math import degrees

import os
import shutil


#Import/export commands:         #ALL OF THESE NEED TO NOW RUN WITH PILLOW
def create(name, Sdir):
    f = open(name, "x")
    f.close()
    shutil.move(name, Sdir)
    f = open(name) #Might be a problem
    print("Image created")


def source(GetDir, oldName, SaveDir, newName):
    shutil.move(GetDir, SaveDir)
    os.rename(oldName, newName)
    f = open(newName)
    print("Image sourced")


#Object property edit commands:
def crop(imageName, saveName, left, upper, right, lower):
    image = Image.open(imageName)
    box = (left, upper, right, lower)
    tempName = image.crop(box)
    tempName.save(saveName)
    print(imageName + " cropped to " + saveName) 


def resize(imageName, saveName, X, Y):
    image = Image.open(imageName)
    box = (X, Y)
    image.thumbnail(box)
    image.save(saveName)
    print(imageName + " resized as " + saveName)


#Image space edit commands
def move (image, X, Y):                    #Might not come with pillow
    #print(image + " moved")


def rotate(imageName, saveName, angle):
    #image is rotated COUNTERCLOCKWISE
    image = Image.open(imageName)
    tempImage = image.rotate(angle)
    tempImage.save(saveName)
    print(imageName + " rotated to " + saveName)

def flip(imageName, saveName):
    #flips from LEFT to RIGHT, over the vertical axis
    image = Image.open(imageName)
    tempImage = image.transpose(Image.FLIP_LEFT_RIGHT)
    tempImage.save(saveName)
    print(imageName + " flipped to " + saveName)


"""
Script syntax:
-first create overall image and call all images
-all names and directories should be in quotation marks
-All the image objects should be edited before moving onto image space edits
"""

