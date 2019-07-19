from tkinter import *
import tkinter
from imgCommands import Element
import settings


#Tkinter canvas setup
canvas = settings.createCanvas(1000, 1000)

#Define anchor
center = tkinter.CENTER


Back = Element(canvas, "/home/ganesh/workspaces/WAIC/testImages/TEST3.jpg", center, False)

Back.resize(500, 500)
Back.onion(60)


imgOne = Element(canvas, "/home/ganesh/workspaces/WAIC/testImages/TEST3.jpg", center, True)

imgOne.resize(500, 500)
imgOne.rotate(90)
imgOne.smudge(4)
imgOne.mirror()
imgOne.translate(1000, 1001)


#Show canvas:
mainloop()





