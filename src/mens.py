#!/usr/bin/env python

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import Action, MotorCoordinate

import threading
import sys
from random import choice
import time

class Brain():
    def __init__(self):
        # TODO: In launch file have this restart if it errors and closes prematurely
        rospy.init_node('brain', anonymous=True)
        self.pub = rospy.Publisher("goals", MotorCoordinate)
        rospy.Subscriber("events", Action, self.callback)
        rospy.Subscriber("locations", MotorCoordinate, self.update_location)

        self.locations = {}
        self.event_dict = self.load_scripts()
        self.perms_lock = threading.Lock()
        self.shutdown_flags = set()

        self.ownership_dict = { "BLINK": None,
                                "NECK" : None,
                                "LARM" : None,
                                "RARM" : None, 
                                "PUR"  : None}

    def callback(self, data):
        event = data.type

        if not event in self.event_dict:
            rospy.logwarn("BRAIN: Unrecognized event - {}".format(event))
            return

        script = choice(self.event_dict[event])
        
        with self.perms_lock:
            # set of threads that we can steal ownership from
            for m in script.motors:
                owner = self.ownership_dict[m]
                if not owner:
                    continue

                if script.level >= owner.level:
                    rospy.loginfo("BRAIN: Permission denied - {}".format(script.name))
                    return
                else: 
                    rospy.loginfo("BRAIN: Adding to shutdown - {}".format(owner.name))
                    self.shutdown_flags.add(owner)

            # cleanup threads we're stealing from
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
        return {"BELLY_RUB": [__import__('move5')],
                "TEST": [__import__('move1')]}

    def update_location(self, data):
        self.location[data.name] = data.positition

    def move_to(self):
        self.check_perms()
        rospy.loginfo("Hello from {}".format(threading.current_thread().name))
        time.sleep(1)

    def wait_until(self):
        # sleep until self.location has the right things
        pass

if __name__ == '__main__':
    Brain()
    rospy.spin()
