#include <Wire.h>
#include "SparkFunHTU21D.h"

HTU21D htu;

void setup()
{
  Serial.begin(115200);
  htu.begin();
}

void loop()
{
  float humd = htu.readHumidity();
  float temp = htu.readTemperature();
  
  Serial.print(" Temperature:");
  Serial.print(temp);
  Serial.println("C");
  Serial.print(" Humidity:");
  Serial.print(humd);
  Serial.println("%");
  Serial.println();
  delay(1000);
 
}
