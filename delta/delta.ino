#include <Servo.h>

Servo servo0;
Servo servo1;
Servo servo2;

// create array
int incoming[3];

void setup(){
  Serial.begin(9600);
  Serial1.begin(9600);

  servo0.attach(2);
  servo1.attach(3);
  servo2.attach(4);

  servo0.write(70);
  servo1.write(20);
  servo2.write(75);   

  pinMode(13,OUTPUT);
  digitalWrite(13,LOW);
}

void loop(){
  while(Serial.available() >= 3){
    for (int i = 0; i < 3; i++){
      incoming[i] = Serial.read();
    }
    // use the values
    
    servo0.write(incoming[0]+60);
    servo1.write(incoming[1]+10);
    servo2.write(incoming[2]+75);
  }
}
