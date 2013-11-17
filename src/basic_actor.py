#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import Action
    
class Actor():
    def __init__(self):
        rospy.Subscriber("abstract_action", Action, self.callback)

        self.valid_action = {"BELLY_RUB": self.hug,
                             "BLINK": self.blink}

    def callback(self, action):
        rospy.loginfo("Basic Actor Read: {}".format(action))

        if action.type in self.valid_action:
            self.valid_action[action.type]()
            
    def hug(self):
        self.log("hugging")

    def blink(self):
        self.log("blinking")

    def log(self, action):
        rospy.loginfo("Basic Actor Acting: {}".format(action))
        

if __name__ == '__main__':
    rospy.init_node('basic_actor', anonymous=True)
    Actor()
    rospy.spin()
