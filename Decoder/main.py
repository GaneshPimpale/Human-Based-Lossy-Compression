from tkinter import *
from imgCommands import edit, measure


#Tkinter canvas setup
root = Tk()
canvas = Canvas(root, width = 800, height = 800)
canvas.pack(fill='both', expand=True)


#Example Command execution:

#Define image:
Back = edit(canvas, "/home/ganesh/workspaces/WAIC/testImages/TEST3.jpg")

#Edit Images:
Back.resize(500, 500)
Back.onion(60, 500, 500)


imgOne = edit(canvas, "/home/ganesh/workspaces/WAIC/testImages/TEST3.jpg")

imgOne.crop(0, 2, 0, 1)
imgOne.resize(500, 500)
imgOne.rotate(90)
imgOne.smudge(4)
imgOne.mirror()
imgOne.translate(100, 200)


#Show canvas:
root.mainloop()





