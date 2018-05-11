from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

mh = Adafruit_MotorHAT(addr=0x60)
motor_1 = mh.getMotor(1, 3) #setting right motors
motor_2 = mh.getMotor(2, 4) #setting left motors

def forwards(motor_1, motor_2): #moving foward
    while True:
        motor_1.setSpeed(150)
        motor_1.run(Adafruit_MotorHAT.FORWARD)
        motor_2.setSpeed(150)
        motor_2.run(Adafruit_MotorHAT.FORWARD)

def backwards(motor_1, motor_2): #moving backward
    while True:
        motor_1.setSpeed(100)
        motor_1.run(Adafruit_MotorHAT.BACKWARD)
        motor_2.setSpeed(100)
        motor_2.run(Adafruit_MotorHAT.BACKWARD)

def turn_left(motor_1, motor_2): #turning left over distance
    while True:
        motor_1.setSpeed(150)
        motor_1.run(Adafruit_MotorHAT.FORWARD)
        motor_2.setSpeed(100)
        motor_2.run(Adafruit_MotorHAT.FORWARD)

def turn_right(motor_1, motor_2): #turning right over distance
    while True:
        motor_1.setSpeed(100)
        motor_1.run(Adafruit_MotorHAT.FORWARD)
        motor_2.setSpeed(150)
        motor_2.run(Adafruit_MotorHAT.FORWARD)

def turn_left_still(motor_1, motor_2): #turning left on the spot
    while True:
        motor_1.setSpeed(150)
        motor_1.run(Adafruit_MotorHAT.FORWARD)
        motor_2.setSpeed(150)
        motor_2.run(Adafruit_MotorHAT.BACKWORD)

def turn_right_still(motor_1, motor_2): #turning right on the spot
    while True:
        motor_1.setSpeed(150)
        motor_1.run(Adafruit_MotorHAT.BACKWARD)
        motor_2.setSpeed(150)
        motor_2.run(Adafruit_MotorHAT.FORWARD)

#instructions for the user
print('''Turn left = a
turn right = d
foward = w
backwards = s
turning left on spot = q
turning right on spot = e''')

while True: #Main program
    user_input = input()
    if user_input == "a":
        turn_left(motor_1, motor_2)
        print("left")
    elif user_input == "d":
        turn_right(motor_1, motor_2)
    elif user_input == "w":
        forwards(motor_1, motor_2)
        print("forwards")
    elif user_input == "s":
        backwards(motor_1, motor_2)
        print("backwards")
    elif user_input == "q":
        turn_left_still(motor_1, motor_2)
        print("left")
    elif user_input == "e":
        turn_right_still(motor_1, motor_2)
        print("right")
