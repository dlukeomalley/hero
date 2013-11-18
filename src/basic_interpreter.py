#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import CapSense, Action
import pdb

data_set = {(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0): None,
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0): "BELLY UPPER",
        (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0): "BELLY LOWER",
        (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0): "LEFT ARM",
        (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0): "RIGHT ARM",
        (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0): "FRONT HEAD",
        (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): "BACK HEAD"}

class Interpreter():
    def __init__(self):
        # initialize sensor value to 0

        self.pub = rospy.Publisher("abstract_action", Action)
        rospy.Subscriber("capsense_state", CapSense, self.callback)

    def callback(self, data):
        sensor = data.sensor

        #rospy.loginfo("Basic Interpreter Read: {}".format(sensor))

        distances = [(action, self.euclidean_distance(sensor, sample)) for sample, action in data_set.iteritems()]
        distances = sorted(distances, key=lambda pair: pair[1])

        action, val = distances[0]

        if action:
            rospy.loginfo("OUTPUT: {}".format(action))
            self.publish(action)

    def publish(self, abstract_action):
        self.pub.publish(abstract_action)

    def euclidean_distance(self, s1, s2):
        return sum([(x - y)**2 for x, y in zip(s1, s2)])

if __name__ == '__main__':
    try:
        rospy.init_node('basic_interpreter', anonymous=True)
        Interpreter()
        rospy.spin()
    except rospy.ROSInterruptException: pass
