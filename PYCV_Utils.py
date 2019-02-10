import numpy
import math
import cv2

cameraAngle = 60.0
redText = cv2.Scalar(0,500,500)

def distance(pointOne, pointTwo):
    distance = Math.sqrt((pointOne.x-pointTwo.x)**2 + (pointOne.y-pointTwo.y)**2)
    return distance

def center(rectangle):
    midpoint = cv22.Point((rectangle.pt1.x + rectangle.pt2.x)/2,(rectangle.pt1.y + rectangle.pt2.y)/2)
    return midpoint

def side(matrix, rectangle):
    midpoint = midPoint(rectangle)
    TOLERANCE = 100
    if midpoint.x <= matrix.width()/2 + TOLERANCE and midpoint.x >= mat.width()/2 - TOLERANCE:
        print("Your thing is on the line")
    elif midpoint.x < mat.width()/2:
        print("Your thing is on the right of the line")
    else:
        print("Your thing is on the left")

def setLabel(matrix, string, xPos, yPos):
    cv2.Imgproc.putText(matrix, string, cv2.Point(x,y), Core.FONT_HERSHEY_PLAIN,1,  redText)

def putLine(matrix):
    cv2.Imgproc.line(matrix, cv2.Point(matrix.width()/2,0), cv2.Point(matrix.width()/2,0),redText)

def putRect(matrix, rectangle):
    cv2.Imgproc.rectangle(matrix, rectangle.tl(), rectangle.br(), redText)

def midPoint(rectangle):
    return cv2.Point((rectangle.tl().x + rectangle.br().x)/2),(rectangle.tl().y + rectangle.br().y)/2)

def resolution(matrix):
    return str("width " + mat.width() + " height " + mat.height())

# putLine()
#Distance, Midpoint, Side, PutLine, putRect, SetLabel, Res
