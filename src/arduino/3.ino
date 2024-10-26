void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  int i;

  for (i = 0; i < 3; i++) {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(400);
    digitalWrite(LED_BUILTIN, LOW);
    delay(400);
  }

  delay(1200);

  for (i = 0; i < 3; i++) {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1200);
    digitalWrite(LED_BUILTIN, LOW);
    delay(1200);
  }

  delay(1200);

  for (i = 0; i < 3; i++) {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(400);
    digitalWrite(LED_BUILTIN, LOW);
    delay(400);
  }

  delay(3600);
}
