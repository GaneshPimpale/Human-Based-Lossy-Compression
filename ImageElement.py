import PIL.Image, PIL.ImageTk, PIL.ImageFilter, PIL.ImageOps
from tkinter import *

class Element: #EACH OF OBJECT OF ELEMENT CONTAINS A PICTURE AND FUNCTIONS THAT SELF MANIPULATE

    # for more information on "canvas" refer to settings.py and main.py
    # for more information on "parser symbol" refer to file commandParser.py

    #/Users/vivaan/Desktop/Image-Editor-master

    # Initializes class Element:
    # @parameter:
    #       canvas: the tkinter canvas, all elements should have the same canvas
    #
    #        file: the path for the picture represented by this element
    #
    #        anchor: a tkinter specific manipulation -- (0,0) on the picture
    #                this can be represented by: tk.center, tk.NW, tk.SE, etc.
    #
    #       displayBorder: a boolean if element should have black border around the image
    #
    def __init__(self, canvas, file, anchor, displayBorder):
        self.canvas = canvas
        self.PilImage = PIL.Image.open(file).convert("RGBA") # The original PIL image

        self.displayBorder = displayBorder
        self.anchorPoint = anchor

        # A the image objects necessary for displaying in Tkinter
        self.tkImage = PIL.ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(0, 0, image=self.tkImage, anchor=self.anchorPoint)

    # overarching method called at the end of each manipulation
    # converts the PIL manipulated image into displayable on tkinter canvas
    def displayImage(self, x=0, y=0):
        if self.displayBorder:
            self.tkImage = PIL.ImageTk.PhotoImage(PIL.ImageOps.expand(self.PilImage, border=1, fill=(0, 0, 0)))
        else:
            self.tkImage = PIL.ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(x, y, image=self.tkImage, anchor=self.anchorPoint)

    # PARSER SYMBOL: k
    #
    # cropping method where image is cropped to inside of a bounding box with points (0, 0)
    # representing the top left and (1, 1) representing the bottom right
    #
    # @parameters should be floats between [0, 1]
    def cropRatio(self, ratioX0, ratioY0, ratioX1, ratioY1):
        x, y = [0, 100], [0, 100]

        x[0] = self.tkImage.width() * ratioX0
        y[0] = self.tkImage.height() * ratioY0

        x[1] = self.tkImage.width() * ratioX1
        y[1] = self.tkImage.height() * ratioY1

        self.PilImage = self.PilImage.crop((x[0], y[0], x[1], y[1]))
        self.displayImage()

    # PARSER SYMBOL: p
    #
    # cropping method where image is cropped to inside of a bounding box with points (0, 0)
    # representing the top left and (width, height) representing the bottom right
    #
    # @parameters should be floats between 0 and the maximum pixel length allowed for the coordinate
    def cropPixel(self, x1, y1, x2, y2):
        self.PilImage = self.PilImage.crop((x1, y1, x2, y2))
        self.displayImage()

    # PARSER SYMBOL: o
    #
    # rotate method that rotates the image counter clockwise by @parameter angleInDegrees degrees
    #
    # NOTE: Because the bounding of tkinter requires a right rectangle, rotation expands the dimensions
    #       of the image to incorporate the farthest left and right regions of the rotated image.
    #       This process will continue indefinitely as rotations continue, growing the image's dimensions
    def rotate(self, angleInDegrees):
        self.PilImage = self.PilImage.rotate(angleInDegrees, expand=True, resample=PIL.Image.BICUBIC)
        self.displayImage()

    # PARSER SYMBOL: r
    #
    # resize method where image is resized to new width and new height
    def resize(self, width, height):
        self.PilImage = self.PilImage.resize((int(width), int(height)), PIL.Image.NEAREST)
        self.displayImage()

    # PARSER SYMBOL: t
    #
    # translate method where image is moved the point (canvasX, canvasY) on the entirety of the canvas
    #
    # NOTE: the origin point (anchor point) is moved to (canvasX, canvasY)
    #       image can be moved outside of the canvas if placed to a pixel greater than the dimensions of canvas
    def translate(self, canvasX, canvasY):
        self.displayImage(canvasX, canvasY)

    # PARSER SYMBOL: s
    #
    # smudge/blur method where image is blurred with guassian blur of radius @parameter blurVal
    def smudge(self, blurVal ):
        self.PilImage = self.PilImage.filter(PIL.ImageFilter.GaussianBlur(radius = blurVal))
        self.displayImage()

    # PARSER SYMBOL: m
    #
    # mirror/flip method where image is reflected over its y-axis (horizontally)
    #
    # NOTE: to flip picture over its x-axis (vertically) use self.mirror() then self.rotate(180)
    def mirror(self):
        self.PilImage = self.PilImage.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        self.displayImage()


        print ("mirror DONE")

    # not saved in parser
    #
    # HELPER METHOD: displays an image transparently; this is used as a
    #                reference when redesigning the picture by hand
    #
    # NOTE: typically picture should take up background
    def onion(self, val):
        onion = self.PilImage
        onion.putalpha(val)
        bg = PIL.Image.new("RGBA",(self.PilImage.width, self.PilImage.height) , (255, 255, 255, 250))
        bg.paste(onion, (0, 0), onion)
        self.tkImage = PIL.ImageTk.PhotoImage(bg)
        self.canvasImage = self.canvas.create_image(0, 0, image=self.tkImage, anchor=self.anchorPoint)

        print ("onion DONE")

    # @returns the height of the image
    def getHeight(self):
        return self.PilImage.height

    # @returns the length of the image
    def getWidth(self):
        return self.PilImage.width
