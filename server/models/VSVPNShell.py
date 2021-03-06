#!/usr/bin/env python
import shlex
import subprocess
from common.models.ConfigManager import ConfigFile

class VSVPNShell(object):
    def __init__(self, configFile):
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

    # Commands managed by the shell
    def _command_getServerGateway(self, args):
        return (0, self._configFile.get("serverGateway", "192.168.200.1"))
        
    def _command_getNetMask(self, args):
        return (0, self._configFile.get("mask", "255.255.255.0"))
        
    def _command_getVPNParams(self, args):
        result = "GATEWAY="+self._configFile.get("serverGateway", "192.168.200.1")+"\n"+"NETMASK="+self._configFile.get("mask", "255.255.255.0")
        return (0, result)
    
    def _command_startLink(self, args):
        process = subprocess.call(['sudo', '-A', '/usr/sbin/pppd', 'nodetach', 'notty', 'noauth'])
        if process != 0:
            raise Exception("I was not able to start pppd. I may not have sudo access.")