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

        self.own = {} # this could contain motors to a script class that contains priority, name, etc
        # initialize lock here
        # load everything from herolib.moves?
        self.event_map = self.load_scripts()

    def callback(self, data):
        event = data.type

        # if not a recognized event, exit
        if not event in self.event_map:
            rospy.logwarn("BRAIN: Unrecognized event - {}".format(event))
            return

        script = choice(self.event_map[event])

        import pdb
        pdb.set_trace()

        # with self.perm_lock:
        #     contended = []
        #     # check if any of our perms are held
        #     for m in move.perms:
        #         # if motor is already spoken for, make note
        #         if self.motor[m]:
        #             contended.append[m]
        # check permissions, can we own or evict if necessary?
        # if we evict, kill thread that was running previously
        # if we can't, just return now
        # release lock
        # create a new thread and run import's main function

        # consider passing own name here so sidestep collission issue
        thread = threading.Thread(target=script.run)
        rospy.loginfo("Launching thread: {}".format(thread.name))
        thread.start()

    def update_location(self, data):
        # update location dictionary, read by children nodes so they know when they can continue running
        pass

    # decorate these with if permisions not owned, kill thread? would be cleaner code...
    def move_to(self):
        # check permissions, if permissions no longer owned, shut down thread
        rospy.loginfo("Hello from {}".format(threading.current_thread().name))
	time.sleep(1)

    def wait_until(self, **kargs):
        # check permissions on every cycle, could be that thread doens't know it should shut down?
        pass

    def move_and_wait(self, **kargs):
        pass

    # TODO: Have this load all scripts from folder
    def load_scripts(self):
        test = __import__('move')

        return {"BELLY_RUB": [test]}

    def cleanup(self, thread):
        pass

if __name__ == '__main__':
    Brain()
    rospy.spin()