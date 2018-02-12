# -*- coding: utf-8 -*-

from API_WIN10 import *

line = LINE()
line.log("Auth Token : " + str(line.authToken))
channelToken = line.getChannelResult()
line.log("Channel Token : " + str(channelToken))
