#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Handler.QingHuaHandler import *

f = open('./RawImage/uploadimage.jpg')
handle = QingHuaHandler(u"老王", u"软件工程", u"男", u"本科", "2000000", "300000", f)
handle.handleData()
