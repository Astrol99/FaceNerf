import serial
import time

arduinoData = serial.Serial("/dev/ttyACM0",9600)

# Blink Example
"""
while True:
    arduinoData.write(b'1')
    time.sleep(1)
    arduinoData.write(b'0')
    time.sleep(1)
"""

def left():
    print("LEFT")

def right():
    print("RIGHT")

def fire():
    print("FIRING")

