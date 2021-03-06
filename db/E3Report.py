# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 18:32:00 2016

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]

Written by apps/e3reportAnalyze.py
"""


class E3Report(dict):

    def __init__(self):
        self._mydict = {}

    def init_School(self, schoolName):
        self._mydict[schoolName] = ['']*11

    # Set methods

    def set_transferDelayDays(self, schoolName, date):
        self._mydict[schoolName][0] = date

    def set_transferDelaySeconds(self, schoolName, date):
        self._mydict[schoolName][1] = date

    def set_transferTs(self, schoolName, date):
        self._mydict[schoolName][2] = date

    def set_transferDelayStatus(self, schoolName, status):
        self._mydict[schoolName][3] = status

    def set_elogEntryTs(self, schoolName, date):
        self._mydict[schoolName][4] = date

    def set_elogEntryStatus(self, schoolName, status):
        self._mydict[schoolName][5] = status

    def set_triggerRate(self, schoolName, rate):
        self._mydict[schoolName][6] = rate

    def set_triggerStatus(self, schoolName, status):
        self._mydict[schoolName][7] = status

    def set_trackRate(self, schoolName, rate):
        self._mydict[schoolName][8] = rate

    def set_trackStatus(self, schoolName, status):
        self._mydict[schoolName][9] = status

    def set_message(self, schoolName, msg):
        self._mydict[schoolName][10] = msg

    # Get methods

    def get_transferDelayDays(self, schoolName):
        return(self._mydict[schoolName][0])

    def get_transferDelaySeconds(self, schoolName):
        return(self._mydict[schoolName][1])

    def get_transferTs(self, schoolName):
        return(self._mydict[schoolName][2])

    def get_transferDelayStatus(self, schoolName):
        return(self._mydict[schoolName][3])

    def get_elogEntryTs(self, schoolName):
        return(self._mydict[schoolName][4])

    def get_elogEntryStatus(self, schoolName):
        return(self._mydict[schoolName][5])

    def get_triggerRate(self, schoolName):
        return(self._mydict[schoolName][6])

    def get_triggerStatus(self, schoolName):
        return(self._mydict[schoolName][7])

    def get_trackRate(self, schoolName):
        return(self._mydict[schoolName][8])

    def get_trackStatus(self, schoolName):
        return(self._mydict[schoolName][9])

    def get_message(self, schoolName):
        return(self._mydict[schoolName][10])

    def get_schoolData(self, schoolName):
        return(self._mydict[schoolName])

    def get_allData(self):
        return(self._mydict)
