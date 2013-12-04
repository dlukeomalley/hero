#!/usr/bin/env python

import roslib;
roslib.load_manifest('hero')
import rospy
from hero.msg import MotorCoordinate

DEBUG = False
if not DEBUG:
    import herolib.thirdparty.Adafruit_MCP3008 as MCP3008

N_CHANNELS = 8
ALPHA = .8

def poll():
    pub = rospy.Publisher('/motors/locations', MotorCoordinate)
    rospy.init_node('analog_poller', anonymous=True)
    
    # set polling rate in Hz
    r = rospy.Rate(100)

    pin_map = { 0: "NECK",
                1: "LARM",
                2: "RARM",
                3: "BLINK"}

    old_reading = [0]*N_CHANNELS
    voltages = [0]*N_CHANNELS

    while not rospy.is_shutdown():
        if DEBUG:
            reading = [0]*8
        else:
            reading = MCP3008.read_all()

        for i in range(N_CHANNELS):
            voltages[i] = reading[i]*ALPHA + old_reading[i]*(1-ALPHA)
        
        old_readings = voltages

        for i, name in pin_map.iteritems():
            pub.publish(MotorCoordinate(name, voltages[i]))
        
        r.sleep()
        
if __name__ == '__main__':
    try:
        poll()
    except rospy.ROSInterruptException: pass
