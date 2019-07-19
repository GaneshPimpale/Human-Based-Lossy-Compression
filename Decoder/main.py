from tkinter import *
import tkinter
from imgCommands import Element
import settings

#Tkinter canvas setup
canvas settings.createCanvas(1000, 1000)
NW = tkinter.NW


#Example Command execution:

#Define image:
Back = Element(canvas, "/home/ganesh/workspaces/WAIC/testImages/TEST3.jpg", NW, False)

#Edit Images:
Back.resize(500, 500)
Back.onion(60, 500, 500)


imgOne = Element(canvas, "/home/ganesh/workspaces/WAIC/testImages/TEST3.jpg", NE, False)

imgOne.crop(0, 2, 0, 1)
imgOne.resize(500, 500)
imgOne.rotate(90)
imgOne.smudge(4)
imgOne.mirror()
imgOne.translate(100, 200)


#Show canvas:
mainloop()





