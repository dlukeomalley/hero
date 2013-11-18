#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import RPi.GPIO as GPIO

# Initialize the GPIO pin.  One pin will be used to turn
# all motors on and off at once.  The A and B pins are 
# used to move the motor clockwise, counter clockwise,
# or stationary.
# GPIO.setmode(GPIO.BCM)
# enablePin = 22
# GPIO.setup(enablePin, GPIO.OUT)

# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=True)

# Edit these values to correspond to your brand of servo.
servoMin = 104  # Min pulse length out of 4096, 0 degrees.
servoMax = 521  # Max pulse length out of 4096, 180 degrees.
servoSpan = servoMax - servoMin

# Sets PWM frequency to 50. If you change this, you need to
# change the servo values above. Do not set it above 60 Hz,
# as this can damage the servos.
pwm.setPWMFreq(50)

# Channel is the channel on the adafruit PWM board. Position
# is measured in degrees between 0 and 180.
def setServoPosition(channel, position):
  if position > 180:
    position = 180
  if position < 0:
    position = 0
  pulse = position * servoSpan/180 + servoMin
  pwm.setPWM(channel, 0, pulse)

# Turns all of the motors on, though they have a starting speed
# of zero. This method must be called at the top of any program.
# def motorsOn():
#   GPIO.output(enablePin, True)

# # Turns all of the motors off. Use this to save power or end
# # a program.  To turn an individual motor off, set its speed to
# # zero.
# def motorsOff():
#   GPIO.output(enablePin, False)

# Motors take up two channels on the adafruit PWM board. The
# speed variable should be -1 for counter clockwise and 1 for 
# clockwise.  Speed goes from 0 to 1.
def setMotorSpeed(channelA, channelB, speed):
  if speed > 1:
    speed = 1
  if speed < -1:
    speed = -1
  pulse = int(abs(speed)*4095)
  if speed < 0:
    pwm.setPWM(channelA, 0, pulse)
    pwm.setPWM(channelB, 0, 0)
  else:
    pwm.setPWM(channelA, 0, 0)
    pwm.setPWM(channelB, 0, pulse)
