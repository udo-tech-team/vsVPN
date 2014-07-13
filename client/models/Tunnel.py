#!/usr/bin/env python

import threading
import pipes
import subprocess

class Tunnel(threading.Thread): 
    def __init__(self, config, host, myIp, gateway):
        threading.Thread.__init__(self)
        self.running = False
        self._host = host
        self._myIp = myIp
        self._gateway = gateway
        self._config = config
        self._process = None
        
        
    def openpppd(self):
        ipArg = self._myIp+":"+self._gateway
        command = ["/usr/sbin/pppd", "nodetach", "noauth", "passive", "pty", "ssh "+pipes.quote(self._host)+" -i "+pipes.quote(self._config.get("userKey", "/etc/vsvpn/client_key"))+" -l "+pipes.quote(self._config.get("vsvpnUser", "vsvpn"))+" -o Batchmode=yes -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null startLink", "ipparam", "vpn", ipArg ]
        self._process = subprocess.call(command)
        
    def stop(self):
        self._process.kill()
        self.running = False
        
    def run(self):
        self.running = True
        while(self.running):
            self.openpppd()