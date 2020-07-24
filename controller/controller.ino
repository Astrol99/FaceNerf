char serialData;
int pin = 13;

void setup()
{
    pinMode(pin, OUTPUT);
    Serial.begin(9600);
    Serial.println("Serial connection Ready...");
}

void loop()
{
    if (Serial.available())
    {
        serialData = Serial.read();
        Serial.print(serialData);

        if (serialData == 'L')
        {
            digitalWrite(pin, HIGH);
        }
        else if (serialData == 'R')
        {
            digitalWrite(pin, LOW);
        }
    }
}
