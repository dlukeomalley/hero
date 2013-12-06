#!/usr/bin/env python

CALIBRATE = False
DEBUG = False

import roslib; roslib.load_manifest('hero')

import rospy
from hero.msg import Action, MotorCoordinate

import random
import threading
import sys
import os

class Brain():
    def __init__(self):
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

        rospy.init_node('brain', anonymous=True)
        self.pub = rospy.Publisher("/motors/goals", MotorCoordinate)
        rospy.Subscriber("events", Action, self.callback)
        rospy.Subscriber("/motors/locations", MotorCoordinate, self.update_location)

        if CALIBRATE:
            import pdb
            kill = False
            while True:
                pdb.set_trace()
                if kill:
                    sys.exit()
        

    def callback(self, data):
        event = data.type

        if not event in self.event_dict:
            rospy.logwarn("BRAIN: Unrecognized event - {}".format(event))
            return

        script = random.choice(self.event_dict[event])
        
        with self.perms_lock:
            for m in script.motors:
                owner = self.ownership_dict[m]
                if not owner:
                    continue

                if script.level >= owner.level:
                    if DEBUG:
                        rospy.loginfo("BRAIN: Permission denied - {}".format(script.name))
                    return
                else: 
                    if DEBUG:
                        rospy.loginfo("BRAIN: Adding to shutdown - {}".format(owner.name))
                    self.shutdown_flags.add(owner)

            for owner in self.shutdown_flags:
                for m in owner.motors:
                    self.ownership_dict[m] = None

            thread = threading.Thread(target=script.run, args=(self,))
            thread.level = script.level
            thread.motors = script.motors

            for m in thread.motors:
                self.ownership_dict[m] = thread

            if DEBUG:
                rospy.loginfo("Launching thread: {}".format(thread.name))
            thread.start()


    def check_perms(self):
        cur_thread = threading.current_thread()
        if cur_thread in self.shutdown_flags:
            if DEBUG:
                rospy.loginfo("BRAIN: Permissions stolen - {}".format(cur_thread.name))
            self.shutdown_flags.discard(cur_thread)
            sys.exit()


    def exit(self):
        with self.perms_lock:
            cur_thread = threading.current_thread()

            for m in cur_thread.motors:
                if self.ownership_dict[m] == cur_thread:
                    self.ownership_dict[m] = None

        if DEBUG:
            rospy.loginfo("Exiting from {}".format(threading.current_thread().name))
        sys.exit()


    # TODO: Have this load all scripts from folder
    def load_scripts(self):
        event_to_output = {}
 
        BASE = "/home/pi/2009red/src/hero/src/"

        for fd in os.listdir(BASE + "herolib/moves"):
            if "action_" in fd:
                fd, end = fd.split(".")

                if "pyc" in end:
                    continue

                script = __import__("herolib.moves." + fd, fromlist=['foo'])

                for e in script.events:
                    if e in event_to_output:
                        event_to_output[e].append(script)
                    else:
                        event_to_output[e] = [script]

        if DEBUG:
            rospy.loginfo(event_to_output)

        return event_to_output


    # Allow ID team to easily write scripts that harness power of randomness
    def parse_args(old_func):
        def new(self, **kargs):
            for motor, position in kargs.iteritems():
                if type(position) == tuple:
                    a, b = position
                    kargs[motor] = random.randint(a, b)
            return old_func(self, **kargs)
        return new


    def update_location(self, data):
        self.locations[data.name] = data.position
        if DEBUG:
            rospy.loginfo("BRAIN: Updating {} position to {}".format(data.name, data.position))


    @parse_args
    def move_to(self, **kargs):
        self.check_perms()

        for motor, position in kargs.iteritems():
            rospy.loginfo("BRAIN: Move {} to {}".format(motor, position))
            self.pub.publish(MotorCoordinate (motor, position))

    
    # wait for x seconds
    def wait(duration):
        if type(duration) == tuple:
            a, b = duration
            duration = random.uniform(a, b)
        
        rospy.sleep(duration)

        
    # wait until position reached
    @parse_args
    def wait_until(self, **kargs):
        reached = False

        while True:
            reached = True
    
            self.check_perms()
            for motor, position in kargs.iteritems():
                if abs(self.locations[motor] - position) > self.threshold[motor]:
                    rospy.sleep(.1)
                    reached = False
                    break

            if reached:
                break


    @parse_args
    def move_and_wait(self, **kargs):
        self.move_to(**kargs)
        self.wait_until(**kargs)

    def stop_with_probability(p):
        if random.random() > p:
            sys.exit()


    def play(self, path):
        # TODO, may have to be absolute path
        os.system('mpg321 {} &'.format(path))

if __name__ == '__main__':
    Brain()
    rospy.spin()
