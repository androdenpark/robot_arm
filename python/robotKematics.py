from __future__ import division
import numpy 
from math import *
from common import *


__PointDistanceTonarance__=5

class RobotKinematics:
    def __init__(self, robotPara):
        self.aValue=robotPara[0]
        self.bValue=robotPara[1]
        self.cValue=robotPara[2]
        self.L1Value=robotPara[3]
        self.L2Value=robotPara[4]
        self.L3Value=robotPara[5]

    def angleTransWithin2Pi(self, theNum):       
        if theNum is not None:
            theNum[0,0]=divmod(theNum[0,0],2*PI_VALUE)[1]
            theNum[0,1]=divmod(theNum[0,1],2*PI_VALUE)[1]
        return theNum

    def constrain(self, theNum):
        return theNum if abs(theNum)<=1 else None

    def calculateFunction(self, Para1, Para2, Para3):
        try:
            #Para1*sin(x)+Para2*cos(x)=Para3
            para1Arientation=theNumSign(Para1)
            para2Arientation=theNumSign(Para2)
            #make sure the serTa value is always between 0~pi/2  
            serTa=acos(self.constrain((para2Arientation*Para2/((Para1**2+Para2**2)**(0.5)))))
            # the acos value is always between 0~`pi 
            equtionAsu=acos(self.constrain((para2Arientation*Para3)/((Para1**2+Para2**2)**(0.5))))

            baseAus=equtionAsu+(para2Arientation*para1Arientation)*serTa;
            anotherAus=2*PI_VALUE-equtionAsu+(para2Arientation*para1Arientation)*serTa

            return numpy.array([baseAus+2*PI_VALUE, anotherAus+2*PI_VALUE]).reshape(1,2)
        except:
            return None


    def solvePointByAngle(self, theAngles):
        a=self.aValue
        b=self.bValue
        c=self.cValue
        L1=self.L1Value
        L2=self.L2Value
        L3=self.L3Value
        #print __AngleTrans__*numpy.array(theAngles)
        COSX=cos(theAngles[0])
        SINX=sin(theAngles[0])
        COSY=cos(theAngles[1])
        SINY=sin(theAngles[1])
        COSZ=cos(theAngles[2])
        SINZ=sin(theAngles[2])
        #print SINZ
        x=b*(COSX*COSY*SINZ + COSX*COSZ*SINY) - a*(COSX*SINY*SINZ - COSX*COSY*COSZ) + L1*COSX - c*SINX + L2*COSX*COSY + L3*COSX*COSY*COSZ - L3*COSX*SINY*SINZ
        y=a*(COSY*COSZ*SINX - SINX*SINY*SINZ) + b*(COSY*SINX*SINZ + COSZ*SINX*SINY) + L1*SINX + c*COSX + L2*COSY*SINX + L3*COSY*COSZ*SINX - L3*SINX*SINY*SINZ
        z=b*(COSY*COSZ - SINY*SINZ) - a*(COSY*SINZ + COSZ*SINY) - L2*SINY - L3*COSY*SINZ - L3*COSZ*SINY        
        return [x,y,z]


    def filterAngles(self, thePointList, comparedPoint,pointDistanceTonarance=__PointDistanceTonarance__):
        for index,value in enumerate(thePointList):
            if type(value) == type([]):
                calPoint=self.solvePointByAngle(value)
                deltaDistance=abs(calPoint[0]-comparedPoint[0])+abs(calPoint[1]-comparedPoint[1])+abs(calPoint[2]-comparedPoint[2])
                #print deltaDistance
                if deltaDistance > pointDistanceTonarance:
                    thePointList[index]=False
        return thePointList
                


    def solveAngleByPoint(self, thePoint):
        #the output maybe [False,None,None,False,[1,2,4]] or None,only the [1,2,4] is ocrrect Angle
        #print thePoint
        a=self.aValue
        b=self.bValue
        c=self.cValue
        L1=self.L1Value
        L2=self.L2Value
        L3=self.L3Value
        Px=thePoint[0]
        Py=thePoint[1]
        Pz=thePoint[2]
        Para1=-Px
        Para2=Py
        Para3=self.cValue
        #returnAngleList=[None]*8
        returnAngleList=[]

        xValue=self.angleTransWithin2Pi(self.calculateFunction(Para1,Para2,Para3))
        #print xValue
        if xValue is None:
            print returnAngleList, thePoint
            return None

        XSIN=numpy.sin(xValue)
        XCOS=numpy.cos(xValue)
        CONS=(L3**2+ a**2+ b**2+ 2*L3*a-(L1**2 + Pz**2 + L2**2+ Px**2))*numpy.ones((1,2))/2
        #print XSIN,XCOS,CONS
        Para1=(L2*Pz)*numpy.ones((1,2))
        Para2=(L1*L2*numpy.ones((1,2)) - L2*Px*XCOS- L2*Py*XSIN)
        Para3=CONS+ L1*Px*XCOS+ L1*Py*XSIN - Px*Py*XCOS*XSIN
        #print Para1,Para2,Para3
        yValue_1=self.angleTransWithin2Pi(self.calculateFunction(Para1[0,0],Para2[0,0],Para3[0,0]))
        yValue_2=self.angleTransWithin2Pi(self.calculateFunction(Para1[0,1],Para2[0,1],Para3[0,1]))
        #print yValue_1,yValue_2

        if yValue_1 is not None and yValue_2 is not None:
            yValueSize=2
            yValue=numpy.vstack((yValue_1,yValue_2))
            CoXCOS=numpy.array([XCOS[0,0],XCOS[0,0],XCOS[0,1],XCOS[0,1]]).reshape(2,2)
            CoXSIN=numpy.array([XSIN[0,0],XSIN[0,0],XSIN[0,1],XSIN[0,1]]).reshape(2,2)
        elif yValue_1 is not None:
            yValueSize=1
            yValue=yValue_1
            CoXCOS= numpy.array([XCOS[0,0],XCOS[0,0]]).reshape(1,2)
            CoXSIN= numpy.array([XSIN[0,0],XSIN[0,0]]).reshape(1,2)
        elif yValue_2 is not None:
            yValueSize=1
            yValue=yValue_2
            CoXCOS= numpy.array([XCOS[0,1],XCOS[0,1]]).reshape(1,2)
            CoXSIN= numpy.array([XSIN[0,1],XSIN[0,1]]).reshape(1,2)
        else:
            print returnAngleList, thePoint
            return None
            
        YSIN=numpy.sin(yValue)
        YCOS=numpy.cos(yValue)
        #print YSIN,YCOS

        Para1=b*numpy.ones(yValue.shape)
        Para2=(L3+a)*numpy.ones(yValue.shape)            
        Para3=YCOS*(Px*CoXCOS - L1*numpy.ones(yValue.shape) + Py*CoXSIN) - Pz*YSIN - L2*numpy.ones(yValue.shape)      
        #print Para1,Para2,Para3
        solvedAngles={}


        zValue_1=self.angleTransWithin2Pi((self.calculateFunction(Para1[0,0],Para2[0,0],Para3[0,0])))
        if zValue_1 is not None:
            returnAngleList.append([xValue[0,0],yValue[0,0],zValue_1[0,0]])
            returnAngleList.append([xValue[0,0],yValue[0,0],zValue_1[0,1]])
                            
        zValue_2=self.angleTransWithin2Pi((self.calculateFunction(Para1[0,1],Para2[0,1],Para3[0,1])))
        if zValue_2 is not None:
            returnAngleList.append([xValue[0,0],yValue[0,1],zValue_2[0,0]])
            returnAngleList.append([xValue[0,0],yValue[0,1],zValue_2[0,1]])
                                
        if  yValueSize > 1 :       
            zValue_3=self.angleTransWithin2Pi((self.calculateFunction(Para1[1,0],Para2[1,0],Para3[1,0])))
            if zValue_3 is not None:
                returnAngleList.append([xValue[0,1],yValue[1,0],zValue_3[0,0]])
                returnAngleList.append([xValue[0,1],yValue[1,0],zValue_3[0,1]])
                
            zValue_4=self.angleTransWithin2Pi((self.calculateFunction(Para1[1,1],Para2[1,1],Para3[1,1])))
            if zValue_4 is not None:
                returnAngleList.append([xValue[0,1],yValue[1,1],zValue_4[0,0]])
                returnAngleList.append([xValue[0,1],yValue[1,1],zValue_4[0,1]])

        #print returnAngleList
        returnAngleList=self.filterAngles(returnAngleList,thePoint)

        try:
            if sum(returnAngleList)== False:
                print returnAngleList, thePoint
        except:
            pass

        return returnAngleList




if __name__=="__main__":
    obotKinematics=RobotKinematics([125,55,15,15,92,87])
    print obotKinematics.solveAngleByPoint([ -209.4034 , 15.0000 , 206.7224])






    
