import servo_driver
import time
import random

# PIN DEFINITIONS
# MOTOR DEFINITIONS ARE (POS_PIN, NEG_PIN)
TAIL_M = (4, 5)
TAIL_SPEED = 1
TAIL_CURLED = .4

EYE_M = (6, 7)
EYE_SPEED = .1
EYES_CLOSED = 1

LEFT_ARM_M = (0, 1)
RIGHT_ARM_M = (2, 3)
ARM_SPEED = .2
ARM_CURLED = .2 #how far the arm closes (you probably shouldn't mess with this)

PUR_M = (8,9)
HEAD_SERVO = 10

####################################################################
##                      HELPER FUNCTIONS
####################################################################

def set_motor(motor, speed):
    (pos, neg) = motor
    servo_driver.setMotorSpeed(neg, pos, speed)

def stop_motor(motor):
    (pos, neg) = motor
    servo_driver.setMotorSpeed(neg, pos, 0)

####################################################################
##                             SPINE
####################################################################

def spine_curl():
    set_motor(TAIL_M, TAIL_SPEED)
    time.sleep(SPINE_CURLED/SPINE_SPEED)
    stop_motor(TAIL_M)

def spine_uncurl():
    set_motor(TAIL_M, -TAIL_SPEED)
    time.sleep(SPINE_CURLED/SPINE_SPEED)
    stop_motor(TAIL_M)


####################################################################
##                              EYES
####################################################################

def eyes_close():
    set_motor(EYE_M, EYE_SPEED)
    time.sleep(EYES_CLOSED/EYE_SPEED)
    stop_motor(EYE_M)

def eyes_open():
    set_motor(EYE_M, -EYE_SPEED)
    time.sleep(EYES_CLOSED/EYE_SPEED)
    stop_motor(EYE_M)


####################################################################
##                              ARMS
####################################################################

def left_arm_close():
    set_motor(LEFT_ARM_M, ARM_SPEED)
    time.sleep(ARM_CURLED/ARM_SPEED)
    set_motor(LEFT_ARM_M)

def left_arm_open():
    set_motor(LEFT_ARM_M, -ARM_SPEED)
    time.sleep(ARM_CURLED/ARM_SPEED)
    set_motor(LEFT_ARM_M)

def right_arm_close():
    set_motor(RIGHT_ARM_M, ARM_SPEED)
    time.sleep(ARM_CURLED/ARM_SPEED)
    set_motor(RIGHT_ARM_M)

def right_arm_open():
    set_motor(RIGHT_ARM_M, -ARM_SPEED)
    time.sleep(ARM_CURLED/ARM_SPEED)
    set_motor(RIGHT_ARM_M)

def arms_open():
    left_arm_open()
    right_arm_open()

def arms_close():
    left_arm_close()
    right_arm_close()

####################################################################
##                              HEAD
####################################################################

def headtilt(angle):
    # TODO: map correctly
    angle += 90
    servo_driver.setServoPosition(HEAD, angle)


####################################################################
##                       HIGH LEVEL ACTIONS
####################################################################

def none():
    return

def blink():
    eyes_close()
    time.sleep(.25)
    eyes_open()

def hug():  #but you're so close to getting it right!
    arms_close()
    tail_curl()
    time.sleep(5)
    arms_open()
    tail_uncurl()

def wave(arm):
    for i in range(3):    
        if "LEFT":
            left_arm_close()
            left_arm_open()
        elif "RIGHT":
            right_arm_close()
            left_arm_open()

def headshake():
    headtilt(-20)
    time.sleep()
    headtilt(20)
    time.sleep()
    headtilt(0)

def pur():
    set_motor(PUR_M, PUR_SPEED)
    time.sleep(random.uniform(0.5, 1.5))
    stop_motor()

# Basic "unit" tests
# blink()
# hug()
# wave("LEFT")
# wave("RIGHT")
# headshake()
# pur()

