#ifndef ListenSrilAglMge_H
#define ListenSrilAglMge_H

#include "stdlib.h"
#include "servoDrawing.h"

typedef unsigned char byte;

#define NULL 0



//#define F_HEADER 'F'
//#define LEN_HEADER strlen(HEADER)
//#define MESSAGE_LEN 2*sizeof(char)
#define MALLOC_SIZE 150*sizeof(byte)
//#define LEN_TAIL strlen(TAIL)

//msg format:header+len+message+tail, where header is "FROMPC", len occupies 2 bytes, message occupies angle_num*2+parity(2 bytes), tail is "END".
class ListenSrilAglMge{
  private:
    MessageBuf_t message;
    //const char *MessageHeader="FROMPC";
    const char *MessageHeader;
    //const char MessageFirstByte;
    //byte MessageHeaderLen=strlen("FROMPC");
    //const byte MessageHeaderLen;
    //const byte messageLenOccupy=2;//2 bytes stored mess len after message header
    //const byte messageLenOccupy;
    //char MessageHeaderBuf[(MessageHeaderLen+messageLenOccupy)]={MessageFirstByte};
    
    //const byte ByteTransMaxTime=1;//1 ms
    const byte ByteTransMaxTime;
    unsigned long CurrentTime ;
    //const byte MaxMallocSize=150; // the ram size of the mcu is 2k.
    const byte MaxMallocSize;
    
    //const char *MessageTail="END";
    const char *MessageTail;
    //byte MessageTailLen = strlen("END");
    //byte MessageTailLen;
    //char MessageTailBuf[MessageTailLen]={0};
    
    byte isListenning;

    unsigned short findMessageHeader(void);
    byte checkMessageTail(void);
    byte parityChecking(unsigned short checkResult);
    unsigned short isHeaderComing(void);
    int dealTheAngleMessage(unsigned short messageLen);
    
  public:
    ListenSrilAglMge();
    inline byte getMessageLen(void){
      return this->message.bufLen;
    }
    
    inline byte getListenStatus(void){
      return this->isListenning;
    }
    inline void setListenStatus(byte stat){
      this->isListenning=stat;
    }
    /*
    inline void setMessageLen(byte theLen){
      this.message.bufLen=theLen;
    }      
    inline void setMessageBufAddr(byte *bufAddr){
      this.message.mesAddr=bufAddr;
    }
    */
    inline byte *getMessageBufAddr(void){
      return this->message.mesAddr;
    }
    
    inline int allocMessagebuf(byte messLen){      
      this->message.mesAddr = (byte *)malloc(sizeof(byte)*messLen);
      if (this->message.mesAddr == NULL){
              //Serial.write(33);
            this->message.bufLen=0;
            return -1;
      }
      this->message.bufLen=messLen;
      return 1;
    }
    
    byte isAngleMessage(void);
    void processMsg(ServoDrawing &);
  
  
};



#endif
