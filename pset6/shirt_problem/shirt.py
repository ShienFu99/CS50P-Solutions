# HOW TO RUN: shirt.py *NAME OF IMAGE FILE w/ EXT* *NEW NAME OF IMAGE w/ SAME EXT*
# Description: Takes the name of an image file from the user and overlays a CS50 shirt over it
# > Expects two command-line arguments -> The name of the image file and the name of the new image file
# > Extensions must be the same (accepted extensions are .png, .jpg and .jpeg)


#Imports
import sys
from PIL import Image, ImageOps
import os


def main():
    #User must input 2 command-line arguments
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    #Stores file extensions (with periods) in lowercase
    ext1 = os.path.splitext(sys.argv[1])[1].lower()
    ext2 = os.path.splitext(sys.argv[2])[1].lower()

    #First file extension must be .png, .jpeg, or .jpg
    match ext1:
        case ".jpeg" | ".jpg" | ".png":
            pass
        case _:
            sys.exit("Invalid input")

    #Second file extension must match first one
    if ext2 != ext1:
        sys.exit("Invalid input")

    #Opens shirt.png
    shirt = Image.open("shirt.png")

    #Store the dimensions of shirt.png as a tuple
    (width, height) = shirt.size

    #Opens the user's image (first command-line argument)
    image_before = Image.open(sys.argv[1])

    #Resizes the user's image to the dimensions of shirt.png
    image_after = ImageOps.fit(image_before, (width, height))

    #Paste shirt.png onto the user's resized image
    image_after.paste(shirt, shirt)

    #Saves the image after it's been altered under the name of the second command-line argument
    image_after.save(sys.argv[2])


if __name__ == "__main__":
    main()
