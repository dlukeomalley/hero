#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import Action
import random

def blink():
    pub = rospy.Publisher("abstract_action", Action)
    rospy.init_node('blink_generator', anonymous=True)

    while not rospy.is_shutdown():
        pub.publish("BLINK")
        rospy.loginfo("Blink Generator: BLINK")

        # randomly blink once after a time between A, B seconds
        rospy.sleep(random.randint(20, 40))
        
if __name__ == '__main__':
    try:
        blink()
    except rospy.ROSInterruptException: pass
