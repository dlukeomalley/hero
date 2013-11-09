#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import CapSense, Action
    
class Interpreter():
    def __init__(self):
        # initialize sensor value to 0
        self.sensor = [False]*12

        self.pub = rospy.Publisher("abstract_action", Action)
        rospy.Subscriber("capsense_state", CapSense, self.callback)

    def callback(self, data):
        self.sensor = data.sensor
        rospy.loginfo("Read: {}".format(self.sensor))

        # TODO: Actually interpret sensor values
        for val in self.sensor:
            if val:
                self.publish("HUG")
                break

    def publish(self, abstract_action):
        self.pub.publish(abstract_action)

if __name__ == '__main__':
    rospy.init_node('basic_interpreter', anonymous=True)
    Interpreter()
    rospy.spin()
