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
    cm_spring = mpl.cm.get_cmap('spring')
    cm_summer = mpl.cm.get_cmap('summer')
    cm_autumn = mpl.cm.get_cmap('autumn')
    cm_winter = mpl.cm.get_cmap('winter')
    cm_grey = mpl.cm.get_cmap('gray')
    cm_hsv = mpl.cm.get_cmap('hsv')
    cm_jet = mpl.cm.get_cmap('jet')

    #img_src = Image.open('Jupiter_Globe.jpg').convert('L')
    image_name = "space"
    img_src = Image.open(image_name + ".jpg").convert('L')
    width, height = img_src.size
    img_src.thumbnail((width, height))
    im = np.array(img_src)
    im9 = cm_grey(im)
    save_Image(im9, image_name + "_grey.png")



    img_src = Image.open(image_name + "_grey.png").convert('L')
    img_src.thumbnail((width, height))
    im = np.array(img_src)


    im2 = cm_purples(im)
    im3 = cm_cool(im)
    im4 = cm_hot(im)
    im5 = cm_spring(im)
    im6 = cm_summer(im)
    im7 = cm_autumn(im)
    im8 = cm_winter(im)
    im10 = cm_hsv(im)
    im11 = cm_jet(im)

    #image_name = image_name + "//" + image_name
    save_Image(im4, image_name + "_hot.png")
    save_Image(im2, image_name + "_purple.png")
    save_Image(im3, image_name + "_cool.png")
    save_Image(im5, image_name + "_spring.png")
    save_Image(im6, image_name + "_summer.png")
    save_Image(im7, image_name + "_autumn.png")
    save_Image(im8, image_name + "_winter.png")
    save_Image(im10, image_name + "_hsv.png")
    save_Image(im11, image_name + "_jet.png")


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
    t = timeit.timeit(pil_test, number=1)
    print('PIL: %s' % t)
    #t = timeit.timeit(plt_test, number=30)
    #print('PLT: %s' % t)
    exit(0)