#!/usr/bin/env python

import herolib.moves
from herolib.external import servo

import roslib; 
roslib.load_manifest('hero')
import rospy

# TODO: Create MotorCoordinate
from hero.msg import MotorCoordinate
    
class Motor:
    # TODO: Include max_voltage so that avg voltage from PWM doesn't exceed ratings of motor
    def __init__(self, name, pins, limits, max_voltage=6, threshold=5):
        # pins (pos, neg), limits (low, high)
        self.name = name
        self.pos, self.neg = pins
        self.low, self.high = limits
        
        # how close we have to be to the goal before we stop
        self.threshold = threshold

        self.goal = None
        self.position = None

        # move motor to starting place
        self.move_to(0)

        # Name node, subscribe to positions topic, and setup shutdown handle
        rospy.init_node("{}_motor".format(name.lower()))
        rospy.Subscriber("goals", MotorCoordinate, self.goal_callback)
        rospy.Subscriber("locations", MotorCoordinate, self.update)
        rospy.on_shutdown(self.stop)

    def goal_callback(self, data):
        if data.name == self.name:
            self.move_to(data.position)

    def move_to(position):
        # position hasn't been reported yet
        if self.position == None:
            return

        self.goal = position
        delta = self.goal - self.position

        # Stop motor from wiggling back and forth near goal
        if abs(delta) <= self.threshold:
            delta = 0

        # Speed must be between -1 and 1
        servo.setMotorSpeed(self.pos, self.neg, delta/100.0)

    def update(self, data):
        if data.name == self.name:
            # to convert from 0-100 -> range
            # position = self.low + (self.high - self.low)*data[self.name]/100.0
            
            # to convert from range -> 0-100
            position = 100.0 * (data.position - self.low) / (self.high - self.low)
            
            self.position = int(position)
            self.move_to(self.goal)

    def stop(self):
        servo.setMotorSpeed(self.pos, self.neg, 0)

if __name__ == '__main__':

    # DEFINITIONS
    HEAD_PINS = (0,1)
    LARM_PINS = (2,3)
    RARM_PINS = (4,5)
    BLINK_PINS = (6,7)

    HEAD_LIMITS = (0, 1024)
    LARM_LIMITS = (0, 1024)
    RARM_LIMITS = (0, 1024)
    BLINK_LIMITS = (0, 1024)

    # CREATE MOTOR NODES
    # TODO: Do we want analog channel to report by channel or title?
    Motor("HEAD", HEAD_PINS, HEAD_LIMITS)
    Motor("LARM", LARM_PINS, LARM_LIMITS)
    Motor("RARM", RARM_PINS, RARM_LIMITS)
    Motor("BLINK", BLINK_PINS, BLINK_LIMITS)

    # TODO: Pur motor doesn't conform to our model
    Motor("PUR", PUR_PINS, PUR_LIMITS)

    rospy.spin()