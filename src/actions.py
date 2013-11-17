import servo_driver
import time

# PIN DEFINITIONS
SPINE_POS = 0
SPINE_NEG = 1

EYE_POS = 0
EYE_NEG = 1

LEFT_ARM_POS = 1
LEFT_ARM_NEG = 0

RIGHT_ARM_POS = 0
RIGHT_ARM_NEG = 1

#constants determined by experiment

SPINE_SPEED = 1
SPINE_CURLED = .4

EYE__SPEED = .1
EYES_CLOSED = 1

ARM_SPEED = .2 #anything you want between 0 and 1
ARM_CURLED = .2 #how far the arm closes (you probably shouldn't mess with this)

HEAD = 2 #pin for servo

####################################################################
##                             SPINE
####################################################################

def spine_curl():
    try:
        servo_driver.setMotorSpeed(SPINE_NEG,SPINE_POS,SPINE_SPEED)
        time.sleep(SPINE_CURLED/SPINE_SPEED)
        servo_driver.setMotorSpeed(SPINE_NEG,SPINE_POS,0)

    except:
        servo_driver.setMotorSpeed(SPINE_NEG,SPINE_POS,0)

def spine_uncurl():
    try:
        servo_driver.setMotorSpeed(SPINE_NEG,SPINE_POS,-SPINE_SPEED)
        time.sleep(SPINE_CURLED/SPINE_SPEED)
        servo_driver.setMotorSpeed(SPINE_NEG,SPINE_POS,0)

    except:
        servo_driver.setMotorSpeed(SPINE_NEG,SPINE_POS,0)


####################################################################
##                              EYES
####################################################################

def close_eyes():
    try:
        servo_driver.setMotorSpeed(EYE_POS,EYE_NEG,EYE_SPEED)
        time.sleep(EYES_CLOSED/SPEED)
        servo_driver.setMotorSpeed(EYE_POS,EYE_NEG,0)

    except:
        servo_driver.setMotorSpeed(EYE_POS,EYE_NEG,0)

def open_eyes():
    try:
        servo_driver.setMotorSpeed(EYE_POS,EYE_NEG,-EYE_SPEED)
        time.sleep(EYES_CLOSED/SPEED)
        servo_driver.setMotorSpeed(EYE_POS,EYE_NEG,0)

    except:
        servo_driver.setMotorSpeed(EYE_POS,EYE_NEG,0)

def blink():
    close_eyes()
    time.sleep(.5)
    open_eyes()


####################################################################
##                              ARMS
####################################################################

def close_arms():
    try:
        servo_driver.setMotorSpeed(LEFT_ARM_POS,LEFT_ARM_NEG,-ARM_SPEED)
        time.sleep(ARM_CURLED/ARM_SPEED)
        servo_driver.setMotorSpeed(LEFT_ARM_POS,LEFT_ARM_NEG,0)

    except:
        servo_driver.setMotorSpeed(LEFT_ARM_POS,LEFT_ARM_NEG,0)

def open_arms():
    try:
        servo_driver.setMotorSpeed(LEFT_ARM_POS,LEFT_ARM_NEG,ARM_SPEED)
        time.sleep(ARM_CURLED/ARM_SPEED)
        servo_driver.setMotorSpeed(LEFT_ARM_POS,LEFT_ARM_NEG,0)

    except:
        print 10000
        servo_driver.setMotorSpeed(LEFT_ARM_POS,LEFT_ARM_NEG,0)

def hug():  #but you're so close to getting it right!
        spine_curl()
        close_arms()
        time.sleep(5)
        open_arms()
        spine_uncurl()

####################################################################
##                              HEAD
####################################################################

def headtilt():
    servo_driver.setServoPosition(HEAD,60)
    time.sleep(2)
    servo_driver.setServoPosition(HEAD,120)