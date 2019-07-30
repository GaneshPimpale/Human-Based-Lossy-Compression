import PIL.Image, PIL.ImageTk, PIL.ImageFilter, PIL.ImageOps, PIL.ImageEnhance
from tkinter import *
import os

class Element:
    """
    Each instance of this class constitutes a single image element
    used in creating the composite image on the display.
   
    The constructor adds it to the display, but
    does not begin animating the display window.
    
    If no parameters are entered, it creates an empty version of the object
    to be used for the .getCopy() member function.
    
    For more information on "display" refer to display.py and main.py
    For more information on "parser symbol" refer to file parser.py
    
    :param display: A Display object
    :param file: The filename of the image (ex: 'car.png'). Images must 
        be stored in a folder named 'elements' that is located in directory
        from which 'main.py' is executed
    :param anchor: The anchor option for displaying on the Tkinter canvas.
        A string. Must be lowercase.
    :param showBorder: A boolean that determines whether the image
        will include a black border around it when displayed on Tkinter.
    :param element: an object of Element that self will create a shallow copy
    of, if element is inserted, all other params ignored
    """

    def __init__(self, display=None, file=None, anchor=None, showBorder=False, element=None):

        if isinstance(element, Element):
            self.PilImage = element.PilImage
            self.canvas = element.canvas
            self.showBorder = element.showBorder
            self.anchorPoint = element.anchorPoint
            self.position = element.position
            self.displayImage()
            pass

        if display is None:
            pass
        else:
            fullPath = os.path.join(os.getcwd(), "elements", file)
            self.PilImage = PIL.Image.open(fullPath).convert("RGBA")  # The original PIL image
            self.canvas = display.canvas
            self.showBorder = showBorder
            self.anchorPoint = anchor
            self.position = [0, 0]

            self.displayImage()

    def displayImage(self):
        """
        Helper method that places the element on the canvas.
        Overarching method called at the end of each manipulation.
        """
        if self.showBorder:
            self.tkImage = PIL.ImageTk.PhotoImage(PIL.ImageOps.expand(self.PilImage, border=1, fill=(0, 0, 0)))
        else:
            self.tkImage = PIL.ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(self.position[0], self.position[1],
                                                    image=self.tkImage, anchor=self.anchorPoint)

    #symbol k
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

    #Symbol: p
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
    def resize(self, width=None, height=None, scalar=1):

        """
        Resize method where image is resized to new width and new height
        :param width: Width in pixels
        :param height: Height in pixels
        :param scalar: a scalar that width and height are multiplied by
        :exception if either width/height inputed but not the other, method
                   will scale the other value maintaining aspect ratio
                   """

        if not(width is None or height is None):
            self.PilImage = self.PilImage.resize((int(scalar * width), int(scalar * height)), PIL.Image.NEAREST)
            self.displayImage()
            pass

        if width is None:
            width = self.getWidth()
        if height is None:
            height = self.getHeight()

        height = (height * width) / self.getWidth()
        width = (width * height) / self.getHeight()
        self.PilImage = self.PilImage.resize((int(scalar * width), int(scalar * height)), PIL.Image.NEAREST)
        self.displayImage()

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
        :param val: Value is float with 0 being black and 1 being
        the original brightness. For most images,
        100 would achieve full whiteness but the theoretical
        limit is infinity.
        """
        enhancer = PIL.ImageEnhance.Brightness(self.PilImage)
        self.PilImage = enhancer.enhance(val)
        self.displayImage()

    # Symbol: g
    def greyscale(self):
        """
        Put the image into greyscale
        No Parameters
        """
        alphaChannel = self.PilImage.split()[-1]
        self.PilImage = self.PilImage.convert("L")
        self.PilImage.putalpha(alphaChannel)
        self.PilImage = self.PilImage.convert("RGBA")
        self.displayImage()

    def getCopy(self):
        """
        Returns a copy of the instance where are values are fully
        independent except for the canvas, because both objects are displayed
        on the same canvas. Not used in our testing, and not implemented in the parser.
        :return: a copy of the Element instance
        """
        newElement = Element()
        newElement.PilImage = self.PilImage
        newElement.canvas = self.canvas
        newElement.showBorder = self.showBorder
        newElement.anchorPoint = self.anchorPoint
        newElement.position = self.position
        newElement.displayImage()
        return newElement

    def getHeight(self):
        return self.PilImage.height

    def getWidth(self):
        return self.PilImage.width
