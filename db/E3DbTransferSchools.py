# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:52:54 2015

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]

station_name,
run_date,
run_id,
bin_file_size,
transfer_timestamp,
last_update

"""


class E3DbTransferSchools(dict):

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

    def bin_file_size(self, schoolName):
        return(self._mydict[schoolName][3])

    def transfer_timestamp(self, schoolName):
        return(self._mydict[schoolName][4])

    def last_update(self, schoolName):
        return(self._mydict[schoolName][5])
