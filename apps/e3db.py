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

db = MySQLdb.connect(host=EEE_RUNDB2_CONF['host'],
                     user=EEE_RUNDB2_CONF['user'],
                     passwd=EEE_RUNDB2_CONF['passwd'],
                     db=EEE_RUNDB2_CONF['dbname'])

cur = db.cursor()

cur.execute("SELECT * FROM YOUR_TABLE_NAME")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]
