#!/usr/bin/env python

import threading
import pipes
import subprocess
import time 
import re

class Tunnel(threading.Thread): 
    def __init__(self, config, host, myIp, gateway):
        threading.Thread.__init__(self)
        self.running = False
        self._host = host
        self._myIp = myIp
        self._gateway = gateway
        self._config = config
        self._process = None
        self._interface = None
        self._pppConnected = False
        
    def openpppd(self):
        ipArg = self._myIp+":"+self._gateway
        if(self._config.get("defaultRoute", "false") == "true"):
            defaultRoute = "defaultroute"
        else:
            defaultRoute = "nodefaultroute"
            
        command = ["/usr/sbin/pppd", "nodetach", "noauth", "passive", "pty", "ssh "+pipes.quote(self._host)+" -i "+pipes.quote(self._config.get("userKey", "/etc/vsvpn/client_key"))+" -l "+pipes.quote(self._config.get("vsvpnUser", "vsvpn"))+" -o Batchmode=yes -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null startLink", "ipparam", "vpn", defaultRoute, ipArg ]
        self._process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while self._process.poll() == None:
            line = self._process.stdout.readline().replace("\n","")
            
            if(self._config.get("verbose_pppd", "false") == "true"):
                print "{pppd} "+line
                
            interface_search = re.search('(.+)Using interface (.+)', line)
            if(interface_search):
                self._interface = interface_search.group(2)
                
            if("remote IP address" in line):
                self._pppConnected = True
                
            time.sleep(.1)
    
    def getInterface(self):
        return self._interface
    
    def isConnected(self):
        return self._pppConnected
        
    def stop(self):
        self._process.kill()
        self.running = False
        
    def run(self):
        self.running = True
        while(self.running):
            self.openpppd()