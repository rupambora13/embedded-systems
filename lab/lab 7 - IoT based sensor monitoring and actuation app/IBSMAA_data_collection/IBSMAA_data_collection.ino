#include <WiFi.h>
#include <Wire.h>
#include "Adafruit_HTU21DF.h"
#include "Adafruit_BMP085.h"

Adafruit_BMP085 bmp;


#define WIFI_NETWORK "IoT Project"
#define WIFI_PASSWORD "12345678"
#define WIFI_TIMEOUT_MS 20000
#define seaLevelPressure_hPa 1013.25

const int line1 = 26;
const int line2 = 25;
const int trigPin = 5;
const int echoPin = 18;
int duration, distance;
void connectToWiFi(){
    Serial.print("Connecting to Wifi");
    WiFi.mode(WIFI_STA);
    WiFi.begin(WIFI_NETWORK, WIFI_PASSWORD);

    unsigned long startAttemptTime = millis();

    while(WiFi.status() != WL_CONNECTED && millis() - startAttemptTime < WIFI_TIMEOUT_MS){
        Serial.print(".");
        delay(500);
      }

     if (WiFi.status() != WL_CONNECTED){
        Serial.println("Failed");
      }
     else {
        Serial.print("Connected");
        Serial.println(WiFi.localIP());
      }
  }

void setup() {
  Serial.begin(115200);
  connectToWiFi();
  pinMode(line1, OUTPUT);
  pinMode(line2, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {

 // HC-SR04
 digitalWrite(trigPin, LOW);
 delayMicroseconds(2);
 digitalWrite(trigPin, HIGH);
 delayMicroseconds(10);
 digitalWrite(trigPin, LOW);
 duration = pulseIn(echoPin, HIGH);
 distance = duration*0.034/2;
 Serial.println(distance);
 delay(100);

 // BMP180
 Serial.print("Temp = ");
 Serial.print(bmp.readTemperature());
 Serial.println(" *C");

 Serial.print("Pressure = ");
 Serial.print(bmp.readPressure());
 Serial.println(" Pa");


 Serial.print("Altitude = ");
 Serial.print(bmp.readAltitude());
 Serial.println(" meters");
 delay(100);
}
