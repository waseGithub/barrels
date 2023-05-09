#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into digital pin 2 on the Arduino
#define ONE_WIRE_BUS 3

// Setup a oneWire instance to communicate with any OneWire device
OneWire oneWire(ONE_WIRE_BUS);  

// Pass oneWire reference to DallasTemperature library
DallasTemperature sensors(&oneWire);

int barrel_id = 1;
int deviceCount = 2;
float tempC;
const int  R1TipperPin = 14;  // digital in 2 (pin the reactor 1's tipper is attached to)
int R1TipperCounter = 0;
int R1TipperState = 1;
int lastR1TipperState = 1;
unsigned long previousMillis = 0;
const long interval = 200;


void setup(void)
{
  sensors.begin();  // Start up the library
  Serial.begin(9600);
  pinMode(R1TipperPin, INPUT_PULLUP);
  deviceCount = sensors.getDeviceCount();
}

void loop(void)
{ 

    R1TipperState = digitalRead(R1TipperPin);
  // compare the switchState to its previous state
  if (R1TipperState != lastR1TipperState) {
    if (R1TipperState == HIGH) {
      R1TipperCounter+=1;
    }
  }
  lastR1TipperState = R1TipperState;




  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
  Serial.print("-*");
  Serial.print(",");
  Serial.print(barrel_id);
  Serial.print(",");
  sensors.requestTemperatures(); 
  
  // Display temperature from each sensor
  for (int i = 0;  i < 2;  i++)
  {
    tempC = sensors.getTempCByIndex(i);
    Serial.print(tempC);
    Serial.print(",");
  }
  Serial.print(R1TipperCounter);
  Serial.print(",");
  Serial.println("*-");  
  previousMillis = currentMillis;
  }
  

  delay(2);
}
