#!/usr/bin/env python

from common.models.ConfigManager import ConfigFile
from common.exceptions.AlreadyRunning import AlreadyRunning
from client.models.VSVPNServer import VSVPNServer
from client.models.SocketListener import SocketListener

import sys
import signal
import os 
import hashlib
import socket

DEFAULT_CONFIG_FILE = "/etc/vsvpn/client.conf"

class Client(object):
    def __init__(self):
        self._clientConfigFile = DEFAULT_CONFIG_FILE
        self._clientConfig = ConfigFile(self._clientConfigFile)
        self._hostToConnect = self._clientConfig.get("vpnServer")

    def stop(self):
        print "Ending"
        hashHost = hashlib.md5(self._hostToConnect).hexdigest()
        _socketPath = "/tmp/vsvpn_socket_"+hashHost
        
        if(os.path.exists(_socketPath)):
            client = socket.socket( socket.AF_UNIX, socket.SOCK_DGRAM )
            try:
                client.connect( _socketPath )
            except socket.error:
                os.remove(_socketPath)
            else:
                client.send("kill")
        
    def start(self):
        if(not os.path.exists('/etc/ppp/options')):
            open('/etc/ppp/options','w').close()
                
        if(self._hostToConnect):
            _myIp = self._clientConfig.get("myIp", "auto")
            _vpnServer = VSVPNServer(self._clientConfig, self._hostToConnect)
            _vpnServer.loadParams()
            
            try:
                _socketListener = SocketListener(_vpnServer)
            except AlreadyRunning:
                print "VSVPN Client is already running for this host!"
                sys.exit(2)
                
            _vpnServer.connect(_myIp) 
            _socketListener.start()
            
        else:
            raise Exception("Unable to find 'vpnServer' config")
            
if __name__ == '__main__':
    vpnClient = Client()
    
    if(len(sys.argv) > 1 and sys.argv[1] == '--stop'):
        vpnClient.stop()
    else:
        vpnClient.start()
    
    