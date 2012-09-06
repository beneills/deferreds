#!/usr/bin/env python
#
# Ben Eills, 2012
#
# No permission is required to copy, distribute or modify this source code, in
#   fact, the author hopes that you might improve it.  Attribution and linking
#   to the source and/or corresponding tutorial is politely requested.
#

"""
Twisted version of Firecracker program.
See tutorial at TODO
"""

# Standard Twisted imports.  You'll need these for most Twisted applications.
from twisted.internet import reactor, defer

import random

class FireCracker(object):
    def __init__(self, owner):
        self.owner = owner
    def hand_to(self, new_owner):
        self.owner = new_owner
    def explode(self, rv):
        print "BOOM! Firecracker exploded in the unlucky hands " \
            "of {0}".format(self.owner)
    def light_fuse(self):
        burning_time = random.choice([0.5, 1.0, 1.5, 2.0])
        d = defer.Deferred()
        d.addCallback(self.explode)
        reactor.callLater(burning_time, d.callback, True)


class MadHatter(object):
    def __repr__(self):
        return "Mad Hatter"


class BenEills(object):
    def __repr__(self):
        return "Ben Eills"


# Hatter and Ben are born
hatter = MadHatter()
ben = BenEills()

# FireCracker appears, intitially owned by the Hatter
fc = FireCracker(hatter)

# The Hatter lights the fuse immediately
reactor.callLater(0, fc.light_fuse)

# Waits one second and passes it to Ben
reactor.callLater(1, fc.hand_to, ben)

# And stop Twisted after 3 seconds, long enough for the FireCracker to certainly explode
reactor.callLater(3, reactor.stop)

# Start Twisted
reactor.run()
