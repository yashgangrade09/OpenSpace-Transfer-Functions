#Using Python library Pillow
from PIL import Image

#Convert Image to Grayscale
img = Image.open('testimg.jpg').convert('LA')
img.save('testimgConvr.png')