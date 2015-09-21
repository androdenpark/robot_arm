#include "serialCommand.h"
int factorialCalculate(byte);
int parseStr2Int(char*);
int transAngle(byte angleValue);
void printCommandList(void);
void splitShell(void);

int parseStr2Int(char *theStr){
    byte highestMux = strlen(theStr);
    //Serial.print("KKK"); 
    int intValue=0;
    byte currentChar=0;
    int i = 0;
    for(; i < highestMux; i++){
        currentChar = constrain(*(theStr+i)-0x30,0,9);
        intValue += currentChar*(factorialCalculate(highestMux-i-1));   
    }
    
    return intValue;
}

int factorialCalculate(byte times){
    int returnValue=1;
    for(byte i=0; i< times; i++)
        returnValue *= 10;  
    return  returnValue; 
}


int transAngle(byte angleValue){
  return ServoPulseMin+angleValue*10 ;
}

//SerialCommand::SerialCommand(){
//  this.servoMoving.dealComingMessage
//}



        

SerialCommand::SerialCommand( ServoDrawing &servo):listenSrilAglMge(),servoMoving(servo){
  memset(this->shellBuf, 0, sizeof(this->shellBuf));

  //this->servoMoving=ServoDrawing();
  //this->listenSrilAglMge=ListenSrilAglMge();
}











cmd_state_t SerialCommand::cmd_setMovePara(int argc, char* argv[])
{
    const char *usage = "usage: setMovePara <stepAngle> <stepTime>\r\n";
    if(argc != 2){
        Serial.print(usage);
        return CMD_DONE;
    }
    //Serial.print(argv[0]);
    //Serial.print(argv[1]);
    //Serial.print("SR\r\n");
    int value=	parseStr2Int(argv[0]);
    byte stepAngle=constrain(value,1,20);
    //Serial.print("DR\r\n");	
    value= parseStr2Int(argv[1]);
    int stepTime=constrain(value,100,2000);
    
    this->servoMoving.set_StepDelayTime(stepTime);
    this->servoMoving.set_StepAngle(stepAngle);
    Serial.print("OK\r\n");	
    return CMD_DONE;
}


#define MAXBUFFSIZE 50
cmd_state_t SerialCommand::cmd_getMovePara(int argc, char* argv[])
{
    const char *usage = "usage: getMovePara \r\n";
    if(argc != 0){
        Serial.print(usage);
        return CMD_DONE;
    }
    char msgBuf[MAXBUFFSIZE]={0};
    snprintf(msgBuf, MAXBUFFSIZE, "Angle Step:%d, Time During:%d,\r\n", this->servoMoving.get_StepAngle(), this->servoMoving.get_StepDelayTime());
    Serial.print(msgBuf);	
    return CMD_DONE;
}




cmd_state_t SerialCommand::cmd_inListenningMode(int argc, char* argv[]){
    const char *usage = "usage: inListenningMode \r\n";
    if(argc != 0){
        Serial.print(usage);
        return CMD_DONE;
    } 
    Serial.print("Listenning Now!\r\n");
    //listenSrilAglMge.setListenStatus(1);
    if(this->listenSrilAglMge.isAngleMessage()){
    //message_cb func=this->servoMoving.dealComingMessage;   
    this->listenSrilAglMge.processMsg(this->servoMoving);
    //Serial.print("OK\r\n");
    }	
    return CMD_DONE;
}

cmd_state_t SerialCommand::cmd_outListenningMode(int argc, char* argv[]){
    const char *usage = "usage: outListenningMode \r\n";
    if(argc != 0){
        Serial.print(usage);
        return CMD_DONE;
    } 
    Serial.print("Off Listenning!\r\n");
    listenSrilAglMge.setListenStatus(0);	
    return CMD_DONE;
}

void SerialCommand::movingWithAngleList(void){
  if(listenSrilAglMge.getListenStatus()){
    if(this->listenSrilAglMge.isAngleMessage()){
    //message_cb func=this->servoMoving.dealComingMessage;   
    this->listenSrilAglMge.processMsg(this->servoMoving);
    //Serial.print("OK\r\n");
    }
  }    
}

cmd_state_t SerialCommand::cmd_movingWithAngle(int argc, char* argv[]){
    const char *usage = "usage: movingWithAngle <base> <shoulder> <embow> \r\n";
    if(argc != 3){
        Serial.print(usage);
        return CMD_DONE;
    } 
    byte Value=parseStr2Int(argv[0]);
    byte baseAngle=constrain(Value,0,180);
    Value=parseStr2Int(argv[1]);
    byte shoulderAngle=constrain(Value,0,180);
    Value=parseStr2Int(argv[2]);
    byte embowAngle=constrain(Value,0,180);    
    this->servoMoving.servoMoving(transAngle(baseAngle),transAngle(shoulderAngle),transAngle(embowAngle));
    Serial.print("OK\r\n");	
    return CMD_DONE;
}

