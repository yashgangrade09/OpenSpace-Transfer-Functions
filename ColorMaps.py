import cv2
   
im = cv2.imread("convImg.png")  
im_color = cv2.applyColorMap(im, cv2.COLORMAP_RAINBOW)

cv2.imwrite('testimgColor3.png',im_color)
