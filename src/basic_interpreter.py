#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import CapSense, Action
import pdb

data = {(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0): None,
        (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): "BELLY_RUB"}
    

class Interpreter():
    def __init__(self):
        # initialize sensor value to 0

        self.pub = rospy.Publisher("abstract_action", Action)
        rospy.Subscriber("capsense_state", CapSense, self.callback)

    def callback(self, data):
        pdb.set_trace()
        sensor = data.sensor

        rospy.loginfo("Basic Interpreter Read: {}".format(sensor))

        distances = [(action, euclidean_distance(sensor, sample)) for sample, action in data.iteritems()]
        distances = sorted(distances, key=lambda x: entry[1])

        action, val = distances[0]

        if action:
            self.publish(action)

    def publish(self, abstract_action):
        self.pub.publish(abstract_action)

    def euclidean_distance(s1, s2):
        return sum([(x - y)**2 for x, y in zip(s1, s2)])

if __name__ == '__main__':
    rospy.init_node('basic_interpreter', anonymous=True)
    Interpreter()
    rospy.spin()
