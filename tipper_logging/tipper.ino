////latest version of gastippercode as of 10-09-2021
//const int  R1TipperPin = 5;  // digital in 2 (pin the reactor 1's tipper is attached to)
//int R1TipperCounter = 0;
//int R1TipperState = 0;
//int lastR1TipperState = 0;
//unsigned long previousMillis = 0;
//const long interval = 3000; //milliseconds between each print of number of tips (1000ms = 1 second), 1800000 = 30 mins
//
//
//
//void setup() {
//  //initialize serial communication at 9600 bits per second:
//  Serial.begin(9600);
//  // int R1TipperState = 0;         // current state of the switch
//  // int lastR1TipperState = 0;     // previous state of the switch switch pins as an input
//  pinMode(R1TipperPin, INPUT_PULLUP);
//  while (!Serial);
//  //Serial.println("Date & Time, R1 Gas Volume (ml), R2 Gas Volume (ml), R3 Gas Volume (ml), R4 Gas Volume (ml)");
//}
//
//
//void loop() {
//  // read the switch input pins:
//  R1TipperState = digitalRead(R1TipperPin);
//  // compare the switchState to its previous state
//  if (R1TipperState != lastR1TipperState) {
//    if (R1TipperState == HIGH) {
//      R1TipperCounter+=1;
//    }
//  }
// 
//  delay(100);
//
//  lastR1TipperState = R1TipperState;
//  unsigned long currentMillis = millis();
//  if (currentMillis - previousMillis >= interval) {
//    // save the last time you blinked the LED
//    previousMillis = currentMillis;
//    Serial.print(R1TipperCounter);
//    Serial.println(",");
//  }
//}
