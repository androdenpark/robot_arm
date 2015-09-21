import sys
sys.path.append(str(sys.path[0])+'\\lib')
sys.path.append(str(sys.path[0]))

from ConvertAngle2Ardunio import *
from robotKematics import *
from serialCommunication import  *
from common import *
from movingOnLine import *
from serialAngleMessage import *
from drawingWithDots import *
from drawNums import *
from getAge import *

import time
import traceback


__RobotProperties__=[110,-25,5,15,92,87]


#__RobotInitialAngle__=[0,270*ANGLE2PI_FACTOR,355*ANGLE2PI_FACTOR] #cooresponding to angles(pi/2 pi/2 pi/2)
__RobotInitialAngle__=[0,270*ANGLE2PI_FACTOR,274*ANGLE2PI_FACTOR] #cooresponding to angles(pi/2 pi/2 pi/2)
__ArdunioInitialAngle__=[90*ANGLE2PI_FACTOR,90*ANGLE2PI_FACTOR,90*ANGLE2PI_FACTOR]
#__RobotInitialPoint__=[-47.3096,15.0000,299.3584] #cooresponding to angles(pi/2 pi/2 pi/2)
__RobotInitialPoint__=[ -183.5340, 5.0000, 96.2709]
#__RobotInitialPoint__=[ -71.6689, 0, 99.5825]
__angleOriatation__=[1,1,-1]
__angleRange__=[[0,180*ANGLE2PI_FACTOR],[0,180*ANGLE2PI_FACTOR],[0,180*ANGLE2PI_FACTOR]]





