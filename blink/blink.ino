// the setup routine runs once when you press reset:
void setup() {
  // initialize the digital pin as an output.
  pinMode(LEDR, OUTPUT);
  pinMode(LEDG, OUTPUT);
  pinMode(LEDB, OUTPUT);
}

void blink(int led, unsigned long msecs = 1000) {
    digitalWrite(led, HIGH);
    delay(msecs);
    digitalWrite(led, LOW);
    delay(msecs);
}

// the loop routine runs over and over again forever:
void loop() {
    blink(LEDR);
    blink(LEDG);
    blink(LEDB);
}