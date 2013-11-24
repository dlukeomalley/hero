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
    def __init__(self): 
        rospy.init_node("motor_node", anonymous=True)
        rospy.Subscriber("goals", MotorCoordinate, self.goal_callback)
        rospy.Subscriber("locations", MotorCoordinate, self.update)
        rospy.on_shutdown(self.stop)

        self.name = rospy.get_name().split('/')[-1]
        params = rospy.get_param(self.name)
        self.pos, self.neg = params['pins']
        self.low, self.high = params['limits']
        self.threshold = params['threshold']

        rospy.loginfo("INFO: motor {} ON".format(self.name))
        
        self.goal = 0
        self.position = None
        self.stop()

    def goal_callback(self, data):
        if data.name == self.name:
            self.move_to(data.position)

    def move_to(self, position):
        # position hasn't been reported yet
        if self.position == None:
            return

        self.goal = position
        delta = self.goal - self.position

        # Stop motor from wiggling back and forth near goal
        if abs(delta) <= self.threshold:
            delta = 0

        rospy.loginfo("INFO: motor {} moving to {}".format(self.name, self.goal))
        # Speed must be between -1 and 1
        servo.setMotorSpeed(self.pos, self.neg, delta/100.0)

    def update(self, data):
        if data.name == self.name:
            # remap ADC values to 0-100
            position = 100.0 * (data.position - self.low) / (self.high - self.low)
            self.position = int(position)

            rospy.loginfo("INFO: motor {} @ {}".format(self.name, self.position))
            self.move_to(self.goal)

    def stop(self):
        servo.setMotorSpeed(self.pos, self.neg, 0)

if __name__ == '__main__':
    Motor()
    rospy.spin()
