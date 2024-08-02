import sys
import os

from PIL import Image, ImageOps

try:
    if len(sys.argv) == 3:
        exts = [".jpg", ".jpeg", ".png"]
        # use os.path.splitext to get a tuple of file_name + extension
        ext1 = os.path.splitext(sys.argv[1])
        ext2 = os.path.splitext(sys.argv[2])
        # indexing ext1 or ext2
        if ext1[1] == ext2[1] and ext1[1] in exts:
            shirt = Image.open("shirt.png") # open shirt.png
            size_shirt = shirt.size # get the size of shirt.png
            muppet = Image.open(sys.argv[1]) # open muppet image in new file
            muppet = ImageOps.fit(muppet, size_shirt) # crop muppet image size to shirt.png size
            muppet.paste(shirt, shirt) # paste following shirt pixel
            muppet.save(sys.argv[2]) # saving overlay image in new file
        elif ext1[1] != ext2[1]:
            sys.exit("Input and output have different extensions")
        else:
            raise FileNotFoundError
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        raise FileNotFoundError

except FileNotFoundError:
    sys.exit("File does not exist")
