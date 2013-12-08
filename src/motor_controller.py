#!/usr/bin/env python

DEBUG = False

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
        rospy.Subscriber("locations", MotorCoordinate, self.update, queue_size=1)
        rospy.on_shutdown(self.stop)

        self.name = rospy.get_name().split('/')[-1]
        params = rospy.get_param(self.name)
        self.pos, self.neg = params['pins']
        self.low, self.high = params['limits']
        self.threshold = params['threshold']
        self.min_voltage, self.max_voltage = params['voltages']

        if DEBUG:
            rospy.loginfo("INFO: {} motor ON".format(self.name))
        
        self.goal = 50
        self.position = None
        self.old_position = 0
        self.stop()

    def goal_callback(self, data):
        if data.name == self.name:
            if DEBUG:
                rospy.loginfo("POS RECV: {}".format(self.name))
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

        # Speed must be between -1 and 1
        # Scale for battery input voltage of 7.4V
        speed = (self.max_voltage/7.4) * (delta/100.0)
        
        direction = 1
        if speed < 0:
            direction = -1

        if abs(speed) > 0:
            if abs(speed) < (self.min_voltage/7.4):
                speed = self.min_voltage/7.4
                speed *= direction

        if DEBUG:
            rospy.loginfo("{}: Delta {} Speed {}".format(self.name, delta, speed))

        servo.setMotorSpeed(self.pos, self.neg, speed)

    def update(self, data):
        if data.name == self.name:
            # remap ADC values to 0-100
            if (data.position > self.high or data.position < self.low) and DEBUG:
                rospy.logwarn("{}: Position outside of limits H:{} and L:{}!".format(self.name, 
                                                                                     self.high, 
                                                                                     self.low))

            position = 100.0 * (data.position - self.low) / (self.high - self.low)
            self.position = int(position)

            # make sure it's not a small drift
            if abs(self.position - self.old_position) > 2:
                if DEBUG:
                    rospy.loginfo("{}: {}".format(self.name, self.position))

                self.old_position = self.position
                self.move_to(self.goal)

                
    def stop(self):
        if DEBUG:
            rospy.loginfo("INFO: stopping motor {}".format(self.name))

        if self.position:
            self.goal = self.position
        servo.setMotorSpeed(self.pos, self.neg, 0)

if __name__ == '__main__':
    Motor()
    rospy.spin()
