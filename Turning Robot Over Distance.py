from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor # Imports Adafruit

import time # This is required to include time module
import atexit # cleans up a function 

mh = Adafruit_MotorHAT(addr=0x60) 
motor_1 = mh.getMotor(1, 3) # front motors 
motor_2 = mh.getMotor(2, 4) # back motors 


def turn_left(motor_1, motor_2): # function for left turn over distance
    while True:
        motor_1.setSpeed(150) # sets right motor to 150
        motor_1.run(Adafruit_MotorHAT.FORWARD) # motor 1 runs
        motor_2.setSpeed(100) #sets left motor to 100
        motor_2.run(Adafruit_MotorHAT.FORWARD) # motor 2 runs 

def turn_right(motor_1, motor_2): # function for right turn over distance
    while True:
        motor_1.setSpeed(100) # sets right motor to 100
        motor_1.run(Adafruit_MotorHAT.FORWARD) # motor 1 runs
        motor_2.setSpeed(150) # sets left motor to 150
        motor_2.run(Adafruit_MotorHAT.FORWARD) # motor 2 runs 
while True:
    user_input = input() 
    if user_input == "a":
        turn_left(motor_1, motor_2) # if user presses "a" run turn_letf function 
        print("left")
    elif user_input == "d":
        turn_right(motor_1, motor_2) # if user presses "d" run turn_right function 
        print("right")
