#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import Action

valid_input = { 'h': 'BELLY_UPPER',
                'b': 'BLINK'}

def poller():
    pub = rospy.Publisher('abstract_action', Action)
    rospy.init_node('keyboard_poller', anonymous=True)

    while not rospy.is_shutdown():
        s = raw_input("h/b: ")
        s.lower()
        rospy.loginfo("Keyboard Input: {}".format(s))
        
        if s in valid_input:
            pub.publish(valid_input[s])
        
if __name__ == '__main__':
    try:
        poller()
    except rospy.ROSInterruptException: pass
