#!/usr/bin/env python

import subprocess
from common.models.ConfigManager import ConfigContent
from client.models.Tunnel import Tunnel

class VSVPNServer(object):   
    def __init__(self, clientConfig, serverHost):
        self._clientConfig = clientConfig
        self._serverHost = serverHost
        self._params = None
        
    def sendCommand(self, command):
        if(isinstance(command, basestring)):
            command = [command]
            
        sshCommand = ["ssh",  self._serverHost, "-i", self._clientConfig.get("userKey", "/etc/vsvpn/client_key"), "-l", self._clientConfig.get("vsvpnUser", "vsvpn")] + command
        return subprocess.check_output(sshCommand)
        
    def loadParams(self):
        self._params = ConfigContent(self.sendCommand("getVPNParams"))
        
    def connect(self, myIp):
        tunnel = Tunnel(self._clientConfig, self._serverHost, myIp, self._params.get("GATEWAY", "255.255.255.0"))
        tunnel.start()
        