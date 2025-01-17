#define TRIG_PIN 12
#define ECHO_PIN 13
#define LED1_PIN 2
#define LED2_PIN 3
#define LED3_PIN 4
#define LED4_PIN 5
//ultrasonic
void setup() {
  Serial.begin(9600);
  
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  
  pinMode(LED1_PIN, OUTPUT);
  pinMode(LED2_PIN, OUTPUT);
  pinMode(LED3_PIN, OUTPUT);
  pinMode(LED4_PIN, OUTPUT);
}

void loop() {
  long duration, distance;
  
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  
  duration = pulseIn(ECHO_PIN, HIGH);
  distance = duration * 0.034 / 2;
  
  // Clear all LEDs
  digitalWrite(LED1_PIN, LOW);
  digitalWrite(LED2_PIN, LOW);
  digitalWrite(LED3_PIN, LOW);
  digitalWrite(LED4_PIN, LOW);
  
  // Light LEDs based on distance
  if (distance < 10) {
    digitalWrite(LED4_PIN, HIGH);
  } else if (distance < 20) {
    digitalWrite(LED3_PIN, HIGH);
  } else if (distance < 30) {
    digitalWrite(LED2_PIN, HIGH);
  } else if (distance < 40) {
    digitalWrite(LED1_PIN, HIGH);
  }
  
  // Print the distance for debugging
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  delay(500);
}