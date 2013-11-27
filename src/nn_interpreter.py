#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import CapSense, Action


# Translation between input and event
data_set = {(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0): None,
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0): "BELLY_RUB",
            (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0): "BELLY_RUB",
            (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0): "LARM_GRAB",
            (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0): "RARM_GRAB",
            (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0): "HEAD_PAT",
            (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): "HEAD_PAT"}

class Interpreter():
    def __init__(self):
        rospy.init_node('nn_interpreter', anonymous=True)
        self.pub = rospy.Publisher("events", Action)
        rospy.Subscriber("capsense_state", CapSense, self.callback, queue_size=2)

    def callback(self, data):
        sensor = data.sensor
        distances = [(action, self.euclidean_distance(sensor, sample)) for sample, action in data_set.iteritems()]
        distances = sorted(distances, key=lambda pair: pair[1])

        #TODO: Add in distance threshold for no action

        action, val = distances[0]

        # ignore action if action is None
        if action:
            rospy.loginfo("OUTPUT: {}".format(action))
            pub.publish(abstract_action)

    def euclidean_distance(self, s1, s2):
        return sum([(x - y)**2 for x, y in zip(s1, s2)])

if __name__ == '__main__':
    Interpreter()
    rospy.spin()
