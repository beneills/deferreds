#!/usr/bin/env python
#
# Ben Eills, 2012
#
# No permission is required to copy, distribute or modify this source code, in
#   fact, the author hopes that you might improve it.  Attribution and linking
#   to the source and/or corresponding tutorial is politely requested.
#

"""
Mad Hatter example, including general purpose Fate event handling code.
See tutorial at TODO
"""

## These two classes for the entirety of the Fate event handling system.
## They are general purpose, i.e. not specific to the Mad Hatter scenario.
import time

class Fate(object):
    def __init__(self):
        self._shutdown = False
        self.fuses = []

    def get_fuse(self, seconds):
        f = Fuse()
        f.set_time(time.time() + seconds)
        self.fuses.append(f)
        return f

    def check_fuses(self):
        for fuse in self.fuses:
            if fuse.has_handler() and fuse.is_burned():
                self.fuses.remove(fuse)
                fuse.call_handler()

    def run(self):
        while not self._shutdown:
            self.check_fuses()
            time.sleep(0.2)

    def shutdown(self):
        self._shutdown = True


class Fuse(object):
    def set_time(self, time):
        self.time = time
    def is_burned(self):
        return self.time < time.time()
    def set_handler(self, handler):
        self.handler = handler
    def has_handler(self):
        return hasattr(self, 'handler')
    def call_handler(self):
        self.handler()



## The following three classes are used in our specific scenario.
## To utilize Fate in your own program, take these as examples and modify
##   to suit your particular problem.
import random

class FireCracker(object):
    def __init__(self, owner, fate):
        self.owner = owner
        self.fate = fate
    def hand_to(self, new_owner):
        self.owner = new_owner
    def explode(self):
        print "BOOM! Firecracker exploded in the unlucky hands " \
            "of {0}".format(self.owner)
        # After any explosion, shutdown program after 2 second delay
        # Otherwise we'd have to kill the program
        f = self.fate.get_fuse(2)
        f.set_handler(self.fate.shutdown)
    def light_fuse(self):
        burning_time = random.choice([0.5, 1.0, 1.5, 2.0])
        f = self.fate.get_fuse(burning_time)
        f.set_handler(self.explode)


class MadHatter(object):
    def __repr__(self):
        return "Mad Hatter"


class BenEills(object):
    def __repr__(self):
        return "Ben Eills"


## The remaining lines make use of the Fate and Mad Hatter objects above.
# Universe come into existence
fate = Fate()
# Hatter and Ben are born
hatter = MadHatter()
ben = BenEills()
# FireCracker appears, intitially owned by the Hatter
fc = FireCracker(hatter, fate)
# The Hatter lights the fuse
fc.light_fuse()
# And hands it to Ben
fc.hand_to(ben)
# Universe begins paying attention to duration of time
# At some point during run, the FireCracker will explode
#   and 2 seconds later, Fate will be shutdown
fate.run()
# Universe has ended.  We have no cleanup to do.
