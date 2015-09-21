#ifndef serialCommand_H
#define serialCommand_H

#include "servoDrawing.h"
#include "listenSrilAglMge.h"

typedef enum {
        CMD_DONE,
        CMD_INPROGRESS
} cmd_state_t;



#define MAXSHELLLEN 50

class SerialCommand{
  private:
        ServoDrawing &servoMoving;
        ListenSrilAglMge listenSrilAglMge;
        char shellBuf[MAXSHELLLEN];
        
        byte console_gets(void);
        void splitShell(void);
        void shellSchedule(SerialCommand &); 
        
  public:
        SerialCommand( ServoDrawing &);
        cmd_state_t cmd_setMovePara(int argc, char* argv[]);
        cmd_state_t cmd_getMovePara(int argc, char* argv[]);
        cmd_state_t cmd_movingWithAngle(int argc, char* argv[]);
        cmd_state_t cmd_inListenningMode(int argc, char* argv[]);
        cmd_state_t cmd_outListenningMode(int argc, char* argv[]);
        cmd_state_t cmd_drawingMode(int argc, char* argv[]);
        cmd_state_t cmd_movingMode(int argc, char* argv[]);
 
        inline void checkCommond(SerialCommand &serialCommd){
            if(this->console_gets())
              this->shellSchedule(serialCommd);
        }
        
        void movingWithAngleList(void);
        
};



#endif
