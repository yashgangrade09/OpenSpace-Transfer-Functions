#!/usr/bin/env python3
#Spencer Fronberg
#OpenSpace Project
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import timeit
from PIL import Image

def pil_test():
    cm_hot = mpl.cm.get_cmap('hot')
    cm_purples = mpl.cm.get_cmap('Purples')
    cm_cool = mpl.cm.get_cmap('cool')

    img_src = Image.open('testimgGray.png').convert('L')
    img_src.thumbnail((512, 512))
    im = np.array(img_src)

    im2 = cm_purples(im)
    im3 = cm_cool(im)
    im = cm_hot(im)

    save_Image(im, 'test_hot.png')
    save_Image(im2, 'test_purple.png')
    save_Image(im3, 'cool.png')

def save_Image(im, image_name):
    im = np.uint8(im * 255)
    im = Image.fromarray(im)
    im.save(image_name)

"""def rgb2gray(rgb):
    return np.dot(rgb[:, :, :3], [0.299, 0.587, 0.114])

def plt_test():
    img_src = mpimg.imread('testimgGray.png')
    im = rgb2gray(img_src)
    f = plt.figure(figsize=(4, 4), dpi=128)
    plt.axis('off')
    plt.imshow(im, cmap='hot')
    plt.savefig('test2_hot.png', dpi=f.dpi)
    plt.close()"""

if __name__ == "__main__":
    t = timeit.timeit(pil_test, number=30)
    print('PIL: %s' % t)
    #t = timeit.timeit(plt_test, number=30)
    #print('PLT: %s' % t)
    exit(0)