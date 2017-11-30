#!/usr/bin/env python
# encoding: utf-8
# Author: Feniox

import math

def Receive():
    '''Receive function.
       Receive two points' information.'''

    print("Please enter first point's information")
    X1 = int(input("Please input X number:"))
    Y1 = int(input("Please input Y number:"))
    print("Please enter second point's information")
    X2 = int(input("Please input X number:"))
    Y2 = int(input("Please input Y number:"))

    return (X1, Y1, X2, Y2)

def ReceivePoints():
    '''Receive function.
       Receive more than two points.
    '''
    PointBox = []
    Rank = ["first", "second", "third", "four", "five", "six"]
    for index in range(len(Rank)):
        print("Please enter {ind} point's information:".format(ind=Rank[index]))
        X = int(input("Please input X number:"))
        Y = int(input("Please input Y number:"))
        point = [X, Y]
        PointBox.append(point)
    else:
        print("Input Success!")

    return PointBox

def CalcDistance(cX1, cY1, cX2, cY2):
    '''CalcDistance function.
       cX1, cY1, cX2, cY2 are parameters.
       calculate two points's distance.
    '''
    distance = math.sqrt((cX1 - cX2)**2+(cY1 - cY2)**2)
    print("the distance between two points is {0}".format(distance))

    return None

def CmpDistanceOrigin(PointBox):
    '''CmpDistanceOrigin function.
       Calculate all points distance from origin.
       Then return max distance in these points.
    '''
    InfoBox = []
    for index in range(len(PointBox)):
        point = PointBox[index]
        (X,Y) = (point[0], point[1])
        Distance = math.sqrt(X**2 + Y**2)
        InfoBox.append([index, Distance])
    else:
        InfoBox.sort(key=lambda InfoBox:InfoBox[1], reverse=True)
    print("the {0} point have max distance that is {1}!".format(InfoBox[0][0]+1, InfoBox[0][1]))

    return None

def HandleData(PointBox):
    '''HandleData function.
       In this funtion, we can decide
       these points belone to which quadrant
       and calculate their radian.
    '''
    FirstQuadrant = []
    SecondQuadrant = []
    ThirdQuadrant = []
    FourthQuadrant = []
    InfoBox = []
    Quadrant = ["FirstQuadrant", "SecondQuadrant", "ThirdQuadrant", "FourthQuadrant"]
    for i in range(len(PointBox)):
        if PointBox[i][0] >= 0 and PointBox[i][1] >= 0:
            FirstQuadrant.append(PointBox[i])
            theta = math.atan2(PointBox[i][1], PointBox[i][0])
            InfoBox.append([PointBox[i], Quadrant[0], theta])

        elif PointBox[i][0] < 0 and PointBox[i][1] >= 0:
            SecondQuadrant.append(PointBox[i])
            theta = math.atan2(PointBox[i][1], PointBox[i][0])
            InfoBox.append([PointBox[i], Quadrant[1], theta])

        elif PointBox[i][0] <= 0 and PointBox[i][1] < 0:
            ThirdQuadrant.append(PointBox[i])
            theta = math.atan2(PointBox[i][1], PointBox[i][0])
            InfoBox.append([PointBox[i], Quadrant[2], theta])

        elif PointBox[i][0] > 0 and PointBox[i][1] < 0:
            FourthQuadrant.append(PointBox[i])
            theta = math.atan2(PointBox[i][1], PointBox[i][0])
            InfoBox.append([PointBox[i], Quadrant[3], theta])
    else:
        for index in range(len(InfoBox)):
            print("the {0} point {1} belones to {2} quadrant the radian is {3}"\
                  .format(index+1, InfoBox[index][0], InfoBox[index][1], InfoBox[index][2]))


if __name__ == "__main__":
    #point = Receive()
    #CalcDistance(*point)
    PointBox = ReceivePoints()
    CmpDistanceOrigin(PointBox)
    HandleData(PointBox)


