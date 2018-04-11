import cv2
   
im = cv2.imread("day_temperature_2018-03-23.png")  
im_color = cv2.applyColorMap(im, cv2.COLORMAP_HOT)

cv2.imwrite('testimgColor4.png',im_color)
