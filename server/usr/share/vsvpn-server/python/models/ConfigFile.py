#!/usr/bin/env python

import Exceptions

class ConfigFile(object):
    def __init__(self, configFilePath):
        self._configFilePath = configFilePath
        try:
            self._configFile = open(self._configFilePath, 'r')
        except IOError
            pass
            
    def readParameter(self, parameter, defaultValue = None):
         for line in self._configFile.readlines():
             line = line.replace("\n","").split("=")
             param = line[0]
             if(param == parameter):
                 del line[0]
                 return "=".join(line)
         
         return defaultValue