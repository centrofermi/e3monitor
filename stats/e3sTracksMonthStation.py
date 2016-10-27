#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon 30 May 2016

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
Query Run Db and extract several infos
"""

import os
import MySQLdb
from datetime import datetime, timedelta
import ConfigParser
import csv
import logging
import logging.config
import calendar
from e3monitor.config.__stations__ import EEE_STATISTIC_STATIONS 
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

# Define start of the run and other dates
startRun = datetime(2015, 11, 7)
startRunStr = startRun.strftime("%Y-%m-%d")
endRun = datetime(2016, 5, 20)
endRunStr = startRun.strftime("%Y-%m-%d")
#today = datetime.today()
#todayStr = today.strftime("%Y-%m-%d")

# Set up logging
logging.config.fileConfig(logConfigFile)
logger = logging.getLogger('full')
logger.info('Started')
logger = logging.getLogger('plain')

# Open output file
w = open('/var/www/html/monitor/stats/tracks_per_month_per_station.csv', 'w')
logger.info('Opened output file.')
# Adding headers to the output file
w.write('Date' + ',')
for schoolName in EEE_STATISTIC_STATIONS:
    w.write(schoolName + ',')
w.write('\n')

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
query = "SELECT SUM(num_track_events) from runs2 WHERE (run_date >= %s AND run_date <= %s) AND station_name = %s;"
logger.info("Exec loop: " + query)
for _firstDay, _lastDay in enumerate_month_dates(startRun, endRun):
    _lastDayStr = _lastDay.strftime("%Y-%m-%d")
    # writing date to file
    w.write(_lastDayStr + ',')
    # Loop for each station in Run
    for schoolName in EEE_STATISTIC_STATIONS:
        queryParam = (startRunStr, _lastDayStr, schoolName)
        logger.info('Parameters: ' + str(queryParam))
        cur.execute(query, queryParam)
        try: 
            _tracks = int(cur.fetchone()[0])
        except:
            _tracks = 0
        logger.info('School: ' + schoolName + '  Tracks: ' + str(_tracks))
        w.write(str(_tracks) + ',')
    w.write('\n')

logger.info('Final Result of the queries:\n')

# Save the  data extracted from the db
#logger.info('Writing data to file...')
#output = open(os.path.join(pathWorkDir, pklStatFile), 'wb')
#pickle.dump(trackStat, output)
#output.close()
#logger = logging.getLogger('full')
#logger.info('Written ' + os.path.join(pathWorkDir, pklStatFile))

cur.close()
db.close()
w.close()
logger.info('Finished')

