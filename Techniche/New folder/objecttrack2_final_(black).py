import numpy as np
import cv2 

video = cv2.VideoCapture(0)
while True:
    
    
    ret, orig_frame = video.read()
    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_black = np.array([0,0,0])
    up_black = np.array([180, 255, 30])
    mask = cv2.inRange(hsv, low_black, up_black)
    edges = cv2.Canny(mask, 10, 150)
 
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
 
    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)
 
    key = cv2.waitKey(25)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()
