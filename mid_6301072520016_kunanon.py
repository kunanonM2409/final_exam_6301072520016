from ctypes.wintypes import PINT
from operator import truediv
from pickle import TRUE
from tkinter import font
from unittest import result
import cv2
from cv2 import resize 
import numpy


img=cv2.imread('kunanon.jpg')
img=cv2.resize(img,(700,700))
noise=cv2.GaussianBlur(img,(5,5),0)
img2 =cv2.fastNlMeansDenoisingColored(noise,None,11,11,7,7)
hsv = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)

#orage
lower = numpy.array([20,70,70])
upper = numpy.array([30,255,255])
mask=cv2.inRange(hsv,lower,upper)
result = cv2.bitwise_and(img2,img2,mask=mask)

#blue
lower1 = numpy.array([100,60,60])
upper1 = numpy.array([110,200,200])
mask1=cv2.inRange(hsv,lower1,upper1)
result1=cv2.bitwise_and(img2,img2,mask=mask1)

#pink
lower2 = numpy.array([140,35,35])
upper2 = numpy.array([190,255,255])
mask2=cv2.inRange(hsv,lower2,upper2)
result2 = cv2.bitwise_and(img2,img2,mask=mask2)

#cream
lower3 = numpy.array([5,40,40])
upper3 = numpy.array([18,255,255])
mask3=cv2.inRange(hsv,lower3,upper3)
result3 = cv2.bitwise_and(img2,img2,mask=mask3)

#ิblack
lower4 = numpy.array([0,0,0])
upper4 = numpy.array([200,200,95])
mask4=cv2.inRange(hsv,lower4,upper4)
result4 = cv2.bitwise_and(img2,img2,mask=mask4)



bgimg = numpy.ones((700, 700, 3), dtype=numpy.uint8)*190
orangimg = numpy.zeros((700, 700), dtype=numpy.uint8)
orangimg1 = numpy.zeros((700, 700), dtype=numpy.uint8)
maneethe, hierarchy_P = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for t in range(len(maneethe)):
    area_N = cv2.contourArea(maneethe[t])
    #print(area_N)
    
    if area_N ==3524.0 :
      (x, y, w, h) = cv2.boundingRect(maneethe[t])
      cv2.rectangle(orangimg, (x, y-2), (x+w, y+h), (255, 255, 255), -1)
      MarkW = numpy.where(orangimg== 255)

    if area_N == 3364.5:
      (x, y, w, h) = cv2.boundingRect(maneethe[t])
      cv2.rectangle(orangimg1, (x-5, y-2), (x+w+5, y+h+3), (255, 255, 255), -1)
      MarkW1 = numpy.where(orangimg1== 255)
      
bgimg[MarkW[0]-150,MarkW[1]-370] = img2[MarkW]
bgimg[MarkW1[0]-200,MarkW1[1]-370] = img2[MarkW1]

blueimg = numpy.zeros((700, 700), dtype=numpy.uint8)
blueimg1 = numpy.zeros((700, 700), dtype=numpy.uint8)
blueimg2 = numpy.zeros((700, 700), dtype=numpy.uint8)
blueimg3 = numpy.zeros((700, 700), dtype=numpy.uint8)
maneethe1, hierarchy_P = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for t in range(len(maneethe1)):
    area_N1 = cv2.contourArea(maneethe1[t])
    #print(area_N1)
   
    if area_N1 == 543.0:
     (x, y, w, h) = cv2.boundingRect(maneethe1[t])
     cv2.rectangle(blueimg, (x-5, y-5), (x+w+5, y+h+5), (255, 255, 255), -1)
     MarkW2 = numpy.where(blueimg== 255)

    if area_N1 == 438.5:
     (x, y, w, h) = cv2.boundingRect(maneethe1[t])
     cv2.rectangle(blueimg1, (x-5, y-5), (x+w+5, y+h+5), (255, 255, 255), -1)
     MarkW3 = numpy.where(blueimg1== 255)

    if area_N1 == 643.5:
     (x, y, w, h) = cv2.boundingRect(maneethe1[t])
     cv2.rectangle(blueimg2, (x-5, y-5), (x+w+5, y+h+5), (255, 255, 255), -1)
     MarkW4 = numpy.where(blueimg2== 255)

    if area_N1 == 628.5:
     (x, y, w, h) = cv2.boundingRect(maneethe1[t])
     cv2.rectangle(blueimg3, (x-5, y-5), (x+w+5, y+h+5), (255, 255, 255), -1)
     MarkW5 = numpy.where(blueimg3== 255)
      
