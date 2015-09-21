#include "servoControl.h"

ServoControl::ServoControl(unsigned char angleSet,unsigned short DelayTime){
  this->StepAngle=angleSet;
  this->StepDelayTime=DelayTime;
}




#define DEBUG

#ifdef DEBUG
  const byte PrintBufSize=50;
  char printStr[PrintBufSize]={0};
#endif

void ServoControl::servoMoving(unsigned short baseAngle,unsigned short shoulderAngle, unsigned short embowAngle){
  //int baseDelta,shoulderDelta,embowDelta;
  unsigned short maxAngle= 0;
  //int stepNum=0;
  //float baseStep,shoulderStep,embowStep;
     
  baseAngle=constrain(baseAngle,ServoPulseMin,ServoPulseMax);
  shoulderAngle=constrain(shoulderAngle,ServoPulseMin,ServoPulseMax);
  embowAngle=constrain(embowAngle,ServoPulseMin,ServoPulseMax);
      
  int baseDelta=baseAngle-servosPos[base].curPos;
  int shoulderDelta=shoulderAngle-servosPos[shoulder].curPos;
  int embowDelta=embowAngle-servosPos[embow].curPos;
      
  maxAngle=max(abs(baseDelta), abs(shoulderDelta)); 
  maxAngle= max(abs(maxAngle), abs(embowDelta));
  
#ifdef DEBUG
  memset(printStr,0,PrintBufSize*sizeof(byte));
  snprintf(printStr,PrintBufSize,"Moving:[%d %d %d] to [%d %d %d]\n\r",servosPos[base].curPos,servosPos[shoulder].curPos,servosPos[embow].curPos,baseAngle,shoulderAngle,embowAngle);
  Serial.print(printStr);
#endif
  //Serial.write(maxAngle);
  int stepNum=(maxAngle/this->StepAngle);
  //Serial.write(stepNum);
  if(stepNum <= 0){
    return;
  }  
  int baseStep=baseDelta/stepNum;
  int shoulderStep=shoulderDelta/stepNum;
  int embowStep=embowDelta/stepNum;  
  
  int stepLeft=stepNum;
  while(stepLeft > 0 ){
      servoMovingOneStep(baseAngle,base,stepLeft);    
      servoMovingOneStep(shoulderAngle,shoulder,stepLeft);      
      servoMovingOneStep(embowAngle,embow,stepLeft);
      delay(this->StepDelayTime);     
      stepLeft--;    
  }  
}

void ServoControl::servoMovingOneStep(unsigned short desAngle, byte servoIndex, unsigned short stepNum){ 
  int angleDelta=desAngle-servosPos[servoIndex].curPos;    
  int currentStep=angleDelta/int(stepNum);
  servosPos[servoIndex].curPos=servosPos[servoIndex].curPos+currentStep;
  servos[servoIndex].write(servosPos[servoIndex].curPos);
}



void ServoControl::movingOrDrawing(byte theFlag){ 
  int desAngle=theFlag == DRAWING?CenterPos:ServoPulseMax;
  int angleDelta=desAngle-servosPos[wristrot].curPos; 
  
  if(!angleDelta) 
    return;
    
  int stepNum=angleDelta>0 ? 100 : -100;
  byte stepLeft=9; //that is 900/50
  while(stepLeft > 0 ){
      servosPos[wristrot].curPos += stepNum;
      servos[wristrot].write(servosPos[wristrot].curPos);
      delay(300);     
      stepLeft--;    
  } 
  servosPos[wristrot].curPos = desAngle;
  servos[wristrot].write(servosPos[wristrot].curPos);
}



