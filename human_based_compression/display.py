import tkinter as tk
import pyscreenshot
import time


class Display:
    """
    The display class that generates the tkinter canvas for displaying the composite as it
    is being edited and save the display as an image file. 
    It includes options to resize and overlay a ruler / grid.

   :param width: The width of the canvas
   :param height: The height of the canvas
    """
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill="both", expand=True)
        self.root.update()

    def resize(self, width, height):
        """
        Resizes the canvas

        :param width: The width that the canvas is resized to
        :param height: The height the canvas is resized to
        """
        self.canvas.config(width=width, height=height)

    def printCanvas(self, path):
        """
        Takes a screenshot of the canvas

        :param path: The path to which the screenshot will be saved
        """
        # Update the canvas to include all the added elements
        self.root.update()

        box = (self.canvas.winfo_rootx(), self.canvas.winfo_rooty(), self.canvas.winfo_rootx() + self.canvas.winfo_width(),
               self.canvas.winfo_rooty() + self.canvas.winfo_height())
        print(box)
        grab = pyscreenshot.grab(bbox=box)

        #Need to wait or else there is weird ghosting from other windows
        time.sleep(2)

        grab.save(path)

    def grid(self, box_x, box_y):
        """
        Adds a labeled grid to the canvas to aid in the editing process

        :param box_x: The width between each vertical grid line
        :param box_y: The height between each horizontal grid line
        """
        self.root.update()
        for i in range(1, int(self.canvas.winfo_width()/box_x)+1):
            self.canvas.create_line(i*box_x, 0, i*box_x, self.canvas.winfo_height(), fill="gray")

        for i in range(1, int(self.canvas.winfo_height()/box_y)+1):
            self.canvas.create_line(0, i * box_y, self.canvas.winfo_width(), i*box_y, fill="gray")

        for i in range(1, int(self.canvas.winfo_width()/box_x)+1):
            self.canvas.create_text(i * box_x, 15, text=str(i * box_x))

        for i in range(1, int(self.canvas.winfo_height()/box_y)+1):
            self.canvas.create_text(15, i*box_y, text=str(i * box_y))


    def mainloop(self):
        """
        Animates the window
        """
        self.root.mainloop()




