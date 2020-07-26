#include <Servo.h>

char serialData;
Servo servoX;

int xpos = 20;

// Weird Buzzing when not in servo range
// Servo Range: 20 - 180

void setup()
{
    Serial.begin(9600);
    Serial.println("Serial Connection Ready...");
    
    servoX.attach(9);
    servoX.write(90); // Set Servo Pos at Middle
    delay(15);
}

void loop()
{   
    // Only run if receiving new data
    if (Serial.available())
    {
        serialData = Serial.read();
        Serial.println(serialData);

        if (serialData == 'L')  // Turn X Servo Left
        {
          ++xpos;
          
          servoX.write(xpos);
          delay(15);
        }
        else if (serialData == 'R') // Turn X Servo Right
        {
          --xpos;

          servoX.write(xpos);
          delay(15);
        }

        Serial.print("Servo Pos: ");
        Serial.println(xpos);
    }
}
