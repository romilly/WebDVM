const float vcc = 5.0;
const float scale = vcc / 1023; 
const int analogPins[] = {A0, A1, A2, A3, A4, A5};
const int delay_ms = 50;
const int channels = 6;

// 6 Channel DVM over serial connection


void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
  }
}


void loop() {
  // read each Analog channel, scale it, and print a formatted version to the Serial output
  for (int i = 0;i<channels;i++) {
    float v = scale * analogRead(analogPins[i]); 
    Serial.print('A');
    Serial.print(i);
    Serial.print('=');
    Serial.println(v);
    delay(delay_ms);
  }
}