if __name__=="__main__":
    try:
        CurrentPortNum=15
        recaivedByte=""
        serialOperition=SerialPortOperation(CurrentPortNum)
        if serialOperition.connect():
            print "Connected!"
        else:
            print "Connect Failed!"
            sys.exit(1)
        time.sleep(15)#wait restart finish
        
        angle2Ardunio=ConvertAngle2Ardunio(__ArdunioInitialAngle__,__RobotInitialAngle__,__angleOriatation__,__angleRange__)
        obotKinematics=RobotKinematics(__RobotProperties__)
        #moving=MovingOnLine(obotKinematics,angle2Ardunio,__angleWeight__)
        drawing = DrawingWithDots(obotKinematics,angle2Ardunio,serialOperition,__ArdunioInitialAngle__)

        '''
        dotList=[__RobotInitialPoint__,[ -209.4034 , 15.0000 , 206.7224],[ -47.4034 , 15.0000 , 206.7224],__RobotInitialPoint__]
        #dotList=[__RobotInitialPoint__,[ -209.4034 , 15.0000 , 206.7224],[ -209.4034 , 80.0000 , 206.7224]]
        drawing.draw(dotList)
        '''

       
        StartPoint=__RobotInitialPoint__

        '''
        drawing_1=[]
        drawing_1.append({"point":[-67, 0, 133],"move":True})
        drawing_1.append({"point":[-27, 0, 133],"move":False})
        drawing_1.append({"point":[-67, 0, 100],"move":False})
        drawing_1.append({"point":[-27, 0, 90],"move":False})
        drawing_1.append({"point":[-67, 0, 74],"move":False})

        drawing_2=[]
        drawing_2.append({"point":[-13, 0, 133],"move":True})
        drawing_2.append({"point":[27, 0, 133],"move":False})
        drawing_2.append({"point":[-13, 0, 100],"move":False})
        drawing_2.append({"point":[27, 0, 80],"move":False})
        drawing_2.append({"point":[27, 0, 60],"move":False})
        drawing_2.append({"point":[-13, 0, 60],"move":False})

        toHome=[{"point":__RobotInitialPoint__,"move":True}]
        '''

 



      
        
        def getInput():
            try:
                inputValue=input("what you want to Draw [0~99]: ")
                if type(inputValue) == type(3) and inputValue >=0 and inputValue <=99 :
                    return inputValue
                else:
                    return None
            except Exception:
                return

        numberArrayObj = DrawingNum()

        while True:
            #numsInput=getInput()
            time.sleep(1)
            numsInput=getAgeFromServer()
            if numsInput is None:
                print "illegal input, please input a num between 0 to 99!"
                continue
            print "start to draw: ",numsInput
            StartPoint=numberArrayObj.draw(StartPoint,numsInput,serialOperition,drawing)
            

        sys.exit(1)
        
        
        StartPoint=__RobotInitialPoint__
        warningStr="Fault Input, format:[11,12,13]"
        while True:
            '''
            try:
                inputValue=input("your start point: ")
                if type(inputValue) == type([]) and len(inputValue) == 3:
                    StartPoint=inputValue
                else:
                    print warningStr
                    continue
            except:
                print warningStr
                continue
            '''
            print  "your start point: ",StartPoint 
            
            try:
                inputValue=input("your end point: ")
                if type(inputValue) == type([]) and len(inputValue) == 3:
                    EndPoint=inputValue
                elif "init" in inputValue:
                    EndPoint=__RobotInitialPoint__
                elif "quit" in inputValue:
                    print "Exiting"
                    serialOperition.disconnect()
                    sys.exit(1)
                    print "Exit failed"
                elif "move" in  inputValue:
                    serialOperition.writeData("moving\r")
                    continue
                elif "draw" in  inputValue:
                    serialOperition.writeData("drawing\r")
                    continue
                else:
                    print warningStr
                    continue
            except Exception as e:
                print e
                print warningStr
                continue

            print  "your end point: ",EndPoint

            status,sentPoint=drawing.draw([StartPoint,EndPoint])
            if(status):
                StartPoint=sentPoint
            
            




            
















        '''
        startPoint=__RobotInitialPoint__
        endPoint=[ -75.9778 , 15.0000 , 206.7224]
        startAngle=__ArdunioInitialAngle__
        print startPoint,startAngle        
        angles1=moving.calculatePointsOnLine(startPoint,endPoint,startAngle,__movingStep__)
        print angles1
        
        startPoint=angles1[-1]["Corrd"]
        endPoint=[ -209.4034 , 15.0000 , 206.7224]
        startAngle=angles1[-1]["angle"]
        print startPoint,startAngle        
        angles2=moving.calculatePointsOnLine(startPoint,endPoint,startAngle,__movingStep__)
        print angles2
        
        startPoint=angles2[-1]["Corrd"]
        endPoint=__RobotInitialPoint__
        startAngle=angles2[-1]["angle"]
        print startPoint,startAngle
        angles3=moving.calculatePointsOnLine(startPoint,endPoint,startAngle,__movingStep__)
        print angles3

    
        messageToSend=[]
        serialAngleM=SerialAngleMessage(serialOperition)
        for value in angles1+angles2+angles3:
            pointBase=value["angle"][0]*PI2ANGLE_FACTOR
            pintShoulder=value["angle"][1]*PI2ANGLE_FACTOR
            pintEmbow=value["angle"][2]*PI2ANGLE_FACTOR
            #print pointBase,pintShoulder,pintEmbow
            messageToSend.append([pointBase,pintShoulder,pintEmbow])
        #messageToSend.append([90,90,90])
        print serialAngleM.sendLongMessage(messageToSend)
        '''

                
        '''
        for value in angles1+angles2:
            pointBase=value["angle"][0]*PI2ANGLE_FACTOR
            pintShoulder=value["angle"][1]*PI2ANGLE_FACTOR
            pintEmbow=value["angle"][2]*PI2ANGLE_FACTOR
            print pointBase,pintShoulder,pintEmbow
            #messageToSend.append([pointBase,pintShoulder,pintEmbow])
        
            
            message=chr(0xFF)+chr(int(round(pointBase)))+chr(int(round(pintShoulder)))+chr(int(round(pintEmbow)))+chr(0xFE)
            #continue
            if serialOperition.writeData(message):
                print "send OK"
            else:
                print "send wrong"
            while True:
                isRecaived = serialOperition.readByte()
                if isRecaived is None:
                    print recaivedByte
                    recaivedByte=""
                    break
                else:
                    recaivedByte += isRecaived
                    if "OK!" in recaivedByte:
                        print recaivedByte
                        recaivedByte=""
                        break
        serialOperition.writeData("\xFF\x5A\x5A\x5A\xFE")                   
        '''          
    except Exception as e:
        print e
        traceback.print_exc()  

        




        
