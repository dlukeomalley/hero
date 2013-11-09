#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import CapSense

def poller():
    pub = rospy.Publisher('capsense_state', CapSense)
    rospy.init_node('capsense_poller', anonymous=True)

    # set polling rate in Hz
    r = rospy.Rate(4)
    
    while not rospy.is_shutdown():
        # read MP121
        # log capsense values
        sensor_values = [False]*12

        rospy.loginfo("Capsense Reading: {}".format(sensor_values))
        # Publish readings to capsense_values topic
        pub.publish(CapSense([False]*12))
        r.sleep()
        
if __name__ == '__main__':
    try:
        poller()
    except rospy.ROSInterruptException: pass
