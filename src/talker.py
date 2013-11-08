#!/usr/bin/env python

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

PKG = 'hero' # this package name
import roslib; roslib.load_manifest(PKG)

import rospy
from hero.msg import Action

def talker():
    pub = rospy.Publisher('chatter', Action)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        str = "Belly rub @ %s"%rospy.get_time()
        rospy.loginfo(str)
        pub.publish(Action(str))
        r.sleep()
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
