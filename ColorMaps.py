import cv2
import numpy as np
   
im = cv2.imread("testimgGray.png", cv2.IMREAD_GRAYSCALE)  
im_color = cv2.applyColorMap(im, cv2.COLORMAP_HOT)

cv2.imwrite('testimgColor.png',im_color)