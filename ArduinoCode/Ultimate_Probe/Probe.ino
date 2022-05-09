// Variables for temperature sensor
long R1 = 100000;
long R3 = 666;



int temperaturePin = A0;
int conductancePin = A1;
int pHPin = A2;

int val = 0;

void setup() {
  Serial.begin(115200);           //  setup serial
  delay(1000);
  //R3 = termistor_resistance(100000, 0);
  //Serial.println(R3);
  //R3 = termistor_resistance(100000, 100);
  //Serial.println(R3);
  //R3 = termistor_resistance(100000, 512);
  //Serial.println(R3);
  //R3 = termistor_resistance(100000, 812);
  //Serial.println(R3);
  //R3 = termistor_resistance(100000, 1022);
  //Serial.println(R3);
}


void loop() {
  //Serial.println("Loop");
  //Serial.println(Serial.available());
  if(Serial.available() > 0) {
    char data = Serial.read();
    //Serial.println(data);
    if(data == 'A'){
      val = analogRead(temperaturePin);
      long thermistor_resistance = termistor_resistance(100000, val);
      Serial.println(thermistor_resistance);
    }
    if(data == 'B'){
      val = analogRead(conductancePin);
      long conductance = compute_conductance(220, val);
      Serial.println(conductance);
    }
    if(data == 'C'){
      val = analogRead(pHPin);
      Serial.println(val);
    }
    if(data == 'D'){
      val = analogRead(conductancePin);
      Serial.println(val);
    }
          
  }
//  val = analogRead(temperaturePin);  // read the input pin
//  R3 = compute_temperature(100000, val);
//  val = analogRead(conductancePin);  // read the input pin
//  R3 = compute_conductance(220, val);
//  delay(500);
}



long termistor_resistance(long R1, int ADCvalue){
  long R2 = 0;
  float scaleing = float(ADCvalue)/(float(1023) - float(ADCvalue));
  R2 = long(scaleing * float(R1));
  //Serial.println("\nThermistor resistance: ");
  //Serial.println(R2);
  return R2;
}

long compute_conductance(long R1, int ADCvalue){
  long R2 = 0;
  float G = 0;
  float scaleing = float(ADCvalue)/(1023.0 - float(ADCvalue));
  R2 = scaleing * R1;
  G = float(1000000)/float(R2);
  //Serial.println("\nSample resistance[Ohm]: ");
  //Serial.println(R2);
  //Serial.println("Sample Conductance[uS]: ");
  //Serial.println(G);
  return G;
}
