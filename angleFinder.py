from typing import Tuple
import cv2
import math

path = "test.jpg"
img = cv2.imread(path)
points = [] # Store coordinates of points in 2D-list

def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        numberOfPoints = len(points)
        if numberOfPoints != 0 and numberOfPoints % 3 != 0:
            if numberOfPoints % 3 == 1:
                cv2.line(img, tuple(points[-1]), (x, y), (0,0,255), 2) # Draw line from first to second point
            if numberOfPoints % 3 == 2:
                cv2.line(img, tuple(points[-2]), (x, y), (0,0,255), 2) # Draw line from first to third point
                
        cv2.circle(img, (x, y), 3, (0,0,255), cv2.FILLED) # Draw points
        points.append([x, y])
        
    
def gradient(p1, p2) -> int:
    # p = [x, y]
    return (p2[1] - p1[1])/(p2[0] - p1[0])
    
        
def getAngle(points: list) -> Tuple[int, list]:
    p1, p2, p3 = points[-3:] # get last three points
    k1 = gradient(p1, p2)
    k2 = gradient(p1, p3)
    angRad = math.atan(abs((k2 - k1)/(1 + k1*k2)))
    angDeg = round(math.degrees(angRad))
    return angDeg, p1

while True:
    
    if len(points) % 3 == 0 and len(points) != 0:
        ang, p1 = getAngle(points)
        cv2.putText(img, str(ang), (p1[0]-40, p1[1]-20), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)
    
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mousePoints)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        points = [] # Clear points if user types q
        img = cv2.imread(path)
        
    # Close window when clicking 'X'
    if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()
        
