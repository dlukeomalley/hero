#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import CapSense, Action

def callback(data):
    rospy.loginfo("Read: {}".format(data.sensor))
    
def basic_touch_interpreter():
    rospy.init_node('basic_touch_interpreter', anonymous=True)
    rospy.Subscriber("capsense_values", CapSense, callback)

    rospy.spin()
        
if __name__ == '__main__':
    basic_touch_interpreter()
