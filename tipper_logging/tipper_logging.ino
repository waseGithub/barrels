//#include <OneWire.h>
//#include <DallasTemperature.h>
//
//
//
//
//#define ONE_WIRE_BUS 3
//OneWire oneWire(ONE_WIRE_BUS);
//DallasTemperature sensors(&oneWire);
//
//
//int barrel_id = 1;
//
//
////latest version of gastippercode as of 10-09-2021
//const int  R1TipperPin = 14;  // digital in 2 (pin the reactor 1's tipper is attached to)
//int R1TipperCounter = 0;
//int R1TipperState = 1;
//int lastR1TipperState = 1;
//unsigned long previousMillis = 0;
//const long interval = 3000; //milliseconds between each print of number of tips (1000ms = 1 second), 1800000 = 30 mins
//
//
//
//
//
//
//void setup() {
//  //initialize serial communication at 9600 bits per second:
//  Serial.begin(9600);
//  pinMode(R1TipperPin, INPUT_PULLUP);
//  while (!Serial);
//}
//
//
//
//
//
//
//
//
//void loop() {
////  add_id();
////   
//  // read the switch input pins:
//  R1TipperState = digitalRead(R1TipperPin);
//  // compare the switchState to its previous state
//  if (R1TipperState != lastR1TipperState) {
//    if (R1TipperState == HIGH) {
//      R1TipperCounter+=1;
//    }
//  }
// 
//
//  lastR1TipperState = R1TipperState;
//
//
//
//  unsigned long currentMillis = millis();
//  if (currentMillis - previousMillis >= interval) {
//  sensors.requestTemperatures(); 
//  Serial.print(barrel_id);
//  Serial.print(",");
//  Serial.print(sensors.getTempCByIndex(0));
//  Serial.print(",");
//  Serial.println(R1TipperCounter);
//  previousMillis = currentMillis;
//  }
//
//  
//  delay(10);
//
//  
//
// 
//
//
//
//
//}
