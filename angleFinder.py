import cv2
import math

path = "test.jpg"
img = cv2.imread(path)
points = [] # Store coordinates of points in 2D-list

def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 5, (0,0,255), cv2.FILLED)
        points.append([x, y])
        print(points)

while True:
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mousePoints)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        points = [] # Clear points if user types q
        img = cv2.imread(path)
