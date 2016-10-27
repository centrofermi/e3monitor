# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 18:22:24 2014

@author: Fabrizio Coccetti
"""
import os


def read_dqmreport(schoolNamesList, pathDqmreport):
    ''' Find directory for the last daily dqmreport
    the format is: dqmreport2/ALTA-01/2014-11-12/index.html
    '''
    lastDqmreport = {}
    schoolsDqmreportList = []
    for dirSchoolName in schoolNamesList:
        try:
            dirDates = os.listdir(os.path.join(pathDqmreport, dirSchoolName))
        except:
            lastDqmreport[dirSchoolName] = ''
        # Get the directory of last day of DqmReports
        if len(dirDates) < 1:
            lastDqmreport[dirSchoolName] = ''
        else:
            lastDqmreport[dirSchoolName] = sorted(dirDates)[-1]
            schoolsDqmreportList.append(dirSchoolName)
    return lastDqmreport, schoolsDqmreportList
