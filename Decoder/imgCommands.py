import PIL.Image
from PIL import ImageTk, ImageFilter
from tkinter import *


class edit():
    def __init__(self, canvas, file):
        self.canvas = canvas
        self.PilImage = PIL.Image.open(file).convert("RGBA") # The original PIL image
        self.scaledDimensions = [100, 100]

        # A the image objects necessary for displaying in Tkinter
        self.tkImage = ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(0, 0, image=self.tkImage, anchor=NW)

        self.x = [0, 100]
        self.y = [0, 100]

        #Parser WILL save these commands:
        #Symbol: x
    def crop(self, ratioX1, ratioY1, ratioX2, ratioY2):
        self.x[0] = self.tkImage.width() * ratioX1
        self.x[1] = self.tkImage.width() * ratioX2

        self.y[0] = self.tkImage.height() * ratioY1
        self.y[1] = self.tkImage.height() * ratioY2

        self.PilImage = self.PilImage.crop((self.x[0], self.y[0], self.x[1], self.y[1]))
        self.tkImage = ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(self.x[0], self.y[0], image=self.tkImage, anchor=NW)

        print("CROP DONE")

        #Symbol: o
    def rotate(self, angleInDegrees):
        print(self.tkImage.width())

        self.PilImage = self.PilImage.rotate(angleInDegrees, expand=True, resample=PIL.Image.BICUBIC)
        self.tkImage = ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(self.x[0], self.y[0], image=self.tkImage, anchor=NW)

        print(self.tkImage.width())
        print("rotate DONE")

        #Symbol: r
    def resize(self, X, Y):
        self.PilImage = self.PilImage.resize((X, Y), PIL.Image.NEAREST)
        self.tkImage = ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(self.x[0], self.y[0], image=self.tkImage, anchor=NW)

        print("resize DONE")

        #Symbol: t
    def translate(self, X, Y):
        self.tkImage = ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(self.x[X], self.y[Y], image=self.tkImage, anchor=NW)

        print("translate DONE")

        #Symbol: s
    def smudge(self, blurVal ):
        self.PilImage = self.PilImage.filter(ImageFilter.GaussianBlur(radius = blurVal))
        self.tkImage = ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(self.x[0], self.y[0], image=self.tkImage, anchor=NW)

        print("smudge DONE")

        #Symbol: m
        #Always mirrors over the vertical axis (left to right)
    def mirror(self):
        self.PilImage = self.PilImage.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        self.tkImage = ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(self.x[0], self.y[0], image=self.tkImage, anchor=NW)
        print ("mirror DONE")


#Parser will NOT save these commands:
class measure():
    def getDimension(Img):
        dim = Img.size
        print(dim)
        return dim

    def getHeight(Img):
        width, height = Img.size
        print (height)
        return height

    def getWidth(Img):
        width, height = Img.size
        print(width)
        return width


'''
TODO:
-translate function seems sketchy

-Change crop input values

-Crop: DONE
-Rotate: DONE
-Resize:
-Translate:
-Mirror: DONE
-Smudge: DONE
'''



