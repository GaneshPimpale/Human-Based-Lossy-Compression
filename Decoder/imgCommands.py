import PIL.Image
from PIL import ImageTk, ImageFilter, ImageDraw, ImageFont, Image
from tkinter import *


class edit():
    def __init__(self, canvas, anchor, file):
        self.canvas = canvas
        self.PilImage = PIL.Image.open(file).convert("RGBA") # The original PIL image
        self.scaledDimensions = [100, 100]
        self.anchorPoint = anchor

        # A the image objects necessary for displaying in Tkinter
        self.tkImage = ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(0, 0, image=self.tkImage, anchor=self.anchorPoint)

        self.x = [0, 100]
        self.y = [0, 100]

    #Parser WILL save these commands:
    #Symbol: k
    def cropRatio(self, ratioX0, ratioY0, ratioX1, ratioY1):
        self.x[0] = self.tkImage.width() * ratioX0
        self.y[0] = self.tkImage.height() * ratioY0

        self.x[1] = self.tkImage.width() * ratioX1
        self.y[1] = self.tkImage.height() * ratioY1

        self.PilImage = self.PilImage.crop((self.x[0], self.y[0], self.x[1], self.y[1]))
        self.tkImage = ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(self.x[0], self.y[0], image=self.tkImage, anchor=self.anchorPoint)

        print("crop DONE")

    #Symbol: p
    def cropPixel(self, X0, Y0, X1, Y1):
        self.PilImage = self.PilImage.crop((X0, Y0, X1, Y1))
        self.tkImage = ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(self.x[0], self.y[0], image=self.tkImage, anchor=self.anchorPoint)

        print("ceop DONE ")

    #Symbol: o
    def rotate(self, angleInDegrees):
        self.PilImage = self.PilImage.rotate(angleInDegrees, expand=True, resample=PIL.Image.BICUBIC)
        self.tkImage = ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(self.x[0], self.y[0], image=self.tkImage, anchor=self.anchorPoint)

        print("rotate DONE")

    #Symbol: r
    def resize(self, X, Y):
        self.PilImage = self.PilImage.resize((X, Y), PIL.Image.NEAREST)
        self.tkImage = ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(self.x[0], self.y[0], image=self.tkImage, anchor=self.anchorPoint)

        print("resize DONE")

    #Symbol: t
    def translate(self, X, Y):
        self.tkImage = ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(X, Y, image=self.tkImage, anchor=self.anchorPoint)

        print("translate DONE")

    #Symbol: s
    def smudge(self, blurVal ):
        self.PilImage = self.PilImage.filter(ImageFilter.GaussianBlur(radius = blurVal))
        self.tkImage = ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(self.x[0], self.y[0], image=self.tkImage, anchor=self.anchorPoint)

        print("smudge DONE")

    #Symbol: m
    #Always mirrors over the vertical axis (left to right)
    def mirror(self):
        self.PilImage = self.PilImage.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        self.tkImage = ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(self.x[0], self.y[0], image=self.tkImage, anchor=self.anchorPoint)

        print("mirror DONE")

    #Parser will not save this command:
    def onion(self, val):
        onion = self.PilImage
        onion.putalpha(val)
        bg = PIL.Image.new("RGBA",(self.PilImage.width, self.PilImage.height) , (255, 255, 255, 250))
        bg.paste(onion, (0, 0), onion)
        self.tkImage = ImageTk.PhotoImage(bg)
        self.canvasImage = self.canvas.create_image(self.x[0], self.y[0], image=self.tkImage, anchor=self.anchorPoint)

        print("onion DONE")

    #Parser will not save this command:
    def save(self, name):

        print("saved" + name)


class measure():
    def getDimension(Img):
        dim = Img.size
        print(dim)
        return dim

    def getHeight(Img):
        width, height = Img.size
        print(height)
        return height

    def getWidth(Img):
        width, height = Img.size
        print(width)
        return width


class settings():
    def createCanvas(X, Y):
        root = Tk()
        canvas = Canvas(root, width = X, height = Y)
        canvas.pack(fill = "both", expand = True)

        print("canvas MADE")
        return canvas

    def imports():

        print("packages imported")

'''
TODO:
-Save function: resize canvas to proper size, export canvas
-
'''





