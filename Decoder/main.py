from tkinter import *
from imgCommands import edit, measure


#Tkinter canvas setup
root = Tk()
canvas = Canvas(root, width = 800, height = 800)
canvas.pack(fill='both', expand=True)


#Example Command execution:
'''
#Define image:
imgOne = edit(canvas, "/home/ganesh/workspaces/WAIC/testImages/TEST3.jpg")

#Edit Image:
imgOne.crop(0.9, 0.9, 0.9, 0.9)
imgOne.rotate(90)
imgOne.resize(100, 100)
imgOne.translate(100, 100)
imgOne.smudge(5)
imgOne.mirror()
'''


#Show canvas:
root.mainloop()





