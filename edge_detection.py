import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	#ret , frame = cap.read()
 	#gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
  	gray = cv2.imread('gauss.png' , 1)

	
	laplacian = cv2.Laplacian(gray, cv2.CV_64F)
	
	sobelx = cv2.Sobel(gray, cv2.CV_64F , 1,0,ksize = 5) #order of derivative in x,y = (1,0)
	sobely = cv2.Sobel(gray, cv2.CV_64F , 0,1,ksize = 5) 
	
	edges_canny_one = cv2.Canny(gray , 100 , 200)  #upper_threshold,lower_threshold = 100,200
		
	edges_canny_two = cv2.Canny(gray , 50 , 50)

	#cv2.imshow('ORIGINAL' , frame)
	#cv2.imshow('GRAY' , gray)
	#cv2.imshow('LAPLACIAN' , laplacian)
	cv2.imshow('SOBEL_X' , sobelx)
	cv2.imshow('SOBL_Y' , sobely)
	cv2.imshow('CANNY_ONE' , edges_canny_one)
	cv2.imshow('CANNY_TWO' , edges_canny_two)
	if cv2.waitKey(1) & 0xFF == ord('q'):

		break


cv2.waitKey(0)
cv2.destroyAllWindows()
