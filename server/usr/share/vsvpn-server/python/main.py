#!/usr/bin/env python

from models.VSVPNServer import VSVPNServer

if __name__ == '__main__':
    _vsServer = VSVPNServer()
    try:
        _vsServer.mainLoop()
    except KeyboardInterrupt:
        pass