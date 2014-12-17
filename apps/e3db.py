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
cur.execute(query)
schoolNames = cur.fetchall()
schoolNames.sort()
print(schoolNames)

# cur.execute("SELECT TOP1 * FROM run_table ORDER BY run_start DESC")
# query = "SELECT * FROM run_table WHERE unique_run_id REGEXP '^" + \
#        schoolNumber + "' ORDER BY unique_run_id DESC LIMIT 1;"
# SELECT * FROM run_table WHERE station_name = 'ALTA-01'
# ORDER BY unique_run_id DESC LIMIT 1;
# query = "SELECT * FROM run_table WHERE unique_run_id REGEXP '^" + \
#        schoolNumber + "[0-9]{9}$' ORDER BY unique_run_id DESC LIMIT 1;"
for _schoolName in schoolNames:
    query = "SELECT * FROM run_table WHERE station_name = " + \
        _schoolName + "ORDER BY unique_run_id DESC LIMIT 1;"
    cur.execute(query)
    # print all the first cell of all the rows
    param = cur.fetchone()
    print(param)

logger = logging.getLogger('full')
logger.info('Finished')
