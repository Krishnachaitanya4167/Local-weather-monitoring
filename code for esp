 #include <ESP8266WiFi.h>
#include <PubSubClient.h>//library to use mqtt protocol from arduino ide
char ch[20];
char hu[20];
char se[20];
 String k="";
  String message="";

const char *ssid = "your network name";
const char *password = "your password";
const char* mqtt_server = "ip address of your server";


const char* clientID = "esp8266";//name of your device
const char* outTopic = "output";//outtopic to be used by mqtt broker
const char* inTopic = "input";//intopic to be used by mqtt broker


WiFiClient espClient;
PubSubClient client(espClient);
char msg[50];


void setup_wifi() {

  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);//function used to connect to your network

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());//prints iipaddress of the wifi module we are using
}

void reconnect() {
 // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect(clientID)) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish(outTopic, clientID);
      // ... and resubscribe
      client.subscribe(inTopic);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}   
   
void callback(char* topic, byte* payload, unsigned int length) {
  payload[length] = '\0'; 
 message = (char*)payload;//message recieved from server
  
 if(message=="temp")
 {

 publish();//publish is a function that handles messages or data that needs to be published

}
 
}

void setup() {
  Serial.begin(115200);//initialize baud rate for serial communication of esp
  setup_wifi();//fuction used to connect to your network
  client.setServer(mqtt_server, 1883);//details of server and port number you use
  client.setCallback(callback); //call back function
}

void loop() { 
/*if server gets disconnected reconnect() functions helps us to connect again*/
  if (!client.connected()) {
    reconnect();
  }
   client.loop();//it checks whether payload is recieved if recieved it executes void callback function only once
  
}

void publish()
{
  while(Serial.available()>0)//while data is recieved from arduino
    {
     String k="";
    for (int i=0;i<20;i++)
   {  
   
    ch[i] = Serial.read();//reading character by character from arduino
    if (ch[i]=='\0')
     {   break; }//read untill a null character is encountered
     k+= ch[i];
} 
String a="device1 "+k;//append name of the device along with dat recievd from arduino
int l=a.length();

a.toCharArray(se,l+1);//convert the data we need to publish into character array

for (int i=0;i<l+1;i++)/*for loop used to print on the serial monitor what data is going to be published*/
   {
    Serial.write(se[i]);
   }
client.publish(outTopic,se);//publish the character array of data after processing
delay(2000);
  } 
}

/*since void callback() function is executed only once when payload is received 
for continous transmission of sensor data we need to include the process in message handling only i.e function publish() in this case*/
//Note:client.publish command can only publish character array based on the outtopic we mention.
