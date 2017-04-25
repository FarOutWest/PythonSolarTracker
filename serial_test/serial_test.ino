float resistance = 1.5;
float voltage = 0;
float amperage = 0;
 
void setup() {
  Serial.begin(9600);              
}
  
void loop() {
  Serial.println(voltage); 
  Serial.println(amperage); 
  
  analogReference(DEFAULT);
  float voltValue = analogRead(A0);
  
  voltage = voltValue * (5.0 / 1023.0);  
  amperage = voltage / resistance; 
  
  delay(1000);                
}
