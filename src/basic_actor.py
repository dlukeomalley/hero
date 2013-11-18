#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')
import actions as output

import rospy
from hero.msg import Action
    
class Actor:
    def __init__(self):
        self.action_map =  {"BELLY UPPER" : output.hug(),
                            "BELLY LOWER": output.hug(),
                            "LEFT ARM": output.wave("LEFT"),
                            "RIGHT ARM": output.wave("RIGHT"),
                            "FRONT HEAD": output.headshake(),
                            "BACK HEAD": output.none(),
                            "BLINK": output.blink(),
                            "PUR": output.pur()}

        rospy.Subscriber("abstract_action", Action, self.callback)

    def callback(self, data):
        import pdb
        pdb.set_trace()




        if data.type in self.action_map:
            rospy.loginfo("Basic Actor Acting: {}".format(data))
            self.action_map[data.type]()

if __name__ == '__main__':
    rospy.init_node('basic_actor', anonymous=True)
    Actor()
    rospy.spin()
