int dirL = 12;
int dirR = 13;
int brkL = 9;
int brkR = 8;
int spdL = 3;
int spdR = 11;

int pingPin = 2;

int buzzer = 6;

void setup()
{
  Serial.begin(9600);
  
  pinMode(dirL, OUTPUT); //direction pins
  pinMode(dirR, OUTPUT);
  pinMode(brkL, OUTPUT); //brake pins
  pinMode(brkR, OUTPUT);
  pinMode(spdL, OUTPUT); //speed pins
  pinMode(spdR, OUTPUT);
  pinMode(buzzer, OUTPUT);
}

void forward()
{
  digitalWrite(dirL, HIGH);
  digitalWrite(dirR, HIGH);
  digitalWrite(brkL, LOW);
  digitalWrite(brkR, LOW);
  digitalWrite(spdL, HIGH);
  digitalWrite(spdR, HIGH);
}

void backward()
{
  digitalWrite(dirL, LOW);
  digitalWrite(dirR, LOW);
  digitalWrite(brkL, LOW);
  digitalWrite(brkR, LOW);
  digitalWrite(spdL, HIGH);
  digitalWrite(spdR, HIGH);
}

void left()
{
  digitalWrite(dirL, LOW);
  digitalWrite(dirR, HIGH);
  digitalWrite(brkL, LOW);
  digitalWrite(brkR, LOW);
  digitalWrite(spdL, HIGH);
  digitalWrite(spdR, HIGH);
}

void right()
{
  digitalWrite(dirL, HIGH);
  digitalWrite(dirR, LOW);
  digitalWrite(brkL, LOW);
  digitalWrite(brkR, LOW);
  digitalWrite(spdL, HIGH);
  digitalWrite(spdR, HIGH);
}

void halt()
{
  digitalWrite(dirL, LOW);
  digitalWrite(dirR, LOW);
  digitalWrite(brkL, HIGH);
  digitalWrite(brkR, HIGH);
  digitalWrite(spdL, HIGH);
  digitalWrite(spdR, HIGH);
}

void low_slow()
{
  tone(buzzer, 1000);
  delay(200);
  noTone(buzzer);
}

void high_slow()
{
  tone(buzzer, 2500);
  delay(200);
  noTone(buzzer);
}

void low_fast()
{
  tone(buzzer, 1000);
  delay(100);
  noTone(buzzer);
}

void high_fast()
{
  tone(buzzer, 2500);
  delay(100);
  noTone(buzzer);
}

long duration, inches;
int incomingByte;

void detect()
{
  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin, LOW);

  pinMode(pingPin, INPUT);
  duration = pulseIn(pingPin, HIGH);

  inches = microsecondsToInches(duration);

  delay(100);
}

void loop()
{
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    Serial.print(incomingByte);
    if (incomingByte == 'F') {
      forward();
    }
    if (incomingByte == 'B') {
      backward();
    }
    if (incomingByte == 'L') {
      left();
    }
    if (incomingByte == 'R') {
      right();
    }
    if (incomingByte == 'H') {
      halt();
    }
    if (incomingByte == 'V') {
      low_slow();
    }
    if (incomingByte == 'X') {
      high_slow();
    }
    if (incomingByte == 'Y') {
      low_fast();
    }
    if (incomingByte == 'Z') {
      high_fast();
    }
  }
}

long microsecondsToInches(long microseconds)
{
  return microseconds / 74 / 2;
}
