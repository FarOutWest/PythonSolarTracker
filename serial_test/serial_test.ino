float voltage = 0.0;
float amperage = 0.0;
 
void setup() {
  Serial.begin(9600);              
}
  
void loop() {
  Serial.println(voltage);
  Serial.println(amperage); 
  
  analogReference(DEFAULT);
  float voltValue = analogRead(A0);
  float ampValue = analogRead(A1);
  
  voltage = voltValue * (5.0 / 1023.0);
  amperage = ampValue * (5.0 / 1023.0);
  amperage = (amperage + voltage) / 10;
  
  delay(500);                
}
