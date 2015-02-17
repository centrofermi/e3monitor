# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 16:06:54 2014

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
"""


class E3DbDqmSchools(dict):

    def __init__(self):
        self._mydict = {}

    def add_entry(self, schoolName, schoolData):
        self._mydict[schoolName] = schoolData

    def schoolData(self, schoolName):
        return(self._mydict[schoolName])

    def AllData(self):
        return(self._mydict)

    def run_date(self, schoolName):
        return(self._mydict[schoolName][1])

    def run_id(self, schoolName):
        return(self._mydict[schoolName][2])

    def transfer_timestamp(self, schoolName):
        return(self._mydict[schoolName][4])

    def run_start(self, schoolName):
        return(self._mydict[schoolName][6])

    def run_stop(self, schoolName):
        return(self._mydict[schoolName][7])

    def num_events(self, schoolName):
        return(self._mydict[schoolName][10])

    def num_hit_events(self, schoolName):
        return(self._mydict[schoolName][11])

    def num_track_events(self, schoolName):
        return(self._mydict[schoolName][12])

    def run_duration(self, schoolName):
        return(self._mydict[schoolName][7] - self._mydict[schoolName][6])

    def trigger_rate(self, schoolName):
        try:
            run_time = (float(self._mydict[schoolName][7]) -
                        float(self._mydict[schoolName][6]))
        except:
            return -2
        if run_time <= 0:
            return -1
        else:
            return float(self._mydict[schoolName][10])/run_time

    def track_rate(self, schoolName):
        try:
            run_time = (float(self._mydict[schoolName][7]) -
                        float(self._mydict[schoolName][6]))
        except:
            return -2
        if run_time <= 0:
            return -1
        else:
            return float(self._mydict[schoolName][12])/run_time
