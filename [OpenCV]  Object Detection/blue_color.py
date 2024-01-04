import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    if cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.resize(frame,(400,400))
        
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
        lower_bound = np.array([82,44,11])
        upper_bound = np.array([190,105,130])

        mask = cv2.inRange(hsv,lower_bound,upper_bound)
        
        res = cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow('org_winname',frame)
        cv2.imshow('mask_winname',mask)
        cv2.imshow('res_winname',res)
        
        key = cv2.waitKey(25)
        if key==27:
            break
cv2.destroyAllWindows()