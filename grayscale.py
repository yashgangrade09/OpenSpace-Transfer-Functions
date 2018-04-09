# import the necessary packages
import cv2

#Load the image 
image = cv2.imread("testimg.jpg")

# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('testimgGray.png',gray)