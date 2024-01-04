import cv2
import numpy as np

img = cv2.imread("D:\\OpenCV\\[P6] ObjectDetectionLiveVideo\\color_balls.jpg")

while True:
        
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        upper_val = np.array([48,255,248])
        lower_val = np.array([20,143,139])
        
        # creating mask
        mask = cv2.inRange(hsv,lower_val,upper_val)
        
        # creating mask
        res = cv2.bitwise_and(img,img,mask=mask)

        cv2.imshow('org img',img)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        
        key = cv2.waitKey(1)
        if key == 27:
            break

cv2.destroyAllWindows()