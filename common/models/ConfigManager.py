#!/usr/bin/env python

class ConfigObject(object):
    def get(self, parameter, defaultValue = None):
        pass

class ConfigContent(ConfigObject):
    def __init__(self, configContent):
        self._configContent = configContent

    def get(self, parameter, defaultValue = None):
        if(self._configContent):
            for line in self._configContent.split("\n"):          
                if(len(line) > 0 and line[0] != "#"):
                    line = line.replace("\n","").split("=")
                    param = line[0]
                    if(param == parameter):
                        del line[0]
                        return "=".join(line).replace("\n","")
         
        return defaultValue
        
class ConfigFile(ConfigObject):
    def __init__(self, configFilePath):
        self._configFilePath = configFilePath
        try:
            self._configFile = open(self._configFilePath, 'r')
        except IOError:
            self._configFile = None
            
    def get(self, parameter, defaultValue = None):
        if(self._configFile):
            self._configFile.seek(0)
            for line in self._configFile.readlines():
               if(len(line) > 0 and line[0] != "#"):
                    line = line.replace("\n","").split("=")
                    param = line[0]
                    if(param == parameter):
                        del line[0]
                        return "=".join(line).replace("\n","")
         
        return defaultValue
