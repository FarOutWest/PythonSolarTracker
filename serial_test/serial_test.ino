float voltage = 0;
float timepoint = 0;
 
void setup() {
  Serial.begin(9600);              
}
  
void loop() {
  Serial.println(voltage);
  Serial.println(timepoint); 
  analogReference(DEFAULT);
  float voltValue = analogRead(A0);
  voltage = voltValue * (5.0 / 1023.0);
  timepoint += 0.5;
  
  delay(500);                
}
