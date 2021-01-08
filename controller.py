#from gpiozero import Servo
from time import sleep

#horizontal_servo = Servo(2)
servo_speed = 0.05

def left():
#    if horizontal_servo.value > -0.9:
        print("LEFT")
#        horizontal_servo.value -= servo_speed

def right():
#    if horizontal_servo.value < 0.9:
        print("RIGHT")
#        horizontal_servo.value += servo_speed

def fire():
    print("FIRE")