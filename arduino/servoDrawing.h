#ifndef servoDrawing_H
#define servoDrawing_H

#include "servoControl.h"
//#include "listenSrilAglMge.h"

#define StepAngleDr 2
#define StepDelayTimeDr 30


struct MessageBuf_t{
  byte* mesAddr;
  byte bufLen;
};

//typedef void (*message_cb)(MessageBuf_t*);


class ServoDrawing:public ServoControl{ 
  
  public:
    ServoDrawing();
    void dealComingMessage(MessageBuf_t *message);
  
};

//typedef void (ServoDrawing::*message_cb)(MessageBuf_t*);

#endif
