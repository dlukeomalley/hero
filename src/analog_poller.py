#!/usr/bin/env python

import roslib;
roslib.load_manifest('hero')
import rospy
from hero.msg import MotorCoordinate

DEBUG = False
CALIBRATE = False

if not DEBUG:
    import herolib.thirdparty.Adafruit_MCP3008 as MCP3008

N_CHANNELS = 8
ALPHA = .8
THRESHOLD = 1

def poll():
    pub = rospy.Publisher('/motors/locations', MotorCoordinate)
    rospy.init_node('analog_poller', anonymous=True)
    
    # set polling rate in Hz
    if CALIBRATE:
        rate = 1
    else:
        rate = 100

    r = rospy.Rate(rate)

    pin_map = { 0: "LARM",
                1: "RARM",
                2: "NECK",
                7: "BLINK",
                3: 'PUR'}

    old_reading = [0]*N_CHANNELS
    voltages = [0]*N_CHANNELS

    while not rospy.is_shutdown():
        if DEBUG:
            reading = [0]*8
        else:
            reading = MCP3008.read_all()

        voltages = reading

        if CALIBRATE:
            rospy.loginfo("AX: {}".format(voltages))

        for i, name in pin_map.iteritems():
            if name == 'PUR':
                voltages[i] = 0
            pub.publish(MotorCoordinate(name, voltages[i]))

        r.sleep()
        
if __name__ == '__main__':
    try:
        poll()
    except rospy.ROSInterruptException: pass
