import serial
import time

arduinoData = serial.Serial("/dev/ttyACM0",9600)

# Signal Table
"""
L  | LEFT
F  | FIRE
R  | RIGHT
S  | STOP (Sends signal to stop repeating signal sent before)
"""

def left():
    print("LEFT")
    arduinoData.write(b'L')

    arduinoData.write(b'S')

def fire():
    print("FIRING")
    arduinoData.write(b'F')

    arduinoData.write(b'S')

def right():
    print("RIGHT")
    arduinoData.write(b'R')

    arduinoData.write(b'S')
