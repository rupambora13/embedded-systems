#include <WiFi.h>
#include <Wire.h>

#define WIFI_NETWORK "IoT Project"
#define WIFI_PASSWORD "12345678"
#define WIFI_TIMEOUT_MS 20000

const int trigPin = 5;
const int echoPin = 18;
int duration, distance;
int previousDistance = 0;
WiFiServer server(80);

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
        //digitalWrite(LED_BUILTIN, HIGH);
      }
  }


void setup() {
  Serial.begin(115200);
  connectToWiFi();
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
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
 if (distance != previousDistance) {
    // Data has changed, process the new distance value
    Serial.print(distance);
    Serial.println(" cm");
    // Update the previous distance
    previousDistance = distance;
  }
  delay(100);
 WiFiClient client = server.available();
  if (client) {
    while (client.connected()) {
      String data = String(distance); // Replace with your sensor data source
      client.println(data);
      delay(1000);
      
      String request = client.readStringUntil('\n');
      if (request == "HIGH") {
        ledState = HIGH;
      } else if (request == "LOW") {
        ledState = LOW;
      }

      digitalWrite(ledPin, ledState);

      client.println(ledState == HIGH ? "LED ON" : "LED OFF");
      delay(1000);
      
    }
    client.stop();
  }
 
}
