from __future__ import division
import numpy 
from math import *
from common import *

class ConvertAngle2Ardunio:
    def __init__(self,audunioInitialAngle, robotInitialAngle,oriatationPolarity,anglesRange):
        ##audunioInitialAngle is the angle given when  startup
        ##robotInitialAngle is the angle referring to base coords when  startup
        self.audunioInitialAngle=audunioInitialAngle
        self.robotInitialAngle =robotInitialAngle
        self.baseOriatationPolarity=oriatationPolarity[0]
        self.shoulderOriatationPolarity=oriatationPolarity[1]
        self.embowOriatationPolarity=oriatationPolarity[2]
        self.baseAngleRange=anglesRange[0]
        self.shoulderAngleRange=anglesRange[1]
        self.embowAngleRange=anglesRange[2]
    
    #################[0 -90 -10]######################################
    def isBaseAngleReachable(self, theAngle):
        return theAngle >=self.baseAngleRange[0] and theAngle <= self.baseAngleRange[1]

    def isShoulderAngleReachable(self, theAngle):
        return theAngle >=self.shoulderAngleRange[0] and theAngle <= self.shoulderAngleRange[1]

    def isEmbowAngleReachable(self, theAngle):
        return theAngle >=self.embowAngleRange[0] and theAngle <= self.embowAngleRange[1]

    def isAngleReachable(self, theAngles):
        return self.isBaseAngleReachable(theAngles[0]) and self.isShoulderAngleReachable(theAngles[1]) and self.isEmbowAngleReachable(theAngles[2])

    #################[0 -90 -10]######################################
    #################[90 90 90]######################################
    def change2AudoinaBaseAngle(self,theBaseAngle):
        deltaBaseAngle=self.audunioInitialAngle[0]-self.robotInitialAngle[0]+2*PI_VALUE
        return (divmod(theBaseAngle+deltaBaseAngle, 2*PI_VALUE)[1]-self.audunioInitialAngle[0])*self.baseOriatationPolarity+self.audunioInitialAngle[0]

    def change2AudoinaShoulderAngle(self,theShoulderAngle):
        deltaShoulderAngle=self.audunioInitialAngle[1]-self.robotInitialAngle[1]+2*PI_VALUE
        return (divmod(theShoulderAngle+deltaShoulderAngle, 2*PI_VALUE)[1]-self.audunioInitialAngle[1])*self.shoulderOriatationPolarity+self.audunioInitialAngle[1]

    def change2AudoinaEmbowAngle(self,theEmbowAngle):
        deltaEmbowAngle=self.audunioInitialAngle[2]-self.robotInitialAngle[2]+2*PI_VALUE
        #print deltaEmbowAngle
        #print divmod(theEmbowAngle+deltaEmbowAngle, 2*PI_VALUE)[1]
        #print (divmod(theEmbowAngle+deltaEmbowAngle, 2*PI_VALUE)[1]-self.audunioInitialAngle[2])
        #print self.embowOriatationPolarity,self.audunioInitialAngle[2]
        return (divmod(theEmbowAngle+deltaEmbowAngle, 2*PI_VALUE)[1]-self.audunioInitialAngle[2])*self.embowOriatationPolarity+self.audunioInitialAngle[2]
            
    def change2AudoinaAngles(self, theAngles):
        audoinaBase=self.change2AudoinaBaseAngle(theAngles[0])
        audoinaShoulder=self.change2AudoinaShoulderAngle(theAngles[1])
        audoinaEmbow=self.change2AudoinaEmbowAngle(theAngles[2])       
        return [audoinaBase,audoinaShoulder,audoinaEmbow]
    ###################################################################



    def covert2ArdunioAngle(self,theAngles):
        #print "covert2ArdunioAngle"
        #print theAngles
        theConverted=self.change2AudoinaAngles(theAngles)
        #print theConverted
        if self.isAngleReachable(theConverted):           
            return theConverted
        else:
            None



        


if __name__=="__main__":
    __RobotInitialAngle__=[0,270*ANGLE2PI_FACTOR,355*ANGLE2PI_FACTOR] #cooresponding to angles(pi/2 pi/2 pi/2)
    __ArdunioInitialAngle__=[90*ANGLE2PI_FACTOR,90*ANGLE2PI_FACTOR,90*ANGLE2PI_FACTOR]
    __RobotInitialPoint__=[-75.9778,15.0000,291.2286] #cooresponding to angles(pi/2 pi/2 pi/2)
    __angleOriatation__=[1,1,-1]
    __angleRange__=[[0,180*ANGLE2PI_FACTOR],[0,180*ANGLE2PI_FACTOR],[0,180*ANGLE2PI_FACTOR]]

    print __ArdunioInitialAngle__,__RobotInitialPoint__,__angleOriatation__,__angleRange__
    
    angle2Ardunio=ConvertAngle2Ardunio(__ArdunioInitialAngle__,__RobotInitialAngle__,__angleOriatation__,__angleRange__)
    print angle2Ardunio.covert2ArdunioAngle([0.0, 5.1315257464285082, 4.5129870159514969])
                
                
