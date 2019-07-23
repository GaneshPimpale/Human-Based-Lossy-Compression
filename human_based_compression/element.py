import PIL.Image, PIL.ImageTk, PIL.ImageFilter, PIL.ImageOps, PIL.ImageEnhance
from tkinter import *

class Element:
    """
    A single image element used to create a composite image.
    Contains both the original PIL image
    and a display version of the image for Tkinter.

    The constructor adds it to the tkinter canvas, but
    does not begin animating the tkinter window.

    For more information on "display" refer to display.py and main.py
    For more information on "parser symbol" refer to file commandParser.py

    :param display: A Display object
    :param file: A path to the image. A string
    :param anchor: The anchor option for displaying on the Tkinter canvas.
        A string. Must be lowercase.
    :param showBorder: A boolean that determines whether the image
        will include a black border around it when displayed on Tkinter.
    """

    def __init__(self, display, file, anchor, showBorder):
        self.canvas = display.canvas
        self.PilImage = PIL.Image.open(file).convert("RGBA") # The original PIL image
        self.showBorder = showBorder
        self.anchorPoint = anchor

        self.position = [0, 0]

        self.displayImage()

    def displayImage(self):
        """
        Overarching method called at the end of each manipulation

        Does not animate the canvas. That's handled in the .mainloop
        function of the Display class.
        """
        if self.showBorder:
            self.tkImage = PIL.ImageTk.PhotoImage(PIL.ImageOps.expand(self.PilImage, border=1, fill=(0, 0, 0)))
        else:
            self.tkImage = PIL.ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(self.position[0], self.position[1],
                                                    image=self.tkImage, anchor=self.anchorPoint)

    def cropRatio(self, ratioX0, ratioY0, ratioX1, ratioY1):
        """
        Cropping method where image is cropped to inside of a bounding box with points (0, 0)
        representing the top left and (1, 1) representing the bottom right

        Parameters should be floats between [0, 1]

        :param ratioX0: Left crop ratio
        :param ratioY0: Top crop ratio
        :param ratioX1: Right crop ratio
        :param ratioY1: Bottom crop ratio
        """

        x, y = [0, 100], [0, 100]

        x[0] = self.tkImage.width() * ratioX0
        y[0] = self.tkImage.height() * ratioY0

        x[1] = self.tkImage.width() * ratioX1
        y[1] = self.tkImage.height() * ratioY1

        self.PilImage = self.PilImage.crop((x[0], y[0], x[1], y[1]))
        self.displayImage()

    #parser WILL save these commands:
    #Symbol: x
    def cropPixel(self, x1, y1, x2, y2):
        """
        Cropping method where image is cropped to inside of a bounding box with points (0, 0)
        representing the top left and (width, height) representing the bottom right

        Parameters should be floats between 0 and the maximum pixel length allowed for the coordinate

        :param x1: Left crop
        :param y1: Top crop
        :param x2: Right crop
        :param y2: Bottom crop
        """
        self.PilImage = self.PilImage.crop((x1, y1, x2, y2))
        self.displayImage()
        print("crop DONE")

    #Symbol: o
    def rotate(self, angleInDegrees):

        self.PilImage = self.PilImage.rotate(angleInDegrees, expand=True, resample=PIL.Image.BICUBIC)
        self.displayImage()

        print("rotate DONE")

    #Symbol: r
    def resize(self, width, height):
        """
        Resize method where image is resized to new width and new height

        :param width: Width in pixels
        :param height: Height in pixels
        """
        self.PilImage = self.PilImage.resize((width, height), PIL.Image.NEAREST)
        self.displayImage()
        print("resize DONE")

    #Symbol: t
    def translate(self, canvasX, canvasY):
        """
        Moves the image ANCHOR POINT to the point defined on the canvas

        :param canvasX: X location to move anchor point
        :param canvasY: Y location to move anchor point
        """
        self.position[0] = canvasX
        self.position[1] = canvasY
        self.displayImage()

    #Symbol: s
    def smudge(self, blurVal):
        """
        Smudge/blur method where image is blurred with Gaussian blur of radius blurVal

        :param blurVal: See PIL documentation for use of GaussianBlur values
        """
        self.PilImage = self.PilImage.filter(PIL.ImageFilter.GaussianBlur(radius = blurVal))
        self.displayImage()

        print("smudge DONE")

    #Symbol: m
    #Always mirrors over the vertical axis (left to right)
    def mirror(self):
        """
        Mirror/flip method where image is reflected over its y-axis (horizontally)
        NOTE: to flip picture over its x-axis (vertically) use self.mirror() then self.rotate(180)
        """

        self.PilImage = self.PilImage.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        self.displayImage()
        print ("mirror DONE")

    #parser will not save this command:
    def onion(self, val):
        """
        NOT SAVED IN PARSER

        Displays an image transparently; this is used as a
        reference when redesigning the picture by hand.

        Typically picture should take up background.

        :param val: Value between 0 and 100, with 0 being fully transparent and 100
        fully saturated
        """
        onion = self.PilImage
        onion.putalpha(val)
        bg = PIL.Image.new("RGBA",(self.PilImage.width, self.PilImage.height) , (255, 255, 255, 250))
        bg.paste(onion, (0, 0), onion)
        self.displayImage()

        print ("onion DONE")

    # Symbol: h
    def brightness(self, val):
        """
        Change the bightness/ contrast of an image element

        :param val: Value is float with 0 being black. 1 is the original bightness
        """
        enhancer = PIL.ImageEnhance.Brightness(self.PilImage)
        self.PilImage = enhancer.enhance(val)
        self.displayImage()

    def getHeight(self):
        return self.PilImage.height

    def getWidth(self):
        return self.PilImage.width




