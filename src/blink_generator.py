#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')
import rospy
from hero.msg import Action

import time
import random

def blink():
    pub = rospy.Publisher("abstract_action", Action)
    rospy.init_node('blink_generator', anonymous=True)

    while not rospy.is_shutdown():
        pub.publish("BLINK")
        rospy.loginfo("Blink Generator: BLINK")

        if random.randint(0,1):
            time.sleep(.25)
            pub.publish("BLINK")

        # randomly blink once after a time between A, B seconds
        rospy.sleep(random.randint(10, 20))
        
if __name__ == '__main__':
    try:
        blink()
    except rospy.ROSInterruptException: pass
