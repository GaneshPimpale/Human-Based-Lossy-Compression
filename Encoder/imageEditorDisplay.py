from tkinter import *

def commandEntered(event):
    #Get command entered in textBox
    cmd = prompt.get()

    #Call the image edit functions and update the window

#Initialize the window
root = Tk()

#Create the display canvas
canvas = Canvas(root, width = 500, height = 500)
canvas.pack()

#Create the prompt bar to capture commands
prompt = Entry(root)
prompt.pack()
prompt.bind("<Return>", commandEntered)

#Main animation loop
root.mainloop()
