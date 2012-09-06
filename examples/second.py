#!/usr/bin/env python
#
# Ben Eills, 2012
#
# No permission is required to copy, distribute or modify this source code, in
#   fact, the author hopes that you might improve it.  Attribution and linking
#   to the source and/or corresponding tutorial is politely requested.
#

"""
Chained Fuse example, including general purpose Fate event handling code.
See tutorial at TODO
"""

## These two classes for the entirety of the Fate event handling system, exactly
##   the same as in the Mad Hatter example.
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


## This function explodes Parliament and shuts down universe.
def explode_parliament():
    print "Boom! The Houses of Parliament explode!"
    fate.shutdown()

## This class represents a fuse in part of a chain.
import sys
class FuseInChain(object):
    def __init__(self, tie_to, burn_time):
        """
        Initialize a new fuse in our chain, tying it to the current end fuse, tie_to
        If tie_to is None, we are tied directly to the barrel.
        We become the new end fuse.
        """
        self.next = tie_to
        self.burn_time = burn_time

    def ignite(self):
        """
        Ignite this fuse.
        """
        print "...igniting next fuse in chain..."
        f = fate.get_fuse(self.burn_time)
        if self.next is None:
            # We are the last Fuse in the chain.  Blow up barrel.
            f.set_handler(explode_parliament)
        else:
            f.set_handler(self.next.ignite)


fate = Fate()
tmp = FuseInChain(None, 0.3)
for i in xrange(7):
    tmp = FuseInChain(tmp, i/10.0)
last = tmp

last.ignite()
fate.run()

