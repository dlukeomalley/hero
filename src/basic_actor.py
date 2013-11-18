#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')
import actions as output

import rospy
from hero.msg import Action
    
class Actor:
    def __init__(self):
        output.stop_all()

        self.action_map =  {"BELLY UPPER" : output.hug,
                            "BELLY LOWER": output.tail_wag,
                            "LEFT ARM": output.left_hand_grab,
                            "RIGHT ARM": output.right_hand_grab,
                            "FRONT HEAD": output.headshake,
                            "BACK HEAD": output.none,
                            "BLINK": output.blink,
                            "PUR": output.pur,
                            "TEST": output.test,
                            "LEFT WAVE": output.left_wave,
                            "RIGHT WAVE": output.right_wave}

        rospy.Subscriber("abstract_action", Action, self.callback, queue_size=2)
        rospy.on_shutdown(output.stop_all)


    def callback(self, data):
        if data.type in self.action_map:
            rospy.loginfo("Basic Actor Acting: {}".format(data))
            self.action_map[data.type]()

if __name__ == '__main__':
    rospy.init_node('basic_actor', anonymous=True)
    Actor()
    rospy.spin()
