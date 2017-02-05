# -*- coding: utf-8 -*-

from netcatPython import Netcat
import conf
import re

class DataLoader:

    def __init__(self):
        self.nc = Netcat(conf.tlCli_host, conf.tlCli_port)

    def getNewMessages(self, target):
        lastMsg = self.nc.getHistory(target)
        return lastMsg

    def close(self):
        self.nc.close()

    def transformRawMsg(rawMsg):
        url = re.search('.*tag=', rawMsg)





