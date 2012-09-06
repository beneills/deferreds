#!/usr/bin/env python
#
# Ben Eills, 2012
#
# No permission is required to copy, distribute or modify this source code, in
#   fact, the author hopes that you might improve it.  Attribution and linking
#   to the source and/or corresponding tutorial is politely requested.
#

"""
Simple example of Twisted
See tutorial at TODO
"""

from twisted.internet import reactor, defer

def slow_multiply(x, y):
    """
    This function multiplies two numbers very slowly (for a computer).
    It takes 3 seconds.
    It returns a Deferred instantly which fires with the result once we've determined it.
    """
    d = defer.Deferred()
    reactor.callLater(3, d.callback, x * y)
    return d

def print_multiplication_result(fired_value):
    """
    Is called by Twisted when the Deferred given by slow_multiply finally fires.  We pretty print the result it fires with.
    """
    print "... result is {0}!".format(fired_value)

print "Determining result of 5 * 7..."
d = slow_multiply(5, 7)
d.addCallback(print_multiplication_result)

# We stop Twisted after 4 seconds, long enough for our code to finish.
# This is pretty similar to Fate's "shutdown" method.
reactor.callLater(4, reactor.stop)
reactor.run()
