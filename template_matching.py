import cv2
import numpy as np

img = cv2.imread('raspi_board.jpg' , 1)
img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
template = cv2.imread('cropped_raspi.jpg' ,0)

count = 0


#img = cv2.imread('pond_algae.jpg' , 1)
#img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
#template = cv2.imread('algae.jpg',0)

#img = cv2.imread('alphabet.jpg' , 1)
#img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
#template = cv2.imread('d.png' ,0)

w,h = template.shape[::-1]
w_m , h_m = img_gray.shape[::-1]

#print "%d %d" %(w_m , h_m) 
#print "%d %d" %(w , h) 


res = cv2.matchTemplate(img_gray , template , cv2.TM_CCOEFF_NORMED)
print(len(res))
print("########################")

threshold = 0.7
loc = np.where(res>= threshold)
#print(loc.shape[1])

print(loc)

img1 = cv2.imread('img_ft_one.jpg',0)
template = cv2.imread('temp_ft_one.jpg' , 0)

#cv2.line(img , (0,0) , (805,156) , (200,0,0) , 4)
#cv2.line(img , (0,0) , (968,402) , (200,0,0) , 4) #for threshold 0.85

#cv2.line(img , (0,0) , (805,155) , (200,0,0) , 4)
#cv2.line(img , (0,0) , (804,156) , (200,0,0) , 4)
#cv2.line(img , (0,0) , (806,156) , (200,0,0) , 4)
#cv2.line(img , (0,0) , (805,157) , (200,0,0) , 4)
#cv2.line(img , (0,0) , (584,484) , (200,0,0) , 4) #for threshold 0.85
#cv2.line(img , (0,0) , (690,445) , (200,0,0) , 4) #for threshold 0.85


for pt in zip(*loc[::-1]):
	cv2.rectangle(img , pt , (pt[0]+w , pt[1]+h)  , (0,0,255) , 2)
	count = count+1
	



print(count)
cv2.imshow('DETECTED' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
