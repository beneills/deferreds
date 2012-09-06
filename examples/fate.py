#!/usr/bin/env python
#
# Ben Eills, 2012
#
# No permission is required to copy, distribute or modify this source code, in
#   fact, the author hopes that you might improve it.  Attribution and linking
#   to the source and/or corresponding tutorial is politely requested.
#

"""
Fate library code only.  Import into your code!
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
