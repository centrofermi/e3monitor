# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 16:58:18 2014

@author: Fabrizio Coccetti
"""
import csv
from datetime import datetime


def read_schools_elog(elogCsvFile):
    '''Read last date for the Entries on the High School E-logbook
    EEE Logbook'''
    allEntries = []
    lastEntryPerSchool = {}
    f = open(elogCsvFile, 'r')
    reader = f.readline()
    reader = csv.reader(f)
    for row in reader:
        allEntries.append([(int(row[0]), row[3], row[1]+row[2])])
    f.close()
    allEntries.sort(key=lambda entryId: entryId[0])
    for row in allEntries:
        lastEntryPerSchool[row[0][1]] = \
            datetime.strptime(row[0][2], '%d/%m/%Y%H:%M:%S')
    return lastEntryPerSchool
