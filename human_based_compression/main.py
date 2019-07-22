from human_based_compression.element import Element
from human_based_compression.display import Display

def main():
    display = Display(500, 500)
    potato = Element(display, "C:/Users/micha/OneDrive/Documents/Python Scripts/Web-AI-Compression/human_based_compression/Potato.jpg", 'nw', True)
    # potato2 = potato
    # potato2.resize(100,100)
    #potato.onion(50)
    #display.grid(100,100)

    display.mainloop()

if __name__ == '__main__':
    main()



