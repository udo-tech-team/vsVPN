#!/usr/bin/env python

import shlex

class VSVPNServer(object):
    def mainLoop(self):
        while True:
            _vsInput = raw_input("> ")
            _vsInput = shlex.split(_vsInput)
            print _vsInput