from __future__ import division
import numpy 
from math import *
from common import *




class MovingOnLine:
    def __init__(self, robotKinematicsObj, convert2AudunioObj,angleWeightList):
        self.robotKinematics=robotKinematicsObj
        self.convert2Audunio=convert2AudunioObj
        self.pointsOnline=[]
        self.baseAngleWeight=angleWeightList[0]
        self.shoulderAngleWeight=angleWeightList[1]
        self.embowAngleWeight=angleWeightList[2]


    def lineDevision2Points(self, point1, point2, divideStep):
    #####Input#####point1,point2 format:[11,12,13] as a list
    #####Output#####can be [] or [[11,12,13]]
        deltaList=[(point2[0]-point1[0]),(point2[1]-point1[1]),(point2[2]-point1[2])]
        distance=((deltaList[0])**2+(deltaList[1])**2+(deltaList[2])**2)**(0.5)
        if distance < 1:
            return []
        segmentsNum=int(distance//divideStep)
        selcetedBase=numpy.abs(deltaList).tolist().index(max(numpy.abs(deltaList)))
        movingTimes=segmentsNum+1
        movingStep=abs(deltaList[selcetedBase])/movingTimes
        #returnPointsList=[None]*(segmentsNum+1)
        returnPointsList=[]
        for times in range(1, movingTimes+1):
            pointKnown=point1[selcetedBase] + times*movingStep*theNumSign(deltaList[selcetedBase])
            coefficients=(pointKnown-point1[selcetedBase])/deltaList[selcetedBase]
            answerX=deltaList[0]*coefficients+point1[0]
            answerY=deltaList[1]*coefficients+point1[1]
            answerZ=deltaList[2]*coefficients+point1[2]
            returnPointsList.append([answerX, answerY, answerZ])
        #returnPointsList.append(point2)
        return returnPointsList


    def calculatePointsOnLine(self,point1, point2, startAngle, divisionStep):
        #print "calculatePointsOnLine"
        self.pointsOnline=[]
        angleforCompare=startAngle
        pointsOnLine=self.lineDevision2Points(point1, point2 ,divisionStep)
        #print pointsOnLine
        for onePoint in pointsOnLine:
            #print onePoint
            anglesofPoint=self.robotKinematics.solveAngleByPoint(onePoint)
            if anglesofPoint is None:
                continue
            #print anglesofPoint
            anglesofPoint=self.convert2ArdunioAngle(anglesofPoint)
            #print anglesofPoint
            seletedAngle=self.filterAngle(angleforCompare, anglesofPoint)
            #print seletedAngle
            if seletedAngle is not None:
                self.savePointInfo(onePoint,seletedAngle)
                angleforCompare=seletedAngle
                #print angleforCompare,seletedAngle
        return self.pointsOnline
                                          

    def convert2ArdunioAngle(self, theAnglesList):
        for index,angle in enumerate(theAnglesList):
            if type(angle) == type([]):
                convertedAngle=self.convert2Audunio.covert2ArdunioAngle(angle)
                theAnglesList[index]=convertedAngle
        return theAnglesList
                
        
    def filterAngle(self, camparedAngle, theAngleList):
        deltaAngle=10000
        returnAngle=None
        for value in theAngleList:
            if type(value) == type([]):
                currentDelta=self.angleDelta(camparedAngle, value)
                if  currentDelta < deltaAngle:
                    deltaAngle=currentDelta
                    returnAngle=value
        return returnAngle
        


    def angleDelta(self, angleOne, angleTwo):
        xAngleDelta=self.angleDistance(angleOne[0],angleTwo[0])*self.baseAngleWeight
        yAngleDelta=self.angleDistance(angleOne[1],angleTwo[1])*self.shoulderAngleWeight
        zAngleDelta=self.angleDistance(angleOne[2],angleTwo[2])*self.embowAngleWeight
        return xAngleDelta +  yAngleDelta + zAngleDelta
            
        

    def angleDistance(self, angle1, angle2):
        ##############when the angle1 and angle2 values are within 0~360####################################
        deltaAngleleft= abs(angle1-angle2)
        deltaAngleright=abs(angle1+2*PI_VALUE-angle2)
        return deltaAngleleft if deltaAngleleft<deltaAngleright else deltaAngleright

    def savePointInfo(self, thePoint, theAngle):        
        self.pointsOnline.append(self.pointInfoFormat(thePoint, theAngle))

    def pointInfoFormat(self, thePoint, theAngle):
        pointInfo={}
        pointInfo["Corrd"]=thePoint
        pointInfo["angle"]=theAngle
        return pointInfo
        
        
        
    
