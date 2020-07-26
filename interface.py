import serial
import time

arduinoData = serial.Serial("/dev/ttyACM0",9600)

# Signal Table
"""
L  | LEFT
F  | FIRE
R  | RIGHT
"""

# Continously move in to 
def left():
    print("LEFT")
    arduinoData.write(b'L')

def fire():
    print("FIRING")
    arduinoData.write(b'F')

def right():
    print("RIGHT")
    arduinoData.write(b'R')
