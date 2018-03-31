import cv2
import numpy as np
import numpy as numpy
   
im = cv2.imread("testimgGray.png", cv2.IMREAD_GRAYSCALE)  
im_color = cv2.applyColorMap(im, cv2.COLORMAP_HOT)

cv2.imwrite('testimgColor.png',im_color)



grey_levels = 256
# Generate a test image

# Define the window size
windowsize_r = 5
windowsize_c = 5

# Crop out the window and calculate the histogram
for r in range(0,im.shape[0] - windowsize_r, windowsize_r):
    for c in range(0,im.shape[1] - windowsize_c, windowsize_c):
        window = im[r:r+windowsize_r,c:c+windowsize_c]
        cv2.imwrite("test.png",window)
        
        
