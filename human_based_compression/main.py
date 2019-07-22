from human_based_compression.element import Element
from human_based_compression.display import Display

# Encapsulated the canvas functions as the 'Display' class
# and renamed the 'settings' file to display

# Added the if __name__ == '__main__' idiom to the code
# so that pyscreenshot would operate properly

# Renamed imgCommands.py to element.py

# Element constructor now takes in display object as constructor rather than
# canvas object

# Added a .resize() function to the display that will be useful later

def main():
    display = Display(500, 500)
    potatoPath = "C:/Users/micha/OneDrive/Documents/Python Scripts/Web-AI-Compression/human_based_compression/Potato.jpg"
    potato = Element(display, potatoPath, 'nw', True)
    #potato.onion(50)
    #display.grid(100,100)




    display.animate()
    pass

if __name__ == '__main__':
    main()



