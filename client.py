#!/usr/bin/env python

from common.models.ConfigManager import ConfigFile
from client.models.VSVPNServer import VSVPNServer
import sys

DEFAULT_CONFIG_FILE = "/etc/vsvpn/client.conf"

if __name__ == '__main__':
    _clientConfigFile = DEFAULT_CONFIG_FILE
    _clientConfig = ConfigFile(_clientConfigFile)
    
    hostToConnect = _clientConfig.get("vpnServer")
    
    if(hostToConnect):
        _myIp = _clientConfig.get("myIp", "auto")

        _vpnServer = VSVPNServer(_clientConfig, hostToConnect)
        _vpnServer.loadParams()
        _vpnServer.connect(_myIp) 
    else:
        raise Exception("Unable to find 'vpnServer' config")