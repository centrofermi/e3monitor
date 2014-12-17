#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 11:08:30 2014

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
"""

try:
    import MySQLdb
except ImportError:
    import pymysql
    pymysql.install_as_MySQLdb()
from e3monitor.config.__db__ import EEE_RUNDB2_CONF

schoolNumber = '28'
list = []

db = MySQLdb.connect(host=EEE_RUNDB2_CONF['host'],
                     user=EEE_RUNDB2_CONF['user'],
                     passwd=EEE_RUNDB2_CONF['pwd'],
                     db=EEE_RUNDB2_CONF['dbname'])

cur = db.cursor()

# cur.execute("SELECT TOP1 * FROM run_table ORDER BY run_start DESC")
#query = "SELECT * FROM run_table WHERE unique_run_id REGEXP '^" + \
#        schoolNumber + "' ORDER BY unique_run_id DESC LIMIT 1;"
query = "SELECT * FROM run_table WHERE unique_run_id REGEXP '^" + \
        schoolNumber + "[0-9]{9}$' ORDER BY unique_run_id DESC LIMIT 1;"
cur.execute(query)

# print all the first cell of all the rows
list = cur.fetchone()
print(list[0])
