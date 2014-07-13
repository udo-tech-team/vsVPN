#!/usr/bin/env python

import subprocess
import platform

class Route(object):   
    def __init__(self, config, ip, netmask, gateway, interface):
        self._ip = ip
        self._netmask = netmask
        self._gateway = gateway
        self._interface = interface
        self._config = config
    
    def create(self):
        if(platform.system() == 'Darwin'):
            args = ['route', 'add', '-net', self._ip, '-netmask', self._netmask, '-interface', self._interface, '-gateway', self._gateway]
           
        if(self._config.get("verbose_routes", "false") == "true"):
            print "{route} " + " ".join(args)
            
        subprocess.call(args)
        