bgimg[MarkW2[0]-160,MarkW2[1]+180] = img2[MarkW2]
bgimg[MarkW3[0]-70,MarkW3[1]+180] = img2[MarkW3]
bgimg[MarkW4[0]-260,MarkW4[1]+235] = img2[MarkW4]
bgimg[MarkW5[0]-360,MarkW5[1]+230] = img2[MarkW5]

pinkimg = numpy.zeros((700, 700), dtype=numpy.uint8)
pinkimg1 = numpy.zeros((700, 700), dtype=numpy.uint8)
pinkimg2 = numpy.zeros((700, 700), dtype=numpy.uint8)
pinkimg3 = numpy.zeros((700, 700), dtype=numpy.uint8)
pinkimg4 = numpy.zeros((700, 700), dtype=numpy.uint8)
maneethe2, hierarchy_P = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for t in range(len(maneethe2)):
    area_N2 = cv2.contourArea(maneethe2[t])
    #print(area_N2)
   
    if area_N2 == 793.5:
     (x, y, w, h) = cv2.boundingRect(maneethe2[t])
     cv2.rectangle(pinkimg, (x-5, y-5), (x+w+5, y+h+5), (255, 255, 255), -1)
     MarkW6 = numpy.where(pinkimg== 255)
    
    if area_N2 == 789.5:
     (x, y, w, h) = cv2.boundingRect(maneethe2[t])
     cv2.rectangle(pinkimg1, (x-2, y-5), (x+w, y+h), (255, 255, 255), -1)
     MarkW7 = numpy.where(pinkimg1== 255)
    
    if area_N2 == 794.0:
     (x, y, w, h) = cv2.boundingRect(maneethe2[t])
     cv2.rectangle(pinkimg2, (x-5, y-5), (x+w+5, y+h+5), (255, 255, 255), -1)
     MarkW8 = numpy.where(pinkimg2== 255)

    if area_N2 == 892.5:
     (x, y, w, h) = cv2.boundingRect(maneethe2[t])
     cv2.rectangle(pinkimg3, (x-2, y-3), (x+w+1, y+h+4), (255, 255, 255), -1)
     MarkW9 = numpy.where(pinkimg3== 255)
     
    if area_N2 == 1084.0:
     (x, y, w, h) = cv2.boundingRect(maneethe2[t])
     cv2.rectangle(pinkimg4, (x-5, y-5), (x+w+5, y+h+5), (255, 255, 255), -1)
     MarkW10 = numpy.where(pinkimg4== 255)

bgimg[MarkW6[0],MarkW6[1]-15] = img2[MarkW6]
bgimg[MarkW7[0]-225,MarkW7[1]-255] = img2[MarkW7]
bgimg[MarkW8[0]-65,MarkW8[1]-123] = img2[MarkW8]
bgimg[MarkW9[0]-295,MarkW9[1]-215] = img2[MarkW9]
bgimg[MarkW10[0]-340,MarkW10[1]+95] = img2[MarkW10]

creamimg = numpy.zeros((700, 700), dtype=numpy.uint8)
creamimg1 = numpy.zeros((700, 700), dtype=numpy.uint8)
creamimg2 = numpy.zeros((700, 700), dtype=numpy.uint8)
maneethe3, hierarchy_P = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for t in range(len(maneethe3)):
    area_N3 = cv2.contourArea(maneethe3[t])
    #print(area_N3)
   
    if area_N3 == 1253.0:
     (x, y, w, h) = cv2.boundingRect(maneethe3[t])
     cv2.rectangle(creamimg, (x-5, y-5), (x+w+5, y+h+5), (255, 255, 255), -1)
     MarkW11 = numpy.where(creamimg== 255)

    if area_N3 == 1393.0:
     (x, y, w, h) = cv2.boundingRect(maneethe3[t])
     cv2.rectangle(creamimg1, (x-5, y), (x+w, y+h+3), (255, 255, 255), -1)
     MarkW12 = numpy.where(creamimg1== 255)
    
    if area_N3 == 882.5:
     (x, y, w, h) = cv2.boundingRect(maneethe3[t])
     cv2.rectangle(creamimg2, (x-5, y-5), (x+w+5, y+h+5), (255, 255, 255), -1)
     MarkW13 = numpy.where(creamimg2== 255)


