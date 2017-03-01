/* In this document we read the sensor data from dht11 using arduino and transmits it to esp for use of publishing
and facilitating esp to print its its messages on serial monitor*/




#include <SoftwareSerial.h>
#include <dht.h>//library for dht temperature and humidity sensor 
char ch[20];
char se[20];
dht s;
#define datapin 5//5th pin of arduino is used for reading data from dht sensor

const byte rxPin = 2; // Wire this to Tx Pin of ESP8266
const byte txPin = 3; // Wire this to Rx Pin of ESP8266

// We'll use a software serial interface to connect to ESP8266
SoftwareSerial ESP8266 (rxPin, txPin);

void setup() {
  Serial.begin(115200);
  ESP8266.begin(115200); // Change this to the baudrate used by ESP8266
  delay(1000); // Let the module self-initialize
}

void loop() {
  String k="";
   sendtemp();//calls function void sendtemp() which transmits temp value to esp.
   sendhum();//calls function void sendhum() which transmits hum value to esp.
  
/*this while loop is used to print data from esp module on serial monitor*/

 while (ESP8266.available()>0)
   {
       for (int i=0;i<10;i++)
       {  
         ch[i] = ESP8266.read();
          if (ch[i]=='\0')
          {   break; }
           k+= ch[i];
       }
    }

   Serial.println(k);  
   
}   
/*function to read and transmit temperature to esp*/    
void sendtemp()
{
  s.read11(datapin);//reading data from sensor
   String t="temp "+String(s.temperature)+'\0';//creating a string along with sensor data to transmit
   int l=t.length();
   t.toCharArray(se,20); //conversion of string to character array for transmission to esp module
   /*for loop is used to transmit the character array to esp*/
    for (int i=0;i<l;i++)
   {
    ESP8266.write(se[i]);
   }
    delay(2000); 
   // Serial.println(t);  
  }
  void sendhum()
  {
    s.read11(datapin);//reading data from sensor
    String t="hum "+String(s.humidity)+'\0';//creating a string along with sensor data to transmit
   int l=t.length();
   t.toCharArray(se,20);  //conversion of string to character array for transmission to esp module
   /*for loop is used to transmit the character array to esp*/
   
    for (int i=0;i<l;i++)
   {
    ESP8266.write(se[i]);
   }
    delay(2000); 
  //Serial.println(t);  
}
