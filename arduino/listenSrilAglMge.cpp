#include "listenSrilAglMge.h"
#include <SimpleTimer.h>

char *HEADER="FROMPC";
char *TAIL="END";


ListenSrilAglMge::ListenSrilAglMge():MessageHeader(HEADER),MessageTail(TAIL),MaxMallocSize(MALLOC_SIZE),ByteTransMaxTime(1){
  this->CurrentTime=0;
  this->isListenning=0;
}


//self.messageHeader="FROMPC"
unsigned short ListenSrilAglMge::findMessageHeader(void){
  this->CurrentTime=millis();
  //byte recaiveIndex=1;
  byte recaiveIndex=0;
  int recaivedByte=0;  
  
  //const byte needBytes=strlen(this->MessageHeader)+2;  //2 bytes for storing message len after header
  const byte needBytes=2; 
  
  //char MessageHeaderBuf[needBytes];
  // MessageHeaderBuf[0]=*this->MessageHeader;
  char MessageHeaderBuf[needBytes];
  
  unsigned long waitTime=this->ByteTransMaxTime*needBytes;
  while((millis()-this->CurrentTime) < waitTime){
    recaivedByte=Serial.read();
    if ( recaivedByte>= 0 ) { 
        MessageHeaderBuf[recaiveIndex]=recaivedByte;  
        //Serial.write(MessageHeaderBuf[recaiveIndex]);
        recaiveIndex++;
    }
    if( recaiveIndex >= needBytes ){
      return (((unsigned short)(MessageHeaderBuf[needBytes-2]))<<8)+(unsigned short)(MessageHeaderBuf[needBytes-1]);
      /*
      if(0 == memcmp(MessageHeaderBuf,this->MessageHeader,strlen(this->MessageHeader))){
        //Serial.write(111);
        return (((unsigned short)(MessageHeaderBuf[needBytes-2]))<<8)+(unsigned short)(MessageHeaderBuf[needBytes-1]);
      }else{
        Serial.flush();
        return 0;
      }*/
    }
  }
  Serial.flush();
  return 0;
}


// return 0 when there is no message, or messageLen(anglesValue+parity) when there is.
unsigned short ListenSrilAglMge::isHeaderComing(void){
    return findMessageHeader();
    /*
    if(*this->MessageHeader ==  Serial.read() ){
      //Serial.write(222);
      return findMessageHeader();
    }else{
      return 0;
    }*/
}







byte ListenSrilAglMge::checkMessageTail(void){
  this->CurrentTime=millis();  
  byte recaiveIndex=0;
  int recaivedByte=0;
  const byte messageTailLen=strlen(this->MessageTail);
  char MessageTailBuf[messageTailLen];
  unsigned long waitTime=this->ByteTransMaxTime*messageTailLen;
  while((millis()-this->CurrentTime) < waitTime){
   // while(1){
    //Serial.write(Serial.read());}
    recaivedByte=Serial.read();
    if (recaivedByte >= 0) { 
      MessageTailBuf[recaiveIndex]=recaivedByte;      
      //Serial.write(MessageHeaderBuf[recaiveIndex]);
      recaiveIndex++;
    }
    if(recaiveIndex >= messageTailLen){
      //Serial.write(88);
      if(0 == memcmp(MessageTailBuf,this->MessageTail,strlen(this->MessageTail))){
        return 1;
      }else{
        Serial.flush();
        return 0;
      }
    }
  }
}




int ListenSrilAglMge::dealTheAngleMessage(unsigned short messageLen){
  unsigned short recavieNum=0;
  unsigned short checkResult=0;
  if( 0>this->allocMessagebuf(messageLen) )
    return -1;
  /*
  AngleBuf = (byte *)malloc(sizeof(byte)*messageLen);
  if (AngleBuf == NULL){
    //Serial.write(33);
    return -1;
  }*/
  this->CurrentTime=millis();
  int recaivedByte=0;
  //Serial.write(44);
  unsigned long waitTime=this->ByteTransMaxTime*messageLen;
       //  while(1){
        // if( recavieNum < messageLen){
        // *(AngleBuf+recavieNum) = 1;
         //recavieNum++;}
       //  loopp();
       
    // }
  while((millis()-this->CurrentTime) < waitTime){
      recaivedByte = Serial.read();
      if (recaivedByte >= 0){ 
        *(this->message.mesAddr+recavieNum) = byte(recaivedByte);
        checkResult ^= (((unsigned short)(*(this->message.mesAddr+recavieNum)))<<(8*((recavieNum+1)%2)));
        //Serial.write(recavieNum);
        recavieNum++;
      }
      if( recavieNum >= messageLen){
        //Serial.write(66);
        if( 0 == this->parityChecking(checkResult))
          return 0;
        else
          return checkMessageTail();//sucess
      }
  }
  //Serial.write(55);
  Serial.flush();
  //free(AngleBuf);    
  return 0;  //timeout
}



byte ListenSrilAglMge::parityChecking(unsigned short checkResult){
  if(checkResult == 0){
    this->message.bufLen -= 2;
    return 1;
  }
  return 0;
}





byte ListenSrilAglMge::isAngleMessage(void){  
  unsigned short recievedAngleLen=this->isHeaderComing() ; 
  Serial.print(recievedAngleLen); 
  if(!((recievedAngleLen>0) && (recievedAngleLen< this->MaxMallocSize))){
    //Serial.write("");
    return 0;
  }  
  int messageResult= this->dealTheAngleMessage(recievedAngleLen);
  if(messageResult == 0){
      free(this->message.mesAddr); 
      Serial.print("ERROR:01"); //message transmit error
      return 0;
  }
  if(messageResult == -1){
      Serial.print("ERROR:02"); //malloc failed
      return 0;
  }
      Serial.print("OK:01"); //message recaived ok  
      return 1;

}


void ListenSrilAglMge::processMsg(ServoDrawing &servoMoving){
  servoMoving.dealComingMessage(&message);
  free(this->message.mesAddr); 
  Serial.print("OK:02");  //finished moving
}

