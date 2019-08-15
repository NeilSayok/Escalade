import colorsys
import cv2
import imutils
import numpy as np

img = cv2.imread("im2.jpeg")

img = imutils.resize(img, width=500, height=500)

blurred = cv2.GaussianBlur(img, (11, 11), 0)
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
kernel = np.ones((5, 5), np.uint8)

mask = cv2.inRange(hsv, (0.12048192771084337, 0.9707602339181286, 171), (0.14388489208633093, 0.5604838709677419, 248))
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

cv2.imshow("img", img)
cv2.imshow("img1", mask)

cv2.waitKey(0)

r = colorsys.rgb_to_hsv(213, 0, 0)

print(r)
