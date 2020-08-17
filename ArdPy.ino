const int Ma1=8;
const int Ma2=9;
const int en_a_RSPEED=10;
const int en_b_LSPEED=11; 
void setup() {
  // put your setup code here, to run once:
pinMode(Ma1,OUTPUT);
pinMode(Ma2,OUTPUT);
pinMode(en_a_RSPEED,OUTPUT);
pinMode(en_b_LSPEED,OUTPUT);
analogWrite(en_b_LSPEED,100);
analogWrite(en_a_RSPEED,100);
//pinMode(A1 , OUTPUT);
//pinMode(A2 , OUTPUT);
Serial.begin(9600);
}

void loop() {
  if (Serial.available()>0)
  {
      switch(Serial.read())
     {
       case '0':stopbot();
               break;
       case '1':forward();
                 break;
       case '2':backward();
                 break;
        case '3':slow();break;
        default: break;
      }
  }
 
   
//if(value=="1")
//  {forward();break;}
//else if(value=="2")
//  {backward();break;}
//else if(value=="3")
//  {slow();break;}
//else if(value=='0')
//  {stopbot();break;}
//else
//  break;
}
void forward()
 
  {
    digitalWrite(Ma1,1);
    digitalWrite(Ma2,0);
    Serial.println("Front");
  }
void backward()
 
  {

    digitalWrite(Ma1,0);
    digitalWrite(Ma2,1);
  }
void stopbot()
 
  {

    digitalWrite(Ma1,0);
    digitalWrite(Ma2,0);
  }
void slow()
  {
    analogWrite(A1 ,0);
    analogWrite(A2 ,0);
  }

