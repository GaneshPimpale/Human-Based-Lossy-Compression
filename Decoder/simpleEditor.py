from PIL import Image, ImageDraw, ImageFont

onion = Image.open("savanna.png").convert("RGBA")
onion.putalpha(60)
penguin = Image.open("penguin.png").convert("RGBA")
bg = Image.new('RGBA', onion.size, (255,255,255,0))

#If I don't add "onion" as a mask (third parameter) the image
#saves properly, but doesn't display properly.
#If I do the other way around, it displays properly, but doesn't
#save properly
#See if displaying it via Tkinter solves the problem

#bg.paste(onion, (0, 0), onion)
bg.paste(onion, (0,0), onion)
bg.paste(penguin, (50,50), penguin)

bg.show()
bg.save("compressed.png")