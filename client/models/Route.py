#!/usr/bin/env python

import subprocess
import platform

class Route(object):   
    def __init__(self, ip, netmask, gateway):
        self._ip = ip
        self._netmask = netmask
        self._gateway = gateway
    
    def create(self):
        subprocess.call(['route', 'add', '-host', self._ip, '-netmask', self._netmask, self._gateway])
        