import cv2
import numpy as np

#capturing video through webcam
cap=cv2.VideoCapture(0)

while(1):
       _, img = cap.read()

       #converting it to BGR to HSV

       hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

       #definig the range of red color
       red_lower=np.array([166, 84, 141],np.uint8)
       red_upper=np.array([186,255,255],np.uint8)

       #defining the Range of Blue color
       blue_lower=np.array([97, 100, 117],np.uint8)
       blue_upper=np.array([117, 255, 255],np.uint8)

       #finding the range of red color int the image
       red=cv2.inRange(hsv, red_lower, red_upper)
       blue=cv2.inRange(hsv,blue_lower,blue_upper)


       kernal = np.ones((5 ,5), "uint8")
       red=cv2.dilate(red, kernal)
       res=cv2.bitwise_and(img, img, mask = red)

       blue=cv2.dilate(blue,kernal)
       res1=cv2.bitwise_and(img, img, mask = blue)

       (_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

       for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area>300:
                x,y,w,h = cv2.boundingRect(contour)
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(img,"RED color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))
                (_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

       for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area>300:
                x,y,w,h = cv2.boundingRect(contour)
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                cv2.putText(img,"Blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0,(255,0,0))


       cv2.imshow("Redcolour",red)
       cv2.imshow("let's",img)
       cv2.imshow("red",res)
       if cv2.waitKey(10) & 0xFF == ord('q'):
           cap.release()
           cv2.destroyAllWindows()
           break
