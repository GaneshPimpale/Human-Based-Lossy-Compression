import PIL.Image
from PIL import ImageTk, ImageFilter, ImageDraw, ImageFont, Image
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
    def crop(self, X0, Y0, X1, Y1):
        self.PilImage = self.PilImage.crop((X0, Y0, X1, Y1))
        self.tkImage = ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(self.x[0], self.y[0], image=self.tkImage, anchor=NW)

        print("crop DONE")

    #Symbol: o
    def rotate(self, angleInDegrees):
        self.PilImage = self.PilImage.rotate(angleInDegrees, expand=True, resample=PIL.Image.BICUBIC)
        self.tkImage = ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(self.x[0], self.y[0], image=self.tkImage, anchor=NW)

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
        self.canvasImage = self.canvas.create_image(X, Y, image=self.tkImage, anchor=NW)

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

    #Parser will not save this command:
    def onion(self, val, X, Y):
        onion = self.PilImage
        onion.putalpha(val)
        bg = PIL.Image.new("RGBA",(X, Y) , (255, 255, 255, 250))
        bg.paste(onion, (0, 0), onion)
        self.tkImage = ImageTk.PhotoImage(bg)
        self.canvasImage = self.canvas.create_image(self.x[0], self.y[0], image=self.tkImage, anchor=NW)

        print ("onion DONE")


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