cmd_state_t SerialCommand::cmd_drawingMode(int argc, char* argv[]){
    const char *usage = "usage: moving \r\n";
    if(argc != 0){
        Serial.print(usage);
        return CMD_DONE;
    } 
    this->servoMoving.set_StepDelayTime(100);
    this->servoMoving.set_StepAngle(2);
    this->servoMoving.movingOrDrawing(DRAWING);
    Serial.print("OK\r\n");	
    return CMD_DONE;
}

cmd_state_t SerialCommand::cmd_movingMode(int argc, char* argv[]){
    const char *usage = "usage: drawing \r\n";
    if(argc != 0){
        Serial.print(usage);
        return CMD_DONE;
    } 
    this->servoMoving.set_StepDelayTime(300);
    this->servoMoving.set_StepAngle(20);
    this->servoMoving.movingOrDrawing(MOVING);
    Serial.print("OK\r\n");	
    return CMD_DONE;
}

//#define MAX_CMD_CONSOLE_NUM 20 
typedef cmd_state_t (SerialCommand::*cmd_cb_t)(int argc, char* argv[]);

cmd_cb_t setMovePara_p=&SerialCommand::cmd_setMovePara;
cmd_cb_t getMovePara_p=&SerialCommand::cmd_getMovePara;
cmd_cb_t movingWithAngle_p=&SerialCommand::cmd_movingWithAngle;
cmd_cb_t inListenningMode_p=&SerialCommand::cmd_inListenningMode;
cmd_cb_t outListenningMode_p=&SerialCommand::cmd_outListenningMode;
cmd_cb_t moving_p=&SerialCommand::cmd_movingMode;
cmd_cb_t drawing_p=&SerialCommand::cmd_drawingMode;

struct {
        cmd_cb_t cb;
        const char* str;
} cmd_list[] = {
  { setMovePara_p, "setMovePara"},
  { getMovePara_p, "getMovePara"},
  { movingWithAngle_p, "movingWithAngle"},
  {moving_p, "moving"},
  {drawing_p, "drawing"},
  { inListenningMode_p, "FROMPC"},
 // { outListenningMode_p, "closeTransMode"},
  {0,0}
  };
 
 
  
 

#define MAXARGVNUM 5 
struct{
     char *shellCommand;
     char *argv[MAXARGVNUM];
     byte argvNum;
}shellBuffer;

void SerialCommand::splitShell(void){
  shellBuffer.argvNum=0;
  char *index=this->shellBuf;
  for(byte newArgFlag=0; *index != 0; index++){
      if(*index == ' ') {
          *index = 0;
          newArgFlag=1;
          continue;
      }
      if(newArgFlag){
          shellBuffer.argv[shellBuffer.argvNum]=index;
          shellBuffer.argvNum++;
          newArgFlag=0;
      }
      if(shellBuffer.argvNum>=MAXARGVNUM){
          Serial.print("error:too much args!\r\n");
          break;
      }
  }
  shellBuffer.shellCommand=this->shellBuf;     
}
  
void SerialCommand::shellSchedule(SerialCommand &serialCommd){
  splitShell();
  byte CompareLen;
  for(byte i=0; cmd_list[i].str != 0; i++){
    CompareLen=strlen(cmd_list[i].str)>strlen(shellBuffer.shellCommand)?strlen(cmd_list[i].str):strlen(shellBuffer.shellCommand);
    if(0 == memcmp(shellBuffer.shellCommand,cmd_list[i].str,CompareLen)){
          (serialCommd.*(cmd_list[i].cb))(shellBuffer.argvNum,shellBuffer.argv);      
          memset(this->shellBuf, 0, sizeof(this->shellBuf));
          Serial.print("$:");
          return;
    }
  }  
  memset(this->shellBuf, 0, sizeof(this->shellBuf));
  Serial.print("no shell matched!\r\n");
  printCommandList();
}  
  
  
byte SerialCommand::console_gets(void){
        byte pos = 0;
        char c;        
        for (;;) {
                c=Serial.read();
                if (c == -1)
                        continue;
                //pos++;
                //pos=constrain(pos,0,MAXSHELLLEN-1);
                if (c == '\r' || c == '\n') {
                        this->shellBuf[pos] = 0;
                        Serial.print("\r\n$:");
                        return pos;
                }
                if (c == 0x7F) {
                        pos -= 1; 
                        this->shellBuf[pos] = 0;
                        Serial.write(c);
                        continue;                       
                }
                else{
                        this->shellBuf[pos] = c;
                        Serial.write(c);
                        pos++;
                        pos=constrain(pos,0,MAXSHELLLEN-1);
                        //Serial.print((c+1));
                }

        }
}


void printCommandList(void){
    Serial.print("Available commands:\r\n");
    for(byte i=0; cmd_list[i].cb != 0; i++){
      Serial.print(cmd_list[i].str);
      Serial.print("\r\n");
    }
    Serial.print("$:");
}

