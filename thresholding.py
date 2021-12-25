import numpy as np
import cv2

img1 = cv2.imread('book.jpeg' , 1)

ret,threshold = cv2.threshold(img1 , 150 , 255 , cv2.THRESH_BINARY) #low-light image, anything above 12 = white

img1_gray = cv2.cvtColor(img1 , cv2.COLOR_BGR2GRAY)

ret2,threshold2 = cv2.threshold(img1_gray , 120 , 255 , cv2.THRESH_BINARY) #low-light image, anything above 12 = white

print("Yo, in branch main")

cv2.imshow('ORIGINAL' , img1)

cv2.imshow('THRESHOLDED' , threshold)

cv2.imshow('THRESHOLDED2' , threshold2)






cv2.waitKey(0)
cv2.destroyAllWindows()

