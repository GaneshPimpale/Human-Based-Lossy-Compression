# Web-AI-Compression

General Program Structure~
---------------------------
Compression:
-Must have a preset database of images to use from before
-AI:
   -Break down the image on the user's end
   -Logically isolate objects using vision algorithms
   -Identify each of the isolated objects and rank thm based on their importance of the image
-The broken down image on the user's end will be compared to the images in the database
-Compressed file will be transformations between the user's image and the image components on the database.

Decompression:
-Each of the commands will cooretate to a python function
-This can be given to GIMP where the editing can take place
-the image creation could also take use of an image editing python library
