#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 11:08:30 2014

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
Query Run Db and extract Transfer and DQM data
"""

import os
import MySQLdb
from datetime import datetime
import ConfigParser
import pickle
import logging
import logging.config
from e3monitor.config.__files_server__ import (logConfigFile,
                                               dbConfigFile,
                                               pklDqmFile,
                                               pklTransferFile,
                                               pklTracksFile,
                                               pathWorkDir)
from e3monitor.db.E3Dqm import E3Dqm
from e3monitor.db.E3Transfer import E3Transfer

# List with the name of the Schools
schoolNames = []
# Class with methods with last run in DQM from the database
dqmData = E3Dqm()
transferData = E3Transfer()
# Define dates
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

# Connect to the School's table and get the school name list
logger.info('Connect to the School\'s table and get the school name list')
query = "SELECT name FROM telescopes;"
logger.info('Get the School\'s name list: ' + query)
cur.execute(query)
schoolNames = [item[0] for item in cur.fetchall()]
sorted(schoolNames)

# Initialize Transfer Data
for _schoolName in schoolNames:
    transferData.init_School(_schoolName)
    print(transferData.schoolData(_schoolName))

# Query for the last transferred file at CNAF
logger.info('Query for the last run transferred at CNAF of each school')
query = ("SELECT station_name, run_date, run_id, bin_file_size, "
         "transfer_timestamp, last_update "
         "FROM runs2 WHERE station_name = %s "
         "ORDER BY transfer_timestamp DESC LIMIT 1;")
logger.info('About to query: ' + query)
for _schoolName in schoolNames:
    cur.execute(query, _schoolName)
    _entry = cur.fetchone()
    if _entry is None:
        continue
    # Assign parameter to the class
    transferData.add_entry(_schoolName, _entry)
    logger.info('Read School: ' + _schoolName)
    logger.info(transferData.schoolData(_schoolName))

# Query for the number of files transferred today
_beginTime = datetime.today().strftime("%Y-%m-%d") + " 00:00:00"
_endTime = datetime.today().strftime("%Y-%m-%d") + " 23:59:59"
logger.info('Query for the number of files transferred today')
query = ("SELECT COUNT(*) FROM runs2 "
         "WHERE station_name = %s "
         "AND (transfer_timestamp BETWEEN %s AND %s);")
logger.info('About to query: ' + query)
for _schoolName in schoolNames:
    queryParam = (_schoolName, _beginTime, _endTime)
    cur.execute(query, queryParam)
    _entry = cur.fetchone()
    if _entry is None:
        continue
    # Assign parameter to the class
    transferData.set_numFiles(_schoolName, _entry)
    # transferData.add_entry(_schoolName, _entry)
    logger.info('Read School: ' + _schoolName)
    logger.info(transferData.schoolData(_schoolName))
    logger.info(transferData.get_numFiles(_schoolName))

# Save the Transfer data extracted from the db
logger.info('Writing data to file...')
output = open(os.path.join(pathWorkDir, pklTransferFile), 'wb')
pickle.dump(transferData, output)
output.close()
logger = logging.getLogger('full')
logger.info('Written ' + os.path.join(pathWorkDir, pklTransferFile))

# Query for DQM: the last run data of each school
logger.info('Query for the last run in DQM of each school')
query = ("SELECT * FROM runs2 WHERE station_name = %s "
         "AND processing_status_code=0 "
         "ORDER BY last_update DESC LIMIT 1;")
logger.info('About to query: ' + query)
for _schoolName in schoolNames:
    cur.execute(query, _schoolName)
    _entry = cur.fetchone()
    if _entry is None:
        continue
    # Assign parameter to the class
    dqmData.add_entry(_schoolName, _entry)
    logger.info('Read School: ' + _schoolName)
    logger.info(dqmData.schoolData(_schoolName))

# Query for Statistics
logger.info('Query for statistics:')
logger.info('1. Query of the total number of Tracks')
query = ("SELECT SUM(num_track_events) from runs2 WHERE (run_date >= %s AND run_date <= %s);")
queryParam = (startRunStr, todayStr)
cur.execute(query, queryParam)
try:
    totalTracks = int(cur.fetchone()[0])
except:
    totalTracks = 0
logger.info('Total Tracks: ' + str(totalTracks))

# Save the DQM data extracted from the db
logger.info('Writing data to file...')
output = open(os.path.join(pathWorkDir, pklDqmFile), 'wb')
pickle.dump(dqmData, output)
output.close()
logger = logging.getLogger('full')
logger.info('Written ' + os.path.join(pathWorkDir, pklDqmFile))

# Save the total number of tracks
logger.info('Writing totalTracks number to file...')
output = open(os.path.join(pathWorkDir, pklTracksFile), 'wb')
pickle.dump(totalTracks, output)
output.close()
logger = logging.getLogger('full')
logger.info('Written ' + os.path.join(pathWorkDir, pklTracksFile))

cur.close()
db.close()
logger.info('Finished')
