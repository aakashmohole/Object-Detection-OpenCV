import cv2
import numpy as np

img = cv2.imread("D:\\OpenCV\\[P6] ObjectDetectionLiveVideo\\color_balls.jpg")

# creat null fun
def nothing():
    pass

cv2.namedWindow('color adjustment')

# creat trackbars for lower and upper ranges of color
cv2.createTrackbar('Lower_h','color adjustment',0,255,nothing)
cv2.createTrackbar('Lower_s','color adjustment',0,255,nothing)
cv2.createTrackbar('Lower_v','color adjustment',0,255,nothing)

cv2.createTrackbar('upper_h','color adjustment',255,255,nothing)
cv2.createTrackbar('upper_s','color adjustment',255,255,nothing)
cv2.createTrackbar('upper_v','color adjustment',255,255,nothing)


while True:
    # get hsv values of img
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)   

    # get pos of trackbars 
    lower_h = cv2.getTrackbarPos('Lower_h','color adjustment')
    lower_s = cv2.getTrackbarPos('Lower_s','color adjustment')
    lower_v = cv2.getTrackbarPos('Lower_v','color adjustment')
    
    upper_h = cv2.getTrackbarPos('upper_h','color adjustment')
    upper_s = cv2.getTrackbarPos('upper_s','color adjustment')
    upper_v = cv2.getTrackbarPos('upper_v','color adjustment')
    
    # get upper and lower bound of single color and crete array
    lower_bound = np.array([lower_h,lower_s,lower_v])
    upper_bound = np.array([upper_h,upper_s,upper_v])
    
    # create mask img of this color
    mask = cv2.inRange(hsv,lower_bound,upper_bound)
    
    # filtering mask with img
    res = cv2.bitwise_and(img,img,mask=mask)
    
    cv2.imshow('org wind',img)
    cv2.imshow('mask wind',mask)
    cv2.imshow('res wind',res)
    
    key = cv2.waitKey(1)
    if key==27:
        break
cv2.destroyAllWindows()

