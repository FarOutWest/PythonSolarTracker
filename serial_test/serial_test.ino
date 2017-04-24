int inputVoltPin = A0;
int inputAmpPin = A1;
float resistance = 1500;
 
void setup() {
  Serial.begin(9600);              
}
  
void loop() {
  int voltValue = analogRead(inputVoltPin);
  int ampValue = analogRead(inputAmpPin);    
  float voltage = voltValue * (5.0 / 1023.0);  
  float amperage = voltage / resistance;              
  Serial.println(voltage);  
  Serial.println(amperage); 
  delay(1000);                
}
