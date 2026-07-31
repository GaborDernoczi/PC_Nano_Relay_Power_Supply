void setup() {

  Serial.begin(9600); 
  Serial.println ("Start");  

  pinMode(5, OUTPUT);     // relay
  pinMode(12, OUTPUT);    // led1
  pinMode(11, OUTPUT);    // led2
  pinMode(10, OUTPUT);    // led3

  delay(500);   
  digitalWrite(5, LOW);   // relay
  delay(500);
  digitalWrite(5, HIGH); 

}

void loop() {

  digitalWrite(12, HIGH); 
  digitalWrite(11, HIGH); 
  digitalWrite(10, HIGH);

  delay(1000);

  digitalWrite(12, LOW); 
  digitalWrite(11, LOW); 
  digitalWrite(10, LOW);

  delay(1000);

}
