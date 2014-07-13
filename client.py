#!/usr/bin/env python

from common.models.ConfigFile import ConfigFile

DEFAULT_CONFIG_FILE = "/etc/vsvpn/client.conf"

if __name__ == '__main__':
    _clientConfigFile = DEFAULT_CONFIG_FILE
    _clientConfig = ConfigFile(_clientConfigFile)
    
    hostToConnect = _clientConfig.get("vpnServer")