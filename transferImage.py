import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

# Reading In Files
srclg = cv2.imread("color_bar_legend.png")
srcImg = cv2.imread("day_temperature_2018-03-23.png")

conImg = []
for i in range(864):
    conImg.append([])
    for j in range(848):
        conImg[i].append(int( round(srcImg[i][j][0]*0.21 + srcImg[i][j][1]*0.72 + srcImg[i][j][2]*0.07)) )
        
conImg = np.asarray(conImg)        


#plt.imshow(conImg, cmap='gray')
#plt.savefig('convImg.png')


cv2.imwrite('convImg.png', conImg)