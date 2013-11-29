#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import Action

def poll():
    valid_input = { 'h' : 'BELLY_RUB',
                    'b' : 'BLINK',
                    's' : 'HEAD_PAT',
                    'p' : 'PUR',
                    'w' : 'BELLY_RUB',
                    't' : 'TEST',
                    'wl': 'LARM_GRAB',
                    'wr': 'RARM_GRAB' }

    rospy.init_node('keyboard_poller', anonymous=True)
    pub = rospy.Publisher('events', Action)

    while not rospy.is_shutdown():
        s = raw_input("h/b/wr/wl/s/p/t/w: ")
        s.lower()
        rospy.loginfo("Keyboard Input: {}".format(s))
        
        if s in valid_input:
            pub.publish(valid_input[s])
        
if __name__ == '__main__':
    try:
        poll()
    except rospy.ROSInterruptException: pass
