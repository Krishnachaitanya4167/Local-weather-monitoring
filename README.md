# Local-weather-monitoring
/*This system works on a frame work which reads sensor data from arduino and transmits to server via Esp8266-wifi module.

file-1:code_for_ard_temp_data.ino

     In this  file the values of temperature and humidity are read from DHT11 sensor using arduino the values are then transmitted to esp8266-wifi-module.
     the arduino transmits data via software serial to Esp8266 and recieves data using software serial to print the data that is being published in  file-2.
     
 file-2:sending sensordata from arduino to server.ino
     
     This file receives data from arduino and publishes the data to server and write backs the data being published to Arduino for the purpose of viewing on serial monitor.
     
 NOTE:
 1)The procedure for implementing the project is mentioned in the readme file included in repository.
 2)The libraries that are used in this project are taken from
     a)pubsub-client library---https://github.com/knolleary/pubsubclient
     b)DHT11-library-----------https://github.com/adafruit/DHT-sensor-library  //a few modifications are done as per our project requirements in dht11 library.
     
     
For more details:Refer to

1)

2)
