import tkinter as tk
import pyscreenshot

def createCanvas(x, y):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=x, height=y)
    canvas.pack(fill="both", expand=True)
    return canvas
def printCanvas(canvas, file_path):
    box = (canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_rootx() + canvas.winfo_width(),
           canvas.winfo_rooty() + canvas.winfo_height())
    grab = pyscreenshot.grab(bbox=box)
    grab.save(file_path)

