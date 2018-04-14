import cv2
import numpy as np
import math
from numpy import linalg as LA

#Search for Pixel In Legend
def searchPixel(lg, curPix, dim_legend):
    if curPix[0] <= 25 and curPix[1] <= 25 and curPix[2] <= 25:
        return 0
    
    bestindex = 0
    best = LA.norm(np.array([[ int(lg[0][0][0])-int(curPix[0]), int(lg[0][0][1])-int(curPix[1]), int(lg[0][0][2])-int(curPix[2])   ]] ),np.inf)
   
    for x in range(dim_legend):
        if lg[0][x][0] == curPix[0] and lg[0][x][1] == curPix[1] and lg[0][x][2] == curPix[2]:
            return math.floor(x / dim_legend * 255)
        
        bestTest = LA.norm(np.array([[ int(lg[0][x][0])-int(curPix[0]), int(lg[0][x][1])-int(curPix[1]), int(lg[0][x][2])-int(curPix[2])   ]] ),np.inf)
        if best > bestTest :
            bestindex = x
            best = bestTest
                
    return math.floor((bestindex / dim_legend) * 255)

    
#Reading In Files
srclg = cv2.imread("color_bar_legendv2.png")
srcImg = cv2.imread("EntireWorld_Temperature_Day.png")

dim_legend = srclg.shape[1]
row_input = srcImg.shape[0]
col_input = srcImg.shape[1]

#Loop Over Pixels
conImg = []
for i in range(row_input):
    print(i)
    conImg.append([])
    for j in range(col_input):
        conImg[i].append( searchPixel(srclg, srcImg[i][j], dim_legend) )      
        
conImg = np.asarray(conImg)  
cv2.imwrite('EntireWorldConverted.png', conImg)
print("Done")



#===========================OLD CODE============================
## Reading In Files
#srclg = cv2.imread("color_bar_legend.png")
#srcImg = cv2.imread("day_temperature_2018-03-23.png")
#
#conImg = []
#for i in range(864):
#    conImg.append([])
#    for j in range(848):
#        conImg[i].append(int( round(srcImg[i][j][0]*0.21 + srcImg[i][j][1]*0.72 + srcImg[i][j][2]*0.07)) )
#        
#conImg = np.asarray(conImg)        
#
#
##plt.imshow(conImg, cmap='gray')
##plt.savefig('convImg.png')
#
#
#cv2.imwrite('convImg.png', conImg)