'''
Doesn't need to import PIL because all of that is handled by the ImageElement
class.
'''

#from TkLearning.photo_editor_classes import ImageElement
from tkinter import *
global element, buttonList


def mouseDragged(event):
    if action == "Resize":
        print("Resize selected")
    elif action == "Crop":
        print("Crop selected")


def mouseReleased(event):
    #element.resize(event.x, event.y)
    pass

def mousePressed(event):
    if action == "Crop":
        pass



def resizeSelected():
    global action, resizeButton, cropButton
    action = "Resize"
    handleButtonHighlighting(resizeButton)

def cropSelected():
    global action, resizeButton, cropButton
    action = "Crop"
    handleButtonHighlighting(cropButton)

"""
Function: Handle Button Highlighting
Parameters:
    selectedButton: the button that was just selected
Behavior:
    Loops through a list of all the button and un-highlights all of them.
    Then highlights the button that was just selected.
Notes:
    Button highlighting could also conceivably be achieved by keepin 
"""
def handleButtonHighlighting(selectedButton):
    for button in buttonList:
        button.config(relief=RAISED)
    selectedButton.config(relief=SUNKEN)

"""
Function: Initialize Window
Behavior:
    Initializes the GUI for the photo editor. The window has two children:
        buttonFrame: the frame the contains the buttons that change the functions
        canvas: where the images are displayed and manipulated using the cursor
    Buttons are not only added visually to the buttonFrame but are also added to 
    buttonList because this allows us to loop through a list of all buttons
    when changing button highlighting.
    Also sets the default mouse action to "Move"
    TODO: Create a seperate initialize button function
"""
def initializeWindow():
    global action, root, canvas, resizeButton, cropButton, buttonList
    #Create the window
    root = Tk()

    #Create and pack the canvas the button frames. The canvas is to the left
    #and the button frame is to the right
    canvas = Canvas(root, width=600, height=400, bd = 5, relief=RIDGE)
    buttonFrame = Frame(root)
    buttonFrame.pack(side = RIGHT)
    canvas.pack(fill="both", expand=True, side = LEFT)

    #Create the buttons, add them to buttonList, and pack them
    resizeButton = Button(buttonFrame, text="Resize", command=resizeSelected)
    cropButton = Button(buttonFrame, text="Crop", command=cropSelected)
    buttonList = []
    buttonList.append(resizeButton)
    buttonList.append(cropButton)
    resizeButton.pack()
    cropButton.pack()

    #Initialize the default mouse action
    action = "Move"

initializeWindow()

#Create an image asset
#element = ImageElement(canvas, 'Bird.jpeg')





canvas.bind('<Button-1>', mousePressed)
canvas.bind('<B1-Motion>', mouseDragged)
canvas.bind('<ButtonRelease-1>', mouseReleased)
root.mainloop()