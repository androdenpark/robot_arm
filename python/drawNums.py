import time

__TensFormPoint__=[[-170, 5, 210],[-90, 5, 250],[-153, 5, 150],[-88, 5, 192],[-125, 5, 100],[-78, 5, 135]]
__OnesFormPoint__=[[-60, 5, 260],[15, 5, 290],[-53, 5, 205],[15, 5, 245],[-35, 5, 150],[25, 5, 195]]

class DrawingNum:
    def __init__(self):
        self.ArrayForZero()
        self.ArrayForOne()
        self.ArrayForTwo()
        self.ArrayForThree()
        self.ArrayForFour()
        self. ArrayForFive()
        self. ArrayForSix()
        self.ArrayForSeven()
        self.ArrayForEight()
        self. ArrayForNine()
        self. ArrayForTen()
        self.ArrayForTwenty()
        self.ArrayForThirsty()
        self. ArrayForFourty()
        self.ArrayForFifty()
        self. ArrayForSixty()
        self. ArrayForSeventy()
        self.ArrayForEighty()
        self.ArrayForNinety()
        self.singleArrayBuf=[self.drawing_0,self.drawing_1,self.drawing_2,self.drawing_3,self.drawing_4,self.drawing_5,self.drawing_6,self.drawing_7,self.drawing_8,self.drawing_9]
        self.tenthArrayBuf=[self.drawing_10,self.drawing_20,self.drawing_30,self.drawing_40,self.drawing_50,self.drawing_60,self.drawing_70,self.drawing_80,self.drawing_90]

    def getdrawNumsArray(self, yourNum):
        tenth,singles=divmod(yourNum,10)
        getSingleArray=self.singleArrayBuf[singles]
        if tenth > 0 :
            getTenthArray=self.tenthArrayBuf[tenth-1]
        else:
            getTenthArray=[]
        print getSingleArray+getTenthArray 
        return getSingleArray+getTenthArray

    def changeOrientation(self, message,serialObj):
        serialObj.writeData(message)
        batre=""
        while True:
            badsfds=serialObj.readByte(5)
            if badsfds is None:
                print "change head orientation failed!"
                break
            batre += badsfds
            if "OK" in batre:
                print "change head orientation OK!"
                break        
        

    def draw(self,currentPoint,yourNum,serialObj,drawingObj):
        if yourNum <0 or yourNum >99:
            return currentPoint
        
        else:
            StartPoint=currentPoint
            for value in self.getdrawNumsArray(yourNum):
                EndPoint=value["point"]
                if value["move"] :
                    #serialObj.writeData("moving\r")
                    self.changeOrientation("moving\r",serialObj)
                else:
                    #serialObj.writeData("drawing\r")
                    self.changeOrientation("drawing\r",serialObj)
                '''
                batre=""
                while True:
                    badsfds=serialObj.readByte(15)
                    if badsfds is None:
                        print "sdf"
                        break
                    batre += badsfds
                    if "OK" in batre:
                        break
                '''
                print StartPoint,EndPoint
                status,sentPoint=drawingObj.draw([StartPoint,EndPoint])
                if(status):
                    StartPoint=sentPoint
            self.changeOrientation("moving\r",serialObj)
            return StartPoint
        
        
    def ArrayForZero(self):
        self.drawing_0=[]
        self.drawing_0.append({"point":__OnesFormPoint__[0],"move":True})
        self.drawing_0.append({"point":__OnesFormPoint__[1],"move":False})
        self.drawing_0.append({"point":__OnesFormPoint__[5],"move":False})
        self.drawing_0.append({"point":__OnesFormPoint__[4],"move":False})
        self.drawing_0.append({"point":__OnesFormPoint__[0],"move":False})
        
    def ArrayForOne(self):
        self.drawing_1=[]
        self.drawing_1.append({"point":__OnesFormPoint__[0],"move":True})
        self.drawing_1.append({"point":__OnesFormPoint__[4],"move":False})

    def ArrayForTwo(self):
        self.drawing_2=[]
        self.drawing_2.append({"point":__OnesFormPoint__[0],"move":True})
        self.drawing_2.append({"point":__OnesFormPoint__[1],"move":False})
        self.drawing_2.append({"point":__OnesFormPoint__[3],"move":False})
        self.drawing_2.append({"point":__OnesFormPoint__[2],"move":False})
        self.drawing_2.append({"point":__OnesFormPoint__[4],"move":False})
        self.drawing_2.append({"point":__OnesFormPoint__[5],"move":False})

    def ArrayForThree(self):
        self.drawing_3=[]
        self.drawing_3.append({"point":__OnesFormPoint__[0],"move":True})
        self.drawing_3.append({"point":__OnesFormPoint__[1],"move":False})
        self.drawing_3.append({"point":__OnesFormPoint__[3],"move":False})
        self.drawing_3.append({"point":__OnesFormPoint__[2],"move":False})
        self.drawing_3.append({"point":__OnesFormPoint__[3],"move":False})
        self.drawing_3.append({"point":__OnesFormPoint__[5],"move":False})
        self.drawing_3.append({"point":__OnesFormPoint__[4],"move":False})

    def ArrayForFour(self):
        self.drawing_4=[]
        self.drawing_4.append({"point":__OnesFormPoint__[0],"move":True})
        self.drawing_4.append({"point":__OnesFormPoint__[2],"move":False})
        self.drawing_4.append({"point":__OnesFormPoint__[3],"move":False})
        self.drawing_4.append({"point":__OnesFormPoint__[1],"move":True})
        self.drawing_4.append({"point":__OnesFormPoint__[5],"move":False})

    def ArrayForFive(self):
        self.drawing_5=[]
        self.drawing_5.append({"point":__OnesFormPoint__[1],"move":True})
        self.drawing_5.append({"point":__OnesFormPoint__[0],"move":False})
        self.drawing_5.append({"point":__OnesFormPoint__[2],"move":False})
        self.drawing_5.append({"point":__OnesFormPoint__[3],"move":False})
        self.drawing_5.append({"point":__OnesFormPoint__[5],"move":False})
        self.drawing_5.append({"point":__OnesFormPoint__[4],"move":False})

    def ArrayForSix(self):
        self.drawing_6=[]
        self.drawing_6.append({"point":__OnesFormPoint__[1],"move":True})
        self.drawing_6.append({"point":__OnesFormPoint__[0],"move":False})
        self.drawing_6.append({"point":__OnesFormPoint__[4],"move":False})
        self.drawing_6.append({"point":__OnesFormPoint__[5],"move":False})
        self.drawing_6.append({"point":__OnesFormPoint__[3],"move":False})
        self.drawing_6.append({"point":__OnesFormPoint__[2],"move":False})

    def ArrayForSeven(self):
        self.drawing_7=[]
        self.drawing_7.append({"point":__OnesFormPoint__[0],"move":True})
        self.drawing_7.append({"point":__OnesFormPoint__[1],"move":False})
        self.drawing_7.append({"point":__OnesFormPoint__[5],"move":False})


    def ArrayForEight(self):
        self.drawing_8=[]
        self.drawing_8.append({"point":__OnesFormPoint__[3],"move":True})
        self.drawing_8.append({"point":__OnesFormPoint__[2],"move":False})
        self.drawing_8.append({"point":__OnesFormPoint__[0],"move":False})
        self.drawing_8.append({"point":__OnesFormPoint__[1],"move":False})
        self.drawing_8.append({"point":__OnesFormPoint__[5],"move":False})
        self.drawing_8.append({"point":__OnesFormPoint__[4],"move":False})
        self.drawing_8.append({"point":__OnesFormPoint__[2],"move":False})

        
    def ArrayForNine(self):
        self.drawing_9=[]
        self.drawing_9.append({"point":__OnesFormPoint__[3],"move":True})
        self.drawing_9.append({"point":__OnesFormPoint__[2],"move":False})
        self.drawing_9.append({"point":__OnesFormPoint__[0],"move":False})
        self.drawing_9.append({"point":__OnesFormPoint__[1],"move":False})
        self.drawing_9.append({"point":__OnesFormPoint__[5],"move":False})


    def ArrayForTen(self):
        self.drawing_10=[]
        self.drawing_10.append({"point":__TensFormPoint__[0],"move":True})
        self.drawing_10.append({"point":__TensFormPoint__[4],"move":False})



    def ArrayForTwenty(self):
        self.drawing_20=[]
        self.drawing_20.append({"point":__TensFormPoint__[0],"move":True})
        self.drawing_20.append({"point":__TensFormPoint__[1],"move":False})
        self.drawing_20.append({"point":__TensFormPoint__[3],"move":False})
        self.drawing_20.append({"point":__TensFormPoint__[2],"move":False})
        self.drawing_20.append({"point":__TensFormPoint__[4],"move":False})
        self.drawing_20.append({"point":__TensFormPoint__[5],"move":False})

    def ArrayForThirsty(self):
        self.drawing_30=[]
        self.drawing_30.append({"point":__TensFormPoint__[0],"move":True})
        self.drawing_30.append({"point":__TensFormPoint__[1],"move":False})
        self.drawing_30.append({"point":__TensFormPoint__[3],"move":False})
        self.drawing_30.append({"point":__TensFormPoint__[2],"move":False})
        self.drawing_30.append({"point":__TensFormPoint__[3],"move":False})
        self.drawing_30.append({"point":__TensFormPoint__[5],"move":False})
        self.drawing_30.append({"point":__TensFormPoint__[4],"move":False})

    def ArrayForFourty(self):
        self.drawing_40=[]
        self.drawing_40.append({"point":__TensFormPoint__[0],"move":True})
        self.drawing_40.append({"point":__TensFormPoint__[2],"move":False})
        self.drawing_40.append({"point":__TensFormPoint__[3],"move":False})
        self.drawing_40.append({"point":__TensFormPoint__[1],"move":True})
        self.drawing_40.append({"point":__TensFormPoint__[5],"move":False})
        
    def ArrayForFifty(self):
        self.drawing_50=[]
        self.drawing_50.append({"point":__TensFormPoint__[1],"move":True})
        self.drawing_50.append({"point":__TensFormPoint__[0],"move":False})
        self.drawing_50.append({"point":__TensFormPoint__[2],"move":False})
        self.drawing_50.append({"point":__TensFormPoint__[3],"move":False})
        self.drawing_50.append({"point":__TensFormPoint__[5],"move":False})
        self.drawing_50.append({"point":__TensFormPoint__[4],"move":False})
        
    def ArrayForSixty(self):
        self.drawing_60=[]
        self.drawing_60.append({"point":__TensFormPoint__[1],"move":True})
        self.drawing_60.append({"point":__TensFormPoint__[0],"move":False})
        self.drawing_60.append({"point":__TensFormPoint__[4],"move":False})
        self.drawing_60.append({"point":__TensFormPoint__[5],"move":False})
        self.drawing_60.append({"point":__TensFormPoint__[3],"move":False})
        self.drawing_60.append({"point":__TensFormPoint__[2],"move":False})

    def ArrayForSeventy(self):
        self.drawing_70=[]
        self.drawing_70.append({"point":__TensFormPoint__[0],"move":True})
        self.drawing_70.append({"point":__TensFormPoint__[1],"move":False})
        self.drawing_70.append({"point":__TensFormPoint__[5],"move":False})

    def ArrayForEighty(self):
        self.drawing_80=[]
        self.drawing_80.append({"point":__TensFormPoint__[0],"move":True})
        self.drawing_80.append({"point":__TensFormPoint__[1],"move":False})
        self.drawing_80.append({"point":__TensFormPoint__[3],"move":False})
        self.drawing_80.append({"point":__TensFormPoint__[2],"move":False})
        self.drawing_80.append({"point":__TensFormPoint__[4],"move":False})
        self.drawing_80.append({"point":__TensFormPoint__[5],"move":False})
        self.drawing_80.append({"point":__TensFormPoint__[3],"move":False})
        self.drawing_80.append({"point":__TensFormPoint__[2],"move":False})
        self.drawing_80.append({"point":__TensFormPoint__[0],"move":False})

    def ArrayForNinety(self):
        self.drawing_90=[]
        self.drawing_90.append({"point":__TensFormPoint__[3],"move":True})
        self.drawing_90.append({"point":__TensFormPoint__[2],"move":False})
        self.drawing_90.append({"point":__TensFormPoint__[0],"move":False})
        self.drawing_90.append({"point":__TensFormPoint__[1],"move":False})
        self.drawing_90.append({"point":__TensFormPoint__[5],"move":False})
