#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import Action, MotorCoordinate

from random import choice
import threading
import time
import sys
import os

class Brain():
    def __init__(self):
        rospy.init_node('brain', anonymous=True)
        self.pub = rospy.Publisher("/motors/goals", MotorCoordinate)
        rospy.Subscriber("events", Action, self.callback)
        rospy.Subscriber("/motors/locations", MotorCoordinate, self.update_location)

        self.event_dict = self.load_scripts()
        self.perms_lock = threading.Lock()
        self.shutdown_flags = set()

        self.ownership_dict = { "BLINK": None,
                                "NECK" : None,
                                "LARM" : None,
                                "RARM" : None, 
                                "PUR"  : None}

        self.threshold = {  "BLINK": 5,
                            "NECK" : 5,
                            "LARM" : 5,
                            "RARM" : 5, 
                            "PUR"  : 5, }

        self.locations = {  "BLINK": 0,
                            "NECK" : 0,
                            "LARM" : 0,
                            "RARM" : 0, 
                            "PUR"  : 0, }

    def callback(self, data):
        event = data.type

        if not event in self.event_dict:
            rospy.logwarn("BRAIN: Unrecognized event - {}".format(event))
            return

        script = choice(self.event_dict[event])
        
        with self.perms_lock:
            for m in script.motors:
                owner = self.ownership_dict[m]
                if not owner:
                    continue

                if script.level >= owner.level:
                    rospy.loginfo("BRAIN: Permission denied - {}".format(script.name))
                    return
                else: 
                    #rospy.loginfo("BRAIN: Adding to shutdown - {}".format(owner.name))
                    self.shutdown_flags.add(owner)

            for owner in self.shutdown_flags:
                for m in owner.motors:
                    self.ownership_dict[m] = None

            thread = threading.Thread(target=script.run, args=(self,))
            thread.level = script.level
            thread.motors = script.motors

            for m in thread.motors:
                self.ownership_dict[m] = thread

            rospy.loginfo("Launching thread: {}".format(thread.name))
            thread.start()

    def check_perms(self):
        cur_thread = threading.current_thread()
        if cur_thread in self.shutdown_flags:
            rospy.loginfo("BRAIN: Permissions stolen - {}".format(cur_thread.name))
            self.shutdown_flags.discard(cur_thread)
            sys.exit()

    def exit(self):
        with self.perms_lock:
            cur_thread = threading.current_thread()

            for m in cur_thread.motors:
                if self.ownership_dict[m] == cur_thread:
                    self.ownership_dict[m] = None

        rospy.loginfo("Exiting from {}".format(threading.current_thread().name))
        sys.exit()

    # TODO: Have this load all scripts from folder
    def load_scripts(self):
        event_to_output = {
                "BELLY_RUB":[__import__("herolib/moves/move5")],
                "TEST":[__import__("herolib/moves/move1")]}

        # event_to_output = {}

        # for fd in os.listdir("herolib/moves"):
        #     script = __import__("herolib/moves" + fd)
            
        #     for e in script.events:
        #         event_to_output[e].append(script)

        # return event_to_output

        return event_to_output


    def update_location(self, data):
        self.locations[data.name] = data.position
        #rospy.loginfo("BRAIN: Updating {} position to {}".format(data.name, data.position))

    def move_to(self, **kargs):
        self.check_perms()

        for motor, position in kargs.iteritems():
            rospy.loginfo("BRAIN: Move {} to {}".format(motor, position))
            self.pub.publish(MotorCoordinate (motor, position))
        
    def wait_until(self, **kargs):
        reached = False

        while True:
            reached = True
            
            self.check_perms()
            for motor, position in kargs.iteritems():
                if abs(self.locations[motor] - position) > self.threshold[motor]:
                    time.sleep(.1)
                    reached = False
                    break

            if reached:
                break

    def move_and_wait(self, **kargs):
        self.move_to(**kargs)
        self.wait_until(**kargs)

    def play(self, path):
        os.system('mpg321 {} &'.format(path))

if __name__ == '__main__':
    Brain()
    rospy.spin()
