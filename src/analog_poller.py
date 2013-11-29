#!/usr/bin/env python

import roslib;
roslib.load_manifest('hero')
import rospy
from hero.msg import MotorCoordinate

DEBUG = True
if not DEBUG:
    from herolib.thirdparty import MCP3008

def poll():
    pub = rospy.Publisher('/motors/locations', MotorCoordinate)
    rospy.init_node('analog_poller', anonymous=True)
    # set polling rate in Hz
    r = rospy.Rate(2)

    pin_map = { 0: "HEAD",
                1: "LARM",
                2: "RARM",
                3: "BLINK"}

    while not rospy.is_shutdown():
        # code to read from analog and send out to chip goes here
        if DEBUG:
            voltages = [0]*8
        else:
            voltages = MCP3008.read_all()

        for i, name in pin_map.iteritems():
            pub.publish(MotorCoordinate(name, voltages[i]))
            #rospy.loginfo('{}: {}'.format(name, voltages[i]))

        r.sleep()
        
if __name__ == '__main__':
    try:
        poll()
    except rospy.ROSInterruptException: pass
