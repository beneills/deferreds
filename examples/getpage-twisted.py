#!/usr/bin/env python
#
# Ben Eills, 2012
#
# No permission is required to copy, distribute or modify this source code, in
#   fact, the author hopes that you might improve it.  Attribution and linking
#   to the source and/or corresponding tutorial is politely requested.
#

"""
Example of using Twisted's getPage utility function in place of urllib2
See tutorial at TODO
"""

from twisted.internet import reactor
import twisted.web.client as twc

# This Twisted library function returns a Deferred
d = twc.getPage("http://www.beneills.com/")

# The deferred will fire when/if the page is successfully downloaded with the contents of the web page as a string

# As in the above examples, we tell Twisted what to do when it does fire

def printPage(data):
    print "Page contents:"
    print data

d.addCallback(printPage)

# Shutdown, regardless of success after 3 seconds
reactor.callLater(3, reactor.stop)

reactor.run()
