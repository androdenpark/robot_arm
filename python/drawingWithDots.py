from ConvertAngle2Ardunio import *
from robotKematics import *
from serialCommunication import  *
from common import *
from movingOnLine import *
from serialAngleMessage import *

import traceback

__movingStep__=5
__angleWeight__=[3,2,1]



class DrawingWithDots:
    def __init__(self, robotKi,angle2Ardunio,serialObj,intialPostionAngle):
        self.movingObj=MovingOnLine(robotKi,angle2Ardunio,__angleWeight__)
        self.serial=serialObj
        self.currentAngle=intialPostionAngle

    def transDots2Angles(self, dotList):
        angleList=[]
        #lastAngle=startAngle
        lastAngle=self.currentAngle
        for index,dot in enumerate(dotList[0:-1]):
            startPoint=dot
            endPoint=dotList[index+1]
            anglesGet=self.movingObj.calculatePointsOnLine(startPoint,endPoint,lastAngle,__movingStep__)
            try:
                lastAngle=anglesGet[-1]["angle"]# the anglesGet may be empty
                angleList += anglesGet
            except:
                pass
        self.currentAngle=lastAngle
        return angleList


    def startDrawing(self, angleList):
        messageToSend=[]
        serialAngleM=SerialAngleMessage(self.serial)
        for value in angleList:
            pointBase=value["angle"][0]*PI2ANGLE_FACTOR
            pintShoulder=value["angle"][1]*PI2ANGLE_FACTOR
            pintEmbow=value["angle"][2]*PI2ANGLE_FACTOR
            #print pointBase,pintShoulder,pintEmbow
            messageToSend.append([pointBase,pintShoulder,pintEmbow])
        #print messageToSend
        return serialAngleM.sendLongMessage(messageToSend),angleList[-1]["Corrd"]

    def draw(self, dotList):
        try:            
            return self.startDrawing(self.transDots2Angles(dotList))
        except Exception as e:
            print e
            traceback.print_exc()  
            return False,None
            
            
            
