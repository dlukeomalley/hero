#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import CapSense

import RPi.GPIO as GPIO
from herolib.external import MPR121
import time

MPR121_IRQ = 17
NUM_TOUCH_PADS = 12
MPR121_ADDR = 0x5a

def poller():
    # Initialize ROS features
    pub = rospy.Publisher('capsense_state', CapSense)
    rospy.init_node('capsense_poller', anonymous=True)

    # Initialize GPIO Pin numbering and I/O
    GPIO.setmode(GPIO.BCM)
    #GPIO.setup(MPR121_IRQ, GPIO.IN)

    # Initialize MP121 capacitive touch board
    MPR121.TOU_THRESH = 0x15
    MPR121.REL_THRESH = 0x12
    MPR121.setup(MPR121_ADDR)

    # set polling rate in Hz
    r = rospy.Rate(4)
    old_touch_data = 0
    
    while not rospy.is_shutdown():
        touch_data = MPR121.readData(MPR121_ADDR)
        touch_data &= 0b111111

        if not touch_data == old_touch_data:
            sensor_values = [False] * NUM_TOUCH_PADS

            for i in range(NUM_TOUCH_PADS):
                if touch_data & (1 << i):
                    sensor_values[i] = True

            old_touch_data = touch_data

            # Publish readings to capsense_values topic
            pub.publish(sensor_values)
            rospy.loginfo(sensor_values)

        r.sleep()
        
if __name__ == '__main__':
    try:
        poller()
    except rospy.ROSInterruptException: pass
