import serial

arduinoData = serial.Serial("/dev/ttyACM0",9600,timeout=0)
print(f"Connected to {arduinoData.name}...")

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

