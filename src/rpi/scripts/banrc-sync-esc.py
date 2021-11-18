#! /usr/bin/python3

#
# BanRC-01 - 2021
# 
# Script for initial Sync with ESC.
#  Tamiya TBLE04S beeps until it receives a PWM signal.
#  Systemd services launch at machine starts.
#
# dbanshee@gmail.com
#

from adafruit_servokit import ServoKit

# ESC channel
SERVO_CHANNEL = 9

kit = ServoKit(channels=16)
kit.continuous_servo[SERVO_CHANNEL].throttle = 0

print('BanRC-01 Sync ESC')
print('Setting default PWM Servo Throttle on channel: ' + str(SERVO_CHANNEL) + ' to SYNC with ESC and Stop Beep.')