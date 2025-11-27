#   Before running this python script to create a gif. Run this commands in the terminal:
#       pip install pillow imageio
#   Change the name of the image in the filename list to create a custom gif.
#   Add those image to the project folder.
#   if you don't want to use PIL make sure the images are of the same size.
#   run the script to create a custome gif.
#   It will be saved under the name 'cat_running.gif' in the project folder.


import imageio.v3 as iio
from PIL import Image

filenames = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg']
images = []

first = Image.open(filenames[0])
w,h = first.size

for filename in filenames:
    img = Image.open(filename).resize((w,h))
    images.append(img)

iio.imwrite('cat_running.gif', images, duration=200, loop=0)