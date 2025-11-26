import imageio.v3 as iio
from PIL import Image

filenames = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg']
images = []

first = Image.open(filenames[0])
w,h = first.size

for filename in filenames:
    img = Image.open(filename).resize((w,h))
    images.append(img)

iio.imwrite('cat_running.gif', images, duration=200, loop=0)