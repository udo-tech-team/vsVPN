#!/usr/bin/env python

DEFAULT_CONFIG_FILE = "/etc/vsvpn/server.conf"

import shlex
from models.ConfigFile import ConfigFile

class VSVPNShell(object):
    def __init__(self, configFile = DEFAULT_CONFIG_FILE):
        self._configFile = ConfigFile(configFile)
        
    def main(self, args):
        command = self.runCommand(args)
        print command[1]
        return command[0]
            
    def runCommand(self, uInput):
        try:
            command = uInput[0]
            del uInput[0]
        except IndexError:
            return (2, "No command given")
        
        try:
            return getattr(self, "_command_"+command)(uInput)
        except AttributeError:
            return (2, "Unknown command ")

    def _command_getLocalIp(self, args):
        return (0, self._configFile.get("serverIp", "192.168.200.1"))