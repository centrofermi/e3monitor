#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed 24 Feb 2016

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
Query Run Db and extract total number of tracks
"""

import os
import MySQLdb
from datetime import datetime, timedelta
import ConfigParser
import pickle
import logging
import logging.config
import calendar
from e3monitor.config.__files_server__ import (logConfigFile,
                                               dbConfigFile,
                                               pklStatFile,
                                               pathWorkDir)


def enumerate_month_dates(start_date, end_date):
    current = start_date
    while current <= end_date:
        if current.month >= 12:
            next = datetime(current.year + 1, 1, 1)
        else:
            next = datetime(current.year, current.month + 1, 1)
        last = min(next - timedelta(1), end_date)
        yield current, last
        current = next

# Define dictionary with dates and number of tracks
trackStat = {}

# Define start of the run and other dates
startRun = datetime(2014, 9, 1)
startRunStr = startRun.strftime("%Y-%m-%d")
today = datetime.today()
todayStr = today.strftime("%Y-%m-%d")

# Set up logging
logging.config.fileConfig(logConfigFile)
logger = logging.getLogger('full')
logger.info('Started')
logger = logging.getLogger('plain')

# Reading db ini file
logger.info('Reading ' + dbConfigFile)
parser = ConfigParser.ConfigParser()
parser.read(dbConfigFile)
host = parser.get('General', 'host')
user = parser.get('General', 'user')
dbname = parser.get('General', 'dbname')
passwd = parser.get('General', 'passwd')

# Connecting to the database
logger.info('Connecting to %s on %s (as %s)' % (dbname, host, user))
db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=dbname)

cur = db.cursor()

# Query for the number of tracks every month
logger.info('Queries of the total number of Tracks')
query = "SELECT SUM(num_track_events) from runs2 WHERE (run_date >= %s AND run_date <= %s);"
logger.info("Exec loop: " + query)
for _firstDay, _lastDay in enumerate_month_dates(startRun, today):
    _lastDayStr = _lastDay.strftime("%Y-%m-%d")
    queryParam = (startRunStr, _lastDayStr)
    logger.info('Parameters: ' + str(queryParam))
    cur.execute(query, queryParam)
    try: 
        _tracks = int(cur.fetchone()[0])
    except:
        _tracks = 0
    logger.info('Tracks: ' + str(_tracks))
    trackStat[_lastDayStr] = _tracks

logger.info('Final Result of the queries:\n' + str(trackStat))

# Save the  data extracted from the db
logger.info('Writing data to file...')
output = open(os.path.join(pathWorkDir, pklStatFile), 'wb')
pickle.dump(trackStat, output)
output.close()
logger = logging.getLogger('full')
logger.info('Written ' + os.path.join(pathWorkDir, pklStatFile))

cur.close()
db.close()
logger.info('Finished')

