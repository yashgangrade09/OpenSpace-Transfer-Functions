import cv2
   
im = cv2.imread("EntireWorldConverted.png")  
im_color = cv2.applyColorMap(im, cv2.COLORMAP_HOT)

cv2.imwrite('EntireWorldConverted_HOT.png',im_color)
