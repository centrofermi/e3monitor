# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 16:52:54 2015

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]

"""


class E3W3MonitorSchools(dict):

    def __init__(self):
        self._mydict = {}

    def init_School(self, schoolName):
        self._mydict[schoolName] = [''*10]

    def set_transferDelayDays(self, schoolName, date):
        self._mydict[schoolName][0] = date

    def set_transferDelaySeconds(self, schoolName, date):
        self._mydict[schoolName][1] = date

    def get_transferDelayDays(self, schoolName):
        return(self._mydict[schoolName][0])

    def get_transferDelaySeconds(self, schoolName):
        return(self._mydict[schoolName][1])

    def get_schoolData(self, schoolName):
        return(self._mydict[schoolName])

    def get_allData(self):
        return(self._mydict)
