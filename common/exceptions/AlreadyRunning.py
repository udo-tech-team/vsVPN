#!/usr/bin/env python

class AlreadyRunning(Exception):
    def __str__(self):
        return repr('A client is already running for this host!')