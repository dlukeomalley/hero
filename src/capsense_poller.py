#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import CapSense
import RPi.GPIO as GPIO
import mpr121
import time

NUM_TOUCH_PADS = 12
MPR121_ADDR = 0x5a

def poller():
    # Initialize ROS features
    pub = rospy.Publisher('capsense_state', CapSense)
    rospy.init_node('capsense_poller', anonymous=True)

    # Initialize GPIO Pin numbering and I/O
    GPIO.setmode(GPIO.BOARD)

    # Initialize MP121 capacitive touch board
    mpr121.TOU_THRESH = 0x15
    mpr121.REL_THRESH = 0x12
    mpr121.setup(MPR121_ADDR)

    # set polling rate in Hz
    r = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        IRQ = True
        
        # if IRQ is active
        if IRQ:
            sensor_values = [False] * NUM_TOUCH_PADS
            touch_data = mpr121.readData(MPR121_ADDR)

            for i in range(NUM_TOUCH_PADS):
                if touch_data & (1 << i):
                    sensor_values[i] = True

            # Publish readings to capsense_values topic
            pub.publish(sensor_values)

        r.sleep()
        
if __name__ == '__main__':
    try:
        poller()
    except rospy.ROSInterruptException: pass
