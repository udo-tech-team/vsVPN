#!/usr/bin/env python

import subprocess
import time
from common.models.ConfigManager import ConfigContent
from client.models.Tunnel import Tunnel
from client.models.Route import Route

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
    
    def getServerHost(self):
        return self._serverHost
        
    def connect(self, myIp):
        self.tunnel = Tunnel(self._clientConfig, self._serverHost, myIp, self._params.get("GATEWAY"))
        self.tunnel.start()
        
        while(not tunnel.isConnected()):
            time.sleep(0.1)
        
        route = Route(self._clientConfig, myIp, self._params.get("NETMASK", "255.255.255.0"), self._params.get("GATEWAY"), tunnel.getInterface())
        route.create()
        
    def disconnect(self):
        try:
            self.tunnel.stop()
        except NameError:
            print "I have never been connected!"