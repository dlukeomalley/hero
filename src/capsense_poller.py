#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import CapSense

import RPi.GPIO as GPIO
from herolib.thirdparty.Adafruit_MCP230XX import Adafruit_MCP230XX

RESET = 16
INT = None
NUM_TOUCH_PADS = 7

def poll():
    # Initialize ROS features
    pub = rospy.Publisher('capsense_state', CapSense)
    rospy.init_node('capsense_poller', anonymous=True)

    # Initialize GPIO Pin numbering and I/O
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(RESET, GPIO.OUT)
    GPIO.setup(INT, GPIO.IN)
    
    # Turn on chip
    GPIO.output(RESET, True)

    MCP23017 = Adafruit_MCP230XX(address = 0x20, num_gpios = 16)
    # don't change any pins to outputs
    # don't enable the pullup resistors

    # set polling rate in Hz
    r = rospy.Rate(100)
    
    while not rospy.is_shutdown():
        # If state has changed on INTA line
        if GPIO.input(INT):
            if NUM_TOUCH_PADS <= 8:
                # Adafruit code suggests this reads all of OLATA
                data = MCP23017.readU8()
            else:
                # Adafruit code suggests this reads all of OLATB
                data = MCP23017.readU16()

            touch_array = [False] * NUM_TOUCH_PADS

            for i in range(NUM_TOUCH_PADS):
                if touch_data & (1 << i):
                    touch_array[i] = True

                # Publish readings to capsense_values topic
                pub.publish(touch_array)
                # rospy.loginfo(touch_array)

        # Prevent this from being a tight loop
        r.sleep()
        
if __name__ == '__main__':
    try:
        poll()
    except rospy.ROSInterruptException: pass
