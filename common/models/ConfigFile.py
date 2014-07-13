#!/usr/bin/env python


class ConfigFile(object):
    def __init__(self, configFilePath):
        self._configFilePath = configFilePath
        try:
            self._configFile = open(self._configFilePath, 'r')
        except IOError:
            self._configFile = None
            
    def get(self, parameter, defaultValue = None):
        if(self._configFile):
            for line in self._configFile.readlines():
                
                if(len(line) > 0 and line[0] != "#"):
                    line = line.replace("\n","").split("=")
                    param = line[0]
                    if(param == parameter):
                        del line[0]
                        return "=".join(line)
         
        return defaultValue