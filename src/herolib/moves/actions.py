from ..external import servo

import time
import random

# PIN DEFINITIONS
# MOTOR DEFINITIONS ARE (POS_PIN, NEG_PIN)
TAIL_M = (6, 7)
TAIL_SPEED = 1
TAIL_CURLED = .5

EYE_M = (10, 11)
EYE_SPEED = .15
EYES_CLOSED = .3

LEFT_ARM_M = (8, 9)
RIGHT_ARM_M = (1, 0)
ARM_SPEED = .5
ARM_CURLED = 1

PUR_M = (2, 3)
PUR_SPEED = .4

HEAD_SERVO = 12

####################################################################
##                      HELPER FUNCTIONS
####################################################################

def set_motor(motor, speed):
    (pos, neg) = motor
    servo.setMotorSpeed(neg, pos, speed)

def stop_motor(motor):
    (pos, neg) = motor
    servo.setMotorSpeed(neg, pos, 0)

def stop_all():
    stop_motor(TAIL_M)
    stop_motor(EYE_M)
    stop_motor(LEFT_ARM_M)
    stop_motor(RIGHT_ARM_M)
    stop_motor(PUR_M)

####################################################################
##                             SPINE
####################################################################

def tail_curl():
    set_motor(TAIL_M, TAIL_SPEED)
    time.sleep(1)
    stop_motor(TAIL_M)

def tail_uncurl():
    set_motor(TAIL_M, -TAIL_SPEED)
    time.sleep(TAIL_CURLED/TAIL_SPEED)
    stop_motor(TAIL_M)


####################################################################
##                              EYES
####################################################################

EYE_TIME = .4

def eyes_close():
    set_motor(EYE_M, EYE_SPEED)
    time.sleep(EYE_TIME)
    stop_motor(EYE_M)

def eyes_open():
    set_motor(EYE_M, -EYE_SPEED)
    time.sleep(EYE_TIME + .05)
    stop_motor(EYE_M)


####################################################################
##                              ARMS
####################################################################

def left_arm_close():
    set_motor(LEFT_ARM_M, ARM_SPEED)
    time.sleep(ARM_CURLED/ARM_SPEED)
    stop_motor(LEFT_ARM_M)

def left_arm_open():
    set_motor(LEFT_ARM_M, -ARM_SPEED)
    time.sleep(ARM_CURLED/ARM_SPEED)
    stop_motor(LEFT_ARM_M)

def right_arm_close():
    set_motor(RIGHT_ARM_M, ARM_SPEED)
    time.sleep(ARM_CURLED/ARM_SPEED)
    stop_motor(RIGHT_ARM_M)

def right_arm_open():
    set_motor(RIGHT_ARM_M, -ARM_SPEED)
    time.sleep(ARM_CURLED/ARM_SPEED)
    stop_motor(RIGHT_ARM_M)

def arms_open():
    set_motor(LEFT_ARM_M, -ARM_SPEED)
    set_motor(RIGHT_ARM_M, -ARM_SPEED)
    time.sleep(ARM_CURLED/ARM_SPEED)
    stop_motor(LEFT_ARM_M)
    stop_motor(RIGHT_ARM_M)

def arms_close():
    set_motor(LEFT_ARM_M, ARM_SPEED)
    set_motor(RIGHT_ARM_M, ARM_SPEED)
    time.sleep(ARM_CURLED/ARM_SPEED)
    stop_motor(LEFT_ARM_M)
    stop_motor(RIGHT_ARM_M)


####################################################################
##                              HEAD
####################################################################

def headtilt(angle):
    # TODO: map correctly
    angle += 90
    servo.setServoPosition(HEAD_SERVO, angle)


####################################################################
##                       HIGH LEVEL ACTIONS
####################################################################

def none():
    return

def blink():
    eyes_close()
    time.sleep(.1)
    eyes_open()

def tail_wag():
    for x in range(random.randint(2,5)):
        tail_curl()
        tail_uncurl()

def hug():  #but you're so close to getting it right!
    arms_close()
    tail_wag()
    time.sleep(random.randint(1,2))
    arms_open()

def wave(arm):
    for i in range(random.randint(1,3)):    
        if arm == "LEFT":
            left_arm_close()
            left_arm_open()
        elif arm == "RIGHT":
            right_arm_close()
            right_arm_open()

def left_wave():
    wave("LEFT")

def right_wave():
    wave("RIGHT")

def headshake():
    eyes_close()
    headtilt(random.randint(10, 30))
    time.sleep(1)
    headtilt(random.randint(-30, -10))
    eyes_open()
    time.sleep(1)
    headtilt(0)

def pur():
    set_motor(PUR_M, PUR_SPEED)
    time.sleep(random.uniform(0.5, 1.5))
    stop_motor(PUR_M)

def left_hand_grab():
    headtilt(-30)
    pur()

def right_hand_grab():
    headtilt(30)
    pur()

def test():
    left_arm_close()
    right_arm_close()
    pur()
    tail_wag()
    blink()
    headshake()

# Basic "unit" tests
# blink()
# hug()
# wave("LEFT")
# wave("RIGHT")
# headshake()
# pur()

# test()
