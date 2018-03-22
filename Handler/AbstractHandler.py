#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta,abstractmethod

class AbstractHandler():
    __metaclass__ = ABCMeta

    @abstractmethod
    def handleData(self, name, sex, colleges, degeree, id_number, date, upload_file):
        pass
