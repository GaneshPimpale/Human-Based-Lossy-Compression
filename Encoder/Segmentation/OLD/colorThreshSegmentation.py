#Written by Ganesh Pimpale
import cv2
import numpy as np
from matplotlib import pyplot as plt


#Input file:
img = cv2.imread("TEST3.jpg") 

#Grayscale Image:    #Do I even need this???
grayScale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#HSV Image:    #Do I even need this???
HSVImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Blur Image:
blurImg = cv2.blur(img, (10, 10))


#Posterize/quantize image:
n = 2     #quantization level

###   ALL OF THIS STUFF IS NOT FINAL!!!
indices = np.arange(0,256)   # List of all colors
divider = np.linspace(0,255,n+1)[1] # we get a divider
quantiz = np.int0(np.linspace(0,255,n)) # we get quantization colors
color_levels = np.clip(np.int0(indices/divider),0,n-1) # color levels 0,1,2..
palette = quantiz[color_levels] # Creating the palette

pImg = palette[blurImg]  # Applying palette on image
pImg = cv2.convertScaleAbs(pImg) # Converting image back to uint8
###


#Edge detection:
lowerColor = np.array([30,150,50])
upperColor = np.array([255,255,180])

mask = cv2.inRange(pImg, lowerColor, upperColor)
edge = cv2.Canny(pImg, 100, 200)


#Resizing and Formatting:
scale = 100
width = int(img.shape[1] * scale/100)
height = int(img.shape[0] * scale/100)
dimensions = (width, height)

resizeImg = cv2.resize(img, dimensions)
resizeBimg = cv2.resize(blurImg, dimensions)
resizePImg = cv2.resize(pImg, dimensions)
resizeEImg = cv2.resize(edge, dimensions)


#Deconstructing image:



#Output:
#finalImg =  cv2.addWeighted(resizePImg, 0.5, resizeEImg, 0.5, 0)

while(True):
    #Show images
    cv2.imshow("TEST Original", resizeImg)
    cv2.imshow("TEST BLur", resizeBimg)
    cv2.imshow("TEST Quantization", resizePImg)
    cv2.imshow("TEST Edge on Quantization", resizeEImg)
    #cv2.imshow("TEST Quantization & Edge", finalImg)

    #Show histogram
    plt.hist(img.ravel(),256,[0,256])
    plt.show()

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()





