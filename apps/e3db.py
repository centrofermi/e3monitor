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

schoolNumber = '28'
list = []

logger.info('Connecting to %s on %s (as %s)' % (dbname, host, user))

db = MySQLdb.connect(host=host,
                     user=user,
                     passwd=passwd,
                     db=dbname)

cur = db.cursor()

# cur.execute("SELECT TOP1 * FROM run_table ORDER BY run_start DESC")
# query = "SELECT * FROM run_table WHERE unique_run_id REGEXP '^" + \
#        schoolNumber + "' ORDER BY unique_run_id DESC LIMIT 1;"
query = "SELECT * FROM run_table WHERE unique_run_id REGEXP '^" + \
        schoolNumber + "[0-9]{9}$' ORDER BY unique_run_id DESC LIMIT 1;"
cur.execute(query)

# print all the first cell of all the rows
list = cur.fetchone()
print(list)

logger = logging.getLogger('full')
logger.info('Finished')
