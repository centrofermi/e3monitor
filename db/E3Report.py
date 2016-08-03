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
        self._mydict[schoolName] = ['']*10

    def set_transferDelayDays(self, schoolName, date):
        self._mydict[schoolName][0] = date

    def set_transferDelaySeconds(self, schoolName, date):
        self._mydict[schoolName][1] = date

    def set_transferDelayStatus(self, schoolName, status):
        self._mydict[schoolName][2] = status

    def get_transferDelayDays(self, schoolName):
        return(self._mydict[schoolName][0])

    def get_transferDelaySeconds(self, schoolName):
        return(self._mydict[schoolName][1])

    def get_trasferDelayStatus(self, schoolName):
        return(self._mydict[schoolName][2])

    def get_schoolData(self, schoolName):
        return(self._mydict[schoolName])

    def get_allData(self):
        return(self._mydict)
