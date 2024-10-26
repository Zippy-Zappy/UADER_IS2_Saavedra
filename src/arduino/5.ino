void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  int i;

  for (i = 0; i < 3; i++) {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(800);
    digitalWrite(LED_BUILTIN, LOW);
    delay(800);
  }

  delay(2400);

  for (i = 0; i < 3; i++) {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(2400);
    digitalWrite(LED_BUILTIN, LOW);
    delay(2400);
  }

  delay(2400);

  for (i = 0; i < 3; i++) {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(800);
    digitalWrite(LED_BUILTIN, LOW);
    delay(800);
  }

  delay(7200);
}
