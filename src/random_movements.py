#!/usr/bin/env python

import time
import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import Action
import random

actions = [ "INACTIVE" ]

def move():
    pub = rospy.Publisher("events", Action)
    rospy.init_node('random_movements', anonymous=True)

    while not rospy.is_shutdown():
        event = random.choice(actions)

        pub.publish(event)
        rospy.loginfo("RANDOM: {}".format(event))

        # randomly move once after a time between A, B seconds
        rospy.sleep(random.randint(5, 15))
        
if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass
