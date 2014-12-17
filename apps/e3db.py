#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 11:08:30 2014

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
"""

import MySQLdb
import ConfigParser
import logging
import logging.config
from e3monitor.config.__files_server__ import logConfigFile, dbConfigFile

# List with the name of the Schools
schoolNames = []
param = []

# Set up logging
logging.config.fileConfig(logConfigFile)
logger = logging.getLogger('full')
logger.info('Started')
logger = logging.getLogger('plain')

# Reading db ini file
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

# Connect to the School database and get the school name list
query = "SELECT name FROM telescope_id_table;"
logger.info('About to query: ' + query)
cur.execute(query)
schoolNames = [item[0] for item in cur.fetchall()]
sorted(schoolNames)

# Query for the last run data of each school
query = ("SELECT * FROM run_table WHERE station_name = %s "
         "ORDER BY unique_run_id DESC LIMIT 1;")
logger.info('About to query: ' + query)
for _schoolName in schoolNames:
    cur.execute(query, _schoolName)
    param = cur.fetchone()
    if param is None:
        continue
    # Assign parameter to the class

cur.close()
db.close()
logger = logging.getLogger('full')
logger.info('Finished')

