#!/usr/bin/python
# -*- coding: UTF-8 -*-
from QingHuaHandler import QingHuaHandler
from BeiDaHandler import BeiDaHandler
def getCardHandler(school):
    if school == '0' :
        return QingHuaHandler()
    elif school == '1':
        return BeiDaHandler()
    else: 
        return null
