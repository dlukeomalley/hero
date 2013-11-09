#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import Action
    
class Actor():
    def __init__(self):
        rospy.Subscriber("abstract_action", Action, self.callback)

    def callback(self, action):
        if action.type == "HUG":
            self.hug()
            
    def hug(self):
        self.log("HUG")

    def log(self, action):
        rospy.loginfo("Acting: {}".format(action))
        

if __name__ == '__main__':
    rospy.init_node('basic_actor', anonymous=True)
    Actor()
    rospy.spin()
