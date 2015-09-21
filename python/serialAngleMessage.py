import time, datetime

__MovingStep__=2
__MovingStepTime__=0.1
__AngleListLenMax__=100

import traceback

class SerialAngleMessage:
    def __init__(self, serialObj):
        self.messageHeader="FROMPC\r"
        self.messageTail="END"
        self.serial=serialObj

    #################the 10*Angle range[0 1800],min 550 max 2350###############################
    def convertAngle2SerialFormat(self, theAngle, baseNum=550):
        convert2Int=int(round(theAngle*10))+baseNum
        return self.convertWord2Chr(convert2Int)
    
    def convertWord2Chr(self,theNum):
        HighByte=theNum>>8
        LowByte=theNum&0xFF
        #print HighByte,LowByte
        return chr(HighByte)+chr(LowByte),theNum
        

    def sendMessageHeader(self, theCoreLen):
        try:
            if not self.serial.writeData(self.messageHeader):
                return False
            return self.serial.writeData(theCoreLen)
        except:
            return False
        
    def sendMessageCore(self, coreMassage):
        try:
            return self.serial.writeData(coreMassage)
        except :
            return False

    def sendMessageTail(self):
        try:
            return self.serial.writeData(self.messageTail)
        except:
            return False

    def angleListTransform(self, theAngleList):
        theCoreMassage=""
        theCheckWord=0
        for angles in theAngleList:
            for angle in angles:
                angleChr,intvalue=self.convertAngle2SerialFormat(angle)
                theCoreMassage += angleChr
                theCheckWord ^=intvalue
        checkStr,ckeckval=self.convertWord2Chr(theCheckWord)
        return theCoreMassage+checkStr



    def messagePartical(self, theAngleList):
        messageMax=__AngleListLenMax__//6 - 2 # two byte for partity
        messageSegments=divmod(len(theAngleList), messageMax)
        #totalNum=messageSegments[0] if messageSegments[1]==0 else messageSegments[0]+1
        messageReturn=[]
        endIndex = 0
        for index in range(1, messageSegments[0]+1):
            startIndex=(index-1)*(messageMax)
            endIndex = startIndex+messageMax
            messageReturn.append(theAngleList[startIndex:endIndex])
        if messageSegments[1] != 0 :
            messageReturn.append(theAngleList[endIndex:])

        return messageReturn


    def sendLongMessage(self,theAngleList):
        #print len(theAngleList)
        messageSegments=self.messagePartical(theAngleList)
        for messagePart in messageSegments:
            #print len(messagePart)
            status,mess=self.movingMessage(messagePart)
            if not status:
                print mess
                return False
            #return "HAHA"
        return True

    
    def sendAngleMessage(self,theAngleList):
        print theAngleList
        try:
            coreMassage=self.angleListTransform(theAngleList)
            #if (self.angleListLenConstrain(len(coreMassage))):
            #    return False
            angleLenChr,angleLen=self.convertWord2Chr(len(coreMassage))
            if not self.sendMessageHeader(angleLenChr):
                return False
            #time.sleep(palseTime)
            if not self.sendMessageCore(coreMassage):
                return False
            #time.sleep(palseTime)
            if not self.sendMessageTail():
                return False
            return True
        except:
            traceback.print_exc()  
            return False

    def movingMessage(self, theAngleList):
        if not self.sendAngleMessage(theAngleList):
            return False,"Message Send Error!"
        waitTime=self.calculateMovingTime(theAngleList)+1 #one more second
        print waitTime
        recaiveMessage=""
        while True:
            byteRecaived=self.serial.readByte(waitTime)
            #print byteRecaived
            if byteRecaived is None:
                return False,"Time Out!"
            #print ord(byteRecaived)
            recaiveMessage += byteRecaived
            #print recaiveMessage
            status,mess=self.repliedMessage(recaiveMessage)
            if not status :
                return status,mess
            else:
                if "Finished" in mess:
                    return status,mess
                if "Info" in mess:
                    print mess+recaiveMessage
                    recaiveMessage=""
                    
                
                
    def repliedMessage(self, theMes):
        if "ERROR:01" in theMes:
            return False,"Message Transmit Error!"
        if "ERROR:02" in theMes:
            return False,"Arduino Memmory Lack!"
        if "OK:01" in theMes:
            return True,"Transmit Info:"
        if "OK:02" in theMes:
            return True,"Moving Finished!"
        if "Moving" in theMes and "\n\r" in theMes:
            return True,"Debug Info:"
        return True, "Normal Running!"

    def calculateMovingTime(self, theAngleList):
        lastBaseAngle=(theAngleList[0])[0]
        lastShoulderAngle=(theAngleList[0])[1]
        lastEmbowAngle=(theAngleList[0])[2]
        timeNeed=0
        for angles in theAngleList:
            daltaBase=abs(lastBaseAngle-angles[0])
            daltaShoulder=abs(lastShoulderAngle-angles[1])
            daltaEmbow=abs(lastEmbowAngle-angles[2])
            maxAngle=(max([daltaBase,daltaShoulder,daltaEmbow]))*10 # the angle sent to arduino is *10 bigger,use function 'convertAngle2SerialFormat()'
            #print maxAngle
            timeNeed +=(maxAngle//__MovingStep__+1)*__MovingStepTime__
            #print timeNeed,"TIME"
            lastBaseAngle=angles[0]
            lastShoulderAngle=angles[1]
            lastEmbowAngle=angles[2]
        return timeNeed
        
            
            
        
            
        
