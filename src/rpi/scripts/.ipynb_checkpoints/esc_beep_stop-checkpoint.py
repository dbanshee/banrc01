#! /usr/bin/python3

from adafruit_servokit import ServoKit

SERVO_CHANNEL = 9
kit = ServoKit(channels=16)
kit.continuous_servo[SERVO_CHANNEL].throttle = 0

print('Setting default PWM Servo Throttle to SYNC with ESC. Beep STOP.')