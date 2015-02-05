# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 14:24:40 2014

@author: Fabrizio Coccetti
"""
#
# File to open on www.centrofermi.it
#

# Last file with run transfer data
lastTestFile = "/home/noferini/test/lastTest"

# Last file with the CNAF info
lastDataFile = "/home/noferini/test/lastData"

# Last file with the number of transferred file from schools per day
lastTransferredFile = "/home/noferini/test/nfilePerDay"

# In this csv file we write the data extracted from elog .log files
# and read it to make the e3w3 webpage
elogCsvFile = "/var/www/html/monitor/EEE_data.csv"

# Web pages to write
mainWebPageFile = "/var/www/html/monitor/index.html"
cnafWebPageFile = "/var/www/html/monitor/index_cnaf.html"

# xslx File to write
xlsFile = "/var/www/html/monitor/shifter_report.xlsx"

# Config File for logging module
logConfigFile = "/opt/eee/e3monitor/config/logConf.ini"

# Config File for database
dbConfigFile = "/opt/eee/e3monitor/config/database.ini"

# Name of the Data pickle File
plkDataFile = "data.pkl"

# Path of the Working directory
pathWorkDir = '/opt/eee/e3monitor_work'

# Path of Dqm and Dqmreport
pathDqm = "/var/www/html/monitor/dqm"
pathDqmreport = "/var/www/html/monitor/dqmreport"

# Path of the directory where we save transferred files plots
pathSaveFig = '/var/www/html/monitor/plots/'

# Path of the MIDAS elogbook .log files
elogBookPath = "/usr/local/elog/logbooks/EEE e-log/"
