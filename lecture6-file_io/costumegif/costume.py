import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg) #open image using PIL library
    images.append(image)

#save -> opening, writing, closing by PIL library
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
