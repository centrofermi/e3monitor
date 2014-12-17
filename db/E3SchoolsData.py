# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 16:06:54 2014

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
"""


class E3SchoolsData(dict):

    def __init__(self):
        self._mydict = {}

    def add_entry(self, schoolName, schoolData):
        self._mydict[schoolName] = schoolData

    def print_schoolData(self, schoolName):
        print(self._mydict[schoolName])

    def print_AllData(self):
        print(self._mydict)

    def run_date(self, schoolName):
        return(self._mydict[schoolName][1])

    def run_id(self, schoolName):
        return(self._mydict[schoolName][2])

    def transfer_timestamp(self, schoolName):
        return(self._mydict[schoolName][3])

    def run_start(self, schoolName):
        return(self._mydict[schoolName][5])

    def run_stop(self, schoolName):
        return(self._mydict[schoolName][6])

    def num_events(self, schoolName):
        return(self._mydict[schoolName][9])

    def num_hit_events(self, schoolName):
        return(self._mydict[schoolName][10])

    def num_track_events(self, schoolName):
        return(self._mydict[schoolName][11])

    def run_duration(self, schoolName):
        return(self._mydict[schoolName][6] - self._mydict[schoolName][5])

