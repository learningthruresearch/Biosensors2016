/*      The Wires
    For the first DHT11 sensor :
  * The pin 1 is connected to the pin 5V of the Arduino MEGA 2560
  * The pin 2 is connected to the digital pin 5 of the Arduino MEGA 2560
  * The pin 3 is connected to nothing
  * The pin 4 is connected to the pin GND of the Arduino MEGA 2560
  
    For the second DHT11 sensor :
  * The pin 1 is connected to the pin 5V of the Arduino MEGA 2560
  * The pin 2 is connected to the digital pin 6 of the Arduino MEGA 2560
  * The pin 3 is connected to nothing
  * The pin 4 is connected to the pin GND of the Arduino MEGA 2560
*/

#include "DHT.h" //Call the DHT library for the sensor

#define DHTPIN1 5     //Define the pin of the first DHT11 sensor
#define DHTPIN2 6     //Define the pin of the first DHT11 sensor

#define DHTTYPE DHT11   //Define the type of the sensor

DHT dht1(DHTPIN1, DHTTYPE); //Define the fonction for the first sensor
DHT dht2(DHTPIN2, DHTTYPE); //Define the fonction for the second sensor

void setup() 
{
    Serial.begin(9600); //Initialize the Serial
    Serial.println("Humidity (%) & Temperature (C) Sensor1 and Humidity (%) & Temperature (C) Sensor2"); //Tell what the data are
    dht1.begin(); //Initialize the first Sensor
    dht2.begin(); //Initialize the second Sensor
}

void loop() 
{
    float h1 = dht1.readHumidity(); //Take the humidity of the first sensor
    float t1 = dht1.readTemperature(); //Take the temperature of the first sensor
    float h2 = dht2.readHumidity(); //Take the humidity of the second sensor
    float t2 = dht2.readTemperature(); //Take the temperature of the second sensor
    //Print all of it on the Serial
    Serial.print(h1);
    Serial.print("\t");
    Serial.print(t1);
    Serial.print("\t");
    Serial.print(h2);
    Serial.print("\t");
    Serial.println(t2);
    delay(500); //Wait 500ms before the next measurement
}
