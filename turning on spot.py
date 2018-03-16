from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

mh = Adafruit_MotorHAT(addr=0x60)
motor_1 = mh.getMotor(1, 3)
motor_2 = mh.getMotor(2, 4)


def turn_left(motor_1, motor_2):
    while True:
        motor_1.setSpeed(150)
        motor_1.run(Adafruit_MotorHAT.FORWARD)
        motor_2.setSpeed(150)
        motor_2.run(Adafruit_MotorHAT.BACKWORD)

def turn_right(motor_1, motor_2):
    while True:
        motor_1.setSpeed(150)
        motor_1.run(Adafruit_MotorHAT.BACKWARD)
        motor_2.setSpeed(150)
        motor_2.run(Adafruit_MotorHAT.FORWARD)
while True:
    user_input = input()
    if user_input == "a":
        turn_left(motor_1, motor_2)
        print("left")
    elif user_input == "d":
        turn_right(motor_1, motor_2)
        print("right")
