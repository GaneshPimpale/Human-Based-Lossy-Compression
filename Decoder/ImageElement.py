import PIL.Image, PIL.ImageTk, PIL.ImageFilter, PIL.ImageOps
from tkinter import *

class Element:

    def __init__(self, canvas, file, anchor, displayBorder):

        self.canvas = canvas
        self.PilImage = PIL.Image.open(file).convert("RGBA") # The original PIL image

        self.displayBorder = displayBorder
        self.anchorPoint = anchor

        # A the image objects necessary for displaying in Tkinter
        self.tkImage = PIL.ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(0, 0, image=self.tkImage, anchor=self.anchorPoint)

    def displayImage(self, x=0, y=0):
        if self.displayBorder:
            self.tkImage = PIL.ImageTk.PhotoImage(PIL.ImageOps.expand(self.PilImage, border=1, fill=(0, 0, 0)))
        else:
            self.tkImage = PIL.ImageTk.PhotoImage(self.PilImage)
        self.canvasImage = self.canvas.create_image(x, y, image=self.tkImage, anchor=self.anchorPoint)

    def cropRatio(self, ratioX0, ratioY0, ratioX1, ratioY1):

        x, y = [0, 100], [0, 100]

        x[0] = self.tkImage.width() * ratioX0
        y[0] = self.tkImage.height() * ratioY0

        x[1] = self.tkImage.width() * ratioX1
        y[1] = self.tkImage.height() * ratioY1

        self.PilImage = self.PilImage.crop((x[0], y[0], x[1], y[1]))
        self.displayImage()

    #Parser WILL save these commands:
    #Symbol: x
    def cropPixel(self, x1, y1, x2, y2):
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
        self.PilImage = self.PilImage.resize((width, height), PIL.Image.NEAREST)
        self.displayImage()
        print("resize DONE")

    #Symbol: t
    def translate(self, canvasX, canvasY):
        self.displayImage(canvasX, canvasY)
        print("translate DONE")

    #Symbol: s
    def smudge(self, blurVal ):
        self.PilImage = self.PilImage.filter(PIL.ImageFilter.GaussianBlur(radius = blurVal))
        self.displayImage()

        print("smudge DONE")

    #Symbol: m
    #Always mirrors over the vertical axis (left to right)
    def mirror(self):
        self.PilImage = self.PilImage.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        self.displayImage()


        print ("mirror DONE")

    #Parser will not save this command:
    def onion(self, val):
        onion = self.PilImage
        onion.putalpha(val)
        bg = PIL.Image.new("RGBA",(self.PilImage.width, self.PilImage.height) , (255, 255, 255, 250))
        bg.paste(onion, (0, 0), onion)
        self.tkImage = PIL.ImageTk.PhotoImage(bg)
        self.canvasImage = self.canvas.create_image(self.x[0], self.y[0], image=self.tkImage, anchor=CENTER)

        print ("onion DONE")

    def getHeight(self):
        return self.PilImage.height

    def getWidth(self):
        return self.PilImage.width
