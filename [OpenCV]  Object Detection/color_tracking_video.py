import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing():
    pass

cv2.namedWindow('color_adj')

# create track bars for upper and lower values of colors
cv2.createTrackbar('lower_h','color_adj',0,255,nothing)
cv2.createTrackbar('lower_s','color_adj',0,255,nothing)
cv2.createTrackbar('lower_v','color_adj',0,255,nothing)

cv2.createTrackbar('upper_h','color_adj',255,255,nothing)
cv2.createTrackbar('upper_s','color_adj',255,255,nothing)
cv2.createTrackbar('upper_v','color_adj',255,255,nothing)

while True:
    if cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.resize(frame,(400,400))
        
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
        lower_h = cv2.getTrackbarPos('lower_h','color_adj')
        lower_s = cv2.getTrackbarPos('lower_s','color_adj')
        lower_v = cv2.getTrackbarPos('lower_v','color_adj')
        
        upper_h = cv2.getTrackbarPos('upper_h','color_adj')
        upper_s = cv2.getTrackbarPos('upper_s','color_adj')
        upper_v = cv2.getTrackbarPos('upper_v','color_adj')
        
        lower_bound = np.array([lower_h,lower_s,lower_v])
        upper_bound = np.array([upper_h,upper_s,upper_v])

        mask = cv2.inRange(hsv,lower_bound,upper_bound)
        
        res = cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow('org_winname',frame)
        cv2.imshow('mask_winname',mask)
        cv2.imshow('res_winname',res)
        
        key = cv2.waitKey(25)
        if key==27:
            break
cv2.destroyAllWindows()