bgimg[MarkW11[0]+25,MarkW11[1]+190] = img2[MarkW11]
bgimg[MarkW12[0]-115,MarkW12[1]-40] = img2[MarkW12]
bgimg[MarkW13[0]-194,MarkW13[1]-88] = img2[MarkW13]

blackimg = numpy.zeros((700, 700), dtype=numpy.uint8)
blackimg1 = numpy.zeros((700, 700), dtype=numpy.uint8)
blackimg2 = numpy.zeros((700, 700), dtype=numpy.uint8)
maneethe4, hierarchy_P = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for t in range(len(maneethe4)):
    area_N4 = cv2.contourArea(maneethe4[t])
    print(area_N4)
    
    if area_N4 == 1831.5:
     (x, y, w, h) = cv2.boundingRect(maneethe4[t])
     cv2.rectangle(blackimg, (x, y-5), (x+w+2, y+h+2), (255, 255, 255), -1)
     MarkW14 = numpy.where(blackimg== 255)
    
    if area_N4 == 1654.5:
     (x, y, w, h) = cv2.boundingRect(maneethe4[t])
     cv2.rectangle(blackimg1, (x-5, y-5), (x+w+5, y+h+5), (255, 255, 255), -1)
     MarkW15 = numpy.where(blackimg1== 255)

    if area_N4 == 1604.0:
     (x, y, w, h) = cv2.boundingRect(maneethe4[t])
     cv2.rectangle(blackimg2, (x, y-2), (x+w, y+h-2), (255, 255, 255), -1)
     MarkW16 = numpy.where(blackimg2== 255)
     

bgimg[MarkW14[0],MarkW14[1]-190] = img2[MarkW14]
bgimg[MarkW15[0]-60,MarkW15[1]+30] = img2[MarkW15]
bgimg[MarkW16[0]+130,MarkW16[1]-150] = img2[MarkW16]

cv2.rectangle(bgimg,(50,50),(250,140),(100,100,255),3)
cv2.rectangle(bgimg,(550,50),(300,140),(100,100,255),3)
cv2.rectangle(bgimg,(50,180),(280,270),(100,100,255),3)
cv2.rectangle(bgimg,(320,180),(500,270),(100,100,255),3)
cv2.rectangle(bgimg,(50,315),(280,410),(100,100,255),3)

fonts = [cv2.FONT_HERSHEY_TRIPLEX]
cv2.putText(bgimg,'Med1 : 2 tablet',(50,40), fonts[0], 0.7,(0,0,0),1)
cv2.putText(bgimg,'Med2 : 4 tablet',(300,40), fonts[0], 0.7,(0,0,0),1)
cv2.putText(bgimg,'Med3 : 5 tablet',(50,170), fonts[0], 0.7,(0,0,0),1)
cv2.putText(bgimg,'Med4 : 3 tablet',(315,170), fonts[0], 0.7,(0,0,0),1)
cv2.putText(bgimg,'Med5 : 3 tablet',(50,300), fonts[0], 0.7,(0,0,0),1)

cv2.imshow("aa",bgimg)
#cv2.imshow("std",img)
#cv2.imshow("img",bgimg)
#cv2.imshow("orage",img2)
#cv2.imshow("blue",img2)
#cv2.imshow("pink",img2)
#cv2.imshow("cream",img2)
#cv2.imshow("black",img2)
#cv2.imshow("Mask",mask)
#cv2.imshow("Mask1",mask1)
#cv2.imshow("Mask2",mask2)
#cv2.imshow("Mask3",mask3)
#cv2.imshow("Mask4",mask4)
#cv2.imshow("Result",result)
#cv2.imshow("Result1",result1)
#cv2.imshow("Result2",result2)
#cv2.imshow("Result3",result3)
#cv2.imshow("Result4",result4)

cv2.waitKey(0)
cv2.destroyAllWindows()









    
