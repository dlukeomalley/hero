#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import MotorCoordinate

def poll():
    rospy.init_node('test_poller', anonymous=True)
    pub = rospy.Publisher('/motors/goals', MotorCoordinate)

    while not rospy.is_shutdown():
        s = raw_input("Motor, Position:")
        s.upper()
        rospy.loginfo("Keyboard Input: {}".format(s))
        try:
            motor, position = s.split(',')
            pub.publish(MotorCoordinate(motor, int(position)))
        except:
            pass
        
if __name__ == '__main__':
    try:
        poll()
    except rospy.ROSInterruptException: pass
