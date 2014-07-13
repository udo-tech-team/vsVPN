#!/usr/bin/env python

import threading
import socket
import os
import hashlib

from common.exceptions.AlreadyRunning import AlreadyRunning

class SocketListener(threading.Thread): 
    def __init__(self, vpnServer):
        threading.Thread.__init__(self)
        hashHost = hashlib.md5(vpnServer.getServerHost()).hexdigest()
        self._socketPath = "/tmp/vsvpn_socket_"+hashHost
        self._vpnServer = vpnServer
        
        if os.path.exists( self._socketPath ):
            raise AlreadyRunning
            
    def stop(self):
        os.remove(self._socketPath)
        self.running = False
        
    def run(self):
        self.running = True
        server = socket.socket( socket.AF_UNIX, socket.SOCK_DGRAM )
        server.bind(self._socketPath)
        
        while(self.running):
            datagram = server.recv( 1024 )
            if datagram:
                if(datagram == "kill"):
                    self.stop()
                    self._vpnServer.disconnect()
                    