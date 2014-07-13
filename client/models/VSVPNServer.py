#!/usr/bin/env python

import subprocess

class VSVPNServer(object):
    
    def __init__(self, clientConfig, serverHost):
        self._clientConfig = clientConfig
        self._serverHost = serverHost
        
    def sendCommand(self, command):
        if(isinstance(command, basestring)):
            command = [command]
            
        sshCommand = ["ssh",  self._serverHost, "-i", self._clientConfig.get("userKey", "/etc/vsvpn/client_key")] + command
        subprocess.call(sshCommand)
        
    def loadGateway(self):
        return self.sendCommand("getServerGateway")