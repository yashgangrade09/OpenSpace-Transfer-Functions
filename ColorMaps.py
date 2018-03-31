import cv2
import numpy as np
import numpy as numpy
   
im = cv2.imread("testImages/spaceSplit/0-4.png", cv2.IMREAD_GRAYSCALE)  
im_color = cv2.applyColorMap(im, cv2.COLORMAP_HOT)

cv2.imwrite('testimgColor3.png',im_color)
