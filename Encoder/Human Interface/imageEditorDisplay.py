import PIL.Image
from PIL import ImageTk
from tkinter import *


def commandEntered(event):
    #Get command entered in textBox
    cmd = prompt.get()

    #Handle command to init the onionskinned base image
    if cmd[:4] == "init" or cmd[:4] == "Init":
        filePath = cmd[5:len(cmd) - 1]
        displayBaseImage(filePath)

    #Call the image edit functions and update the window


def displayBaseImage(filePath):
    global image
    baseImagePIL = PIL.Image.open(filePath)
    baseImageTk = ImageTk.PhotoImage(baseImagePIL)

    # Resize the canvas to perfectly fit the image
    canvas.config(width=baseImageTk.width(), height=baseImageTk.height())

    #Should display the image, but garbage collection gets in the way
    image = canvas.create_image(0,0, image=baseImageTk, anchor = NW)

    #It will display this rectangle though
    rect = canvas.create_rectangle(0,0,100,100)



#Initialize the window
root = Tk()

# Create the display canvas
canvas = Canvas(root, width=200, height=200)
canvas.pack(expand=True)

#Create the prompt bar to capture commands
prompt = Entry(root)
prompt.pack()
prompt.bind("<Return>", commandEntered)

#Main animation loop
root.mainloop()
