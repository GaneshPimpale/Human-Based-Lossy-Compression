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
    
def grid(box_x, box_y):
    for i in range(1, int(canvas.winfo_width()/box_x)+1):
        canvas.create_line(i*box_x, 0, i*box_x, canvas.winfo_height(), fill="gray")

    for i in range(1, int(canvas.winfo_height()/box_y)+1):
        canvas.create_line(0, i * box_y, canvas.winfo_width(), i*box_y, fill="gray")

    for i in range(1, int(canvas.winfo_width()/box_x)+1):
        canvas.create_text(i * box_x, 15, text=str(i * box_x))

    for i in range(1, int(canvas.winfo_height()/box_y)+1):
        canvas.create_text(15, i*box_y, text=str(i * box_y))




