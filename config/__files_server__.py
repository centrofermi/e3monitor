# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 14:24:40 2014

@author: Fabrizio Coccetti
"""
#
# File to open on vm193 at CNAF
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
mainWebPageFileBeta = "/var/www/html/monitor/index2.html"
cnafWebPageFile = "/var/www/html/monitor/index_cnaf.html"
ibWebPageFile = "/var/www/html/monitor/ib.html"

# xslx File to write
xlsxFile = "/var/www/html/monitor/shifter_report.xlsx"

# Config File for logging module
logConfigFile = "/opt/eee/e3monitor/config/logConf.ini"

# Config File for database
dbConfigFile = "/opt/eee/e3monitor/config/database.ini"

# Name of the Data pickle File storing Transfer entries from DB
pklTransferFile = "transfer_db_data.pkl"

# Name of the Data pickle File storing Transfer entries from DB
pklDqmFile = "dqm_db_data.pkl"

# Name of the pickle File with all the Monitor data
pklMonitorFile = "monitor_data.pkl"

# Path of the Working directory
pathWorkDir = '/opt/eee/e3monitor_work'

# Path of Dqm and Dqmreport
pathDqm = "/var/www/html/monitor/dqm"
pathDqmreport = "/var/www/html/monitor/dqmreport"

# Path of the directory where we save transferred files plots
pathSaveFig = '/var/www/html/monitor/plots/'

# Path of the MIDAS elogbook .log files
elogBookPath = "/usr/local/elog/logbooks/Run2/"

