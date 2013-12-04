#!/usr/bin/env python

DEBUG=False

if not DEBUG:
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

        rospy.loginfo("INFO: motor {} on".format(self.name))
        
        self.goal = 0
        self.position = None
        self.old_position = 0
        self.stop()

    def goal_callback(self, data):
        if data.name == self.name:
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

        if DEBUG:
            return

        # Speed must be between -1 and 1
        speed = delta/100.0
        rospy.loginfo("{}: Delta {} Speed {}".format(self.name, delta, speed))
        servo.setMotorSpeed(self.pos, self.neg, speed)

    def update(self, data):
        if data.name == self.name:
            # remap ADC values to 0-100
            if data.position > self.high or data.position < self.low:
                rospy.logwarn("{}: Position outside of limits H:{} and L:{}!".format(self.name, 
                                                                                     self.high, 
                                                                                     self.low))

            position = 100.0 * (data.position - self.low) / (self.high - self.low)
            self.position = int(position)

            #rospy.loginfo("INFO: motor {} @ {}".format(self.name, self.position))

            # make sure it's not a small drift
            if abs(self.position - self.old_position) > 2:
                rospy.loginfo("{}: {}".format(self.name, self.position))
                self.old_position = self.position
                self.move_to(self.goal)

                
    def stop(self):
        rospy.loginfo("INFO: stopping motor {}".format(self.name))

        if DEBUG:
            return

        if self.position:
            self.goal = self.position
        servo.setMotorSpeed(self.pos, self.neg, 0)

if __name__ == '__main__':
    Motor()
    rospy.spin()
