import cv2

cap = cv2.VideoCapture(0)

blue = [255, 0, 0]
green = [0, 255, 0]
red = [0.0, 255]

while True:
    key = cv2.waitKey(1) & 0xFF
    _, frame = cap.read()

    for j in frame:
        for i in range(0,len(frame)):
            k = max(j[i])
            #print(k)
            if k == j[i][0]:
                j[i]=blue
            elif k == j[i][1]:
                j[i] = green
            else:
                j[i] = red
    print(frame)
    cv2.imshow('win', frame)

    #print(len(frame))
    if key == ord("q"):
        break


cv2.destroyAllWindows()

cap.release()
