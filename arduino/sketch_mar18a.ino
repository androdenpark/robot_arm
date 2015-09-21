

#include <Servo.h>      //调用一些库文件
#include <TimedAction.h>
#include <SimpleTimer.h> 
#include <Wire.h>
//#include <LiquidCrystal_I2C.h>
                                //定义舵机位置名称，并编号。
   
#include "serialCommand.h" 
#include "servoDrawing.h"
ServoDrawing servoMoving=ServoDrawing();
SerialCommand *serialComm=new SerialCommand(servoMoving); 


void setup() {                            //设置
//  delay(200);
  Wire.begin();
  
//  lcd.init();                             //LCD初始化             
//  lcd.backlight();                 //LCD背光灯打开
//  delay(500);
//  lcd.on();                     // LCD开机
  //setupDisplay();               //调用子程序，设置显示内容门，后面有定义。

//  lcd.clear();          //LCD清屏
//  lcd.blink_off();       //LCD光标闪烁关
//  lcd.home();      


  servoMoving.servoInitial();    
  
  //setupLCD();
  Serial.begin(115200);
}



void loop(){
 // Serial.write(recievedAngleLen);
 //isAngleMessage();
 // inSleep();
 serialComm->checkCommond(*serialComm);
 //serialComm->movingWithAngleList();
 
}  

