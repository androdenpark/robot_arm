import serial
import datetime


__serialSpeed__=115200




#############this class is only accessable by control center##################

#  after the appliction starts, the following steps must be done:
#    1.register log window to get port infomation shown, use <register_logWindow(infoObj)>
#    2.try to connect the port saved in rom, use <connect(self, baudRate, port)>


#  before recaive the data, the instance must do:
#    1. register the upload obj to handle the racaived data, use <register_upload(self, upLayerobj)>
#    2. set read bytes one time, use <set_readDataLen(self, readLen)>
#    3. clear read buff if needed, use <clear_recaiveBuff(self)>


#  if the instance is no longer need to recaive data,:
#    1. unregister the upload obj to release the thread


#  if  the appliction is going to terminate:
#    1. disconnect the port
#    2. stop the thread



class SerialPortOperation:
    def __init__(self, serialPortNum, serialSpeed=__serialSpeed__):
        self.speed=serialSpeed
        self.portNum=serialPortNum
        self.readLen = 1
    
    def set_readDataLen(self, readLen):
        self.readLen = readLen
    
    def clear_recaiveBuff(self):
        if self.serialObj is not None:
            self.serialObj.flushInput()

    def clear_writeBuff(self):
        if self.serialObj is not None:
            self.serialObj.flushOutput()        

    def isConnect(self):
        if self.serialObj is not None:
            return self.serialObj.isOpen()
        else:
            return False
                   
    def readByte(self, timeoutRequirement=3):
        timeStart=datetime.datetime.now()
        def isTimeout():
            return (datetime.datetime.now()-timeStart).seconds > timeoutRequirement        
        while not isTimeout():                    
            try:            
                dataRecaived = self.serialObj.read(self.readLen)
                if len(dataRecaived)<1: # the read is non-blocking
                    continue
                else:
                    return dataRecaived
            except:
                raise Exception,"Port Error"
        return None
            
    
    def writeData(self, writeData):
        sendLen=len(writeData)           
        if sendLen != self.serialObj.write(str(writeData)):# it should be type of 'str', not include type of 'unicode' 
            return False
        else:
            return True
            
                    
    def connect(self):        
        try:
            self.serialObj = serial.Serial(self.portNum, self.speed, serial.EIGHTBITS, serial.PARITY_NONE,
                                    serial.STOPBITS_ONE, 3, False, False, 3)#timeout 1 seconds
            if not self.isConnect():
                self.serialObj.open()
            return True
        except :
            self.serialObj = None           
            return False

    def disconnect(self):
        try:
            self.serialObj.close()           
        except :
            pass
        finally:
            self.serialObj = None





if __name__=="__main__":
    serialOperition=SerialPortOperation(15)
    if serialOperition.connect():
        print "Connected!"
    else:
        print "Connect Failed!"
        
    serialOperition.readByte()#wait restart finish
    
    if serialOperition.writeData("\xFF\x5A\x5A\x5A\xFE"):
        print "send OK"
    while True:
        try:
            print serialOperition.readByte()
        except:
            serialOperition.writeData("\xFF\x5A\x5A\x5A\xFE")
        finally:
            break
            
    
    
    

