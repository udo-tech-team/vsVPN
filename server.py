#!/usr/bin/env python

from server.models.VSVPNShell import VSVPNShell
import sys, getopt

DEFAULT_CONFIG_FILE = "/etc/vsvpn/server.conf"

if __name__ == '__main__':
    _vsShell = VSVPNShell(DEFAULT_CONFIG_FILE)
    args = sys.argv
    
    try:
        while ( args[0] != "-c" ):
            del args[0]
    
        del args[0]
    except IndexError:
        args = []
            
    returnCode = _vsShell.main(args)
    sys.exit(returnCode)
