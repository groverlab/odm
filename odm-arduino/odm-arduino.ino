void setup() {
  analogReadResolution(14);
  Serial.begin(2000000);
}

void loop() {
  Serial.println(analogRead(A1));
}
