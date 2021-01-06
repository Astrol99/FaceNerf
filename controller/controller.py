from gpiozero import Servo
from time import sleep
import signal

horizontal_servo = Servo(2)

print(horizontal_servo.value)