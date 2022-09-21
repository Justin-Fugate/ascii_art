from PIL import Image
from numpy import asarray
from matplotlib import image
from matplotlib import pyplot

from ascii import chars

#image = image.imread("ascii-pineapple.jpg")

image = Image.open("ascii-pineapple.jpg")
data = asarray(image)

def average_value():
    for pixel in data:
    data[
pyplot.imshow(image)
pyplot.show()
print(image.size)