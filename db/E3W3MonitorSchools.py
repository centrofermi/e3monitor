# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 16:52:54 2015

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]

"""


class E3W3MonitorSchools(dict):

    def __init__(self):
        self._mydict = {}

    def init_School(self, schoolName):
        self._mydict[schoolName] = ['']*10

    def set_transferDelayDays(self, schoolName, date):
        self._mydict[schoolName][0] = date

    def set_transferDelaySeconds(self, schoolName, date):
        self._mydict[schoolName][1] = date

    def set_transferFileName(self, schoolName, fileName):
        self._mydict[schoolName][2] = fileName

    def set_transferTs(self, schoolName, date):
        self._mydict[schoolName][3] = date

    def set_elogEntryTs(self, schoolName, date):
        self._mydict[schoolName][4] = date

    def set_DqmFileName(self, schoolName, fileName):
        self._mydict[schoolName][5] = fileName

    def set_triggerRate(self, schoolName, rate):
        self._mydict[schoolName][6] = rate

    def set_trackRate(self, schoolName, rate):
        self._mydict[schoolName][7] = rate

    def get_transferDelayDays(self, schoolName):
        return(self._mydict[schoolName][0])

    def get_transferDelaySeconds(self, schoolName):
        return(self._mydict[schoolName][1])

    def get_transferFileName(self, schoolName):
        return(self._mydict[schoolName][2])

    def get_transferTs(self, schoolName, date):
        return(self._mydict[schoolName][3])

    def get_elogEntryTs(self, schoolName, date):
        return(self._mydict[schoolName][4])

    def get_DqmFileName(self, schoolName, fileName):
        return(self._mydict[schoolName][5])

    def get_triggerRate(self, schoolName, rate):
        return(self._mydict[schoolName][6])

    def get_trackRate(self, schoolName, rate):
        return(self._mydict[schoolName][7])

    def get_schoolData(self, schoolName):
        return(self._mydict[schoolName])

    def get_allData(self):
        return(self._mydict)
