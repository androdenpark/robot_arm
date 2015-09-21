#include "servoDrawing.h"

ServoDrawing::ServoDrawing():ServoControl(StepAngleDr,StepDelayTimeDr){}

void ServoDrawing::dealComingMessage(MessageBuf_t *message){
  byte sendLen = 0;
  int baseAngleValue=0;
  int shoulderAgnleValue=0;
  int embowAngleValue=0;
  while(sendLen< message->bufLen ){
              baseAngleValue = (((unsigned short)*(message->mesAddr+sendLen))<<8)+*(message->mesAddr+sendLen+1);
              sendLen += 2;
              shoulderAgnleValue = (((unsigned short)*(message->mesAddr+sendLen))<<8)+*(message->mesAddr+sendLen+1);
              sendLen += 2;
              embowAngleValue = (((unsigned short)*(message->mesAddr+sendLen))<<8)+*(message->mesAddr+sendLen+1);
              //Serial.write(*(AngleBuf+sendLen));
              //Serial.write(0x30);
              sendLen += 2;
              this->servoMoving(baseAngleValue, shoulderAgnleValue, embowAngleValue);
  } 
}


