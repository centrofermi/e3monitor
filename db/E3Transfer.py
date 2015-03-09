# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:52:54 2015

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]

[0] station_name,
[1] run_date,
[2] run_id,
[3] bin_file_size,
[4] transfer_timestamp,
[5] last_update
[6] number_of_files_transferred_since_midnight
"""


class E3Transfer(dict):

    def __init__(self):
        self._mydict = {}

    def add_entry(self, schoolName, schoolData):
        self._mydict[schoolName] = schoolData

    def set_numFiles(self, schoolName, numFiles):
        self._mydict[schoolName][6] = numFiles

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

    def get_numFiles(self, schoolName):
        return(self._mydict[schoolName][6])
