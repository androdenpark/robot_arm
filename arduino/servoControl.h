#ifndef servoControl_H
#define servoControl_H

#include <Servo.h>      //调用一些库文件
#include <SimpleTimer.h> 
typedef unsigned char byte;

#define SERVO_NUM 6

#define ServoPulseMax 2350
#define ServoPulseMin 550
#define ServoPuseRange 1800
#define CenterPos ServoPulseMin+ServoPuseRange/2

#define DRAWING 1
#define MOVING 2

typedef struct{              //数组框架结构
//  byte neutral;             //中位角度
//  byte minPos;             //最小角度
//  byte maxPos;            //最大角度
//  byte delaySpeed;         //延时时间
  int curPos;            //舵机当前角度
} ServoPos;              //结构体名称

enum ServoIndex_E{
  base=0,
  shoulder,
  embow,
  wristflex,        
  wristrot,          
  gripper
};


class ServoControl{
  private:
    unsigned char StepAngle;
    unsigned short StepDelayTime;
    ServoPos servosPos[SERVO_NUM];
    Servo servos[SERVO_NUM];
    void servoMovingOneStep(unsigned short desAngle, byte servoIndex, unsigned short stepNum);  
    
  public:
    ServoControl(unsigned char angleSet,unsigned short DelayTime);
    inline void set_StepAngle(unsigned char value){
      this->StepAngle=value;
    }
    inline unsigned char get_StepAngle(void){
      return this->StepAngle;
    }
    inline void set_StepDelayTime(unsigned short value){
      this->StepDelayTime=value;
    }
    inline unsigned short get_StepDelayTime(void){
      return this->StepDelayTime;
    }

    inline void atachServos(void){
      for(int i=0; i<SERVO_NUM; i++)       
        this->servos[i].attach(i+4);
    }
    inline void setServoInitPos(void){
      for(int i=0; i<SERVO_NUM; i++)       
        this->servosPos[i].curPos=CenterPos;
        delay(200);
    }
    inline void servoInitial(void){
        this->atachServos();
        this->setServoInitPos();
        this->movingOrDrawing(MOVING);
    }

    void servoMoving(unsigned short baseAngle,unsigned short shoulderAngle, unsigned short embowAngle);
    void movingOrDrawing(byte theFlag);
      
  
};

#endif
