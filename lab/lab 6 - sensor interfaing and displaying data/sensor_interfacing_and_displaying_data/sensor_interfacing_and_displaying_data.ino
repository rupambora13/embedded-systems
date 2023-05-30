#include <Wire.h>
#include "SparkFunHTU21D.h"
HTU21D htu;

float a = 74.7796;
float b = 30.8351;
void setup()
{
  Serial.begin(115200);
  htu.begin();
}

void loop()
{
  float humd = htu.readHumidity();
  float temp = htu.readTemperature();
  float y1;
  float y2;
  y1 = temp + a;
  y2 = humd - b;
  
  Serial.print(" Temperature:");
  Serial.print(y1);
  Serial.println("C");
  Serial.print("Humidity:");
  Serial.print(y2);
  Serial.println ("%");
  Serial.println();
  delay(1000);
}
