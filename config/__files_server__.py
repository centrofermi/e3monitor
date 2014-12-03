# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 14:24:40 2014

@author: Fabrizio Coccetti
"""
#
# File to open on www.centrofermi.it
#

# Last file with run transfer data
lastTestFile = "/var/www/html_eee/netstatus/lastTest"

# Last file with the CNAF info
lastDataFile = "/var/www/html_eee/netstatus/lastData"

# Last file with the number of transferred file from schools per day
lastTransferredFile = "/var/www/html_eee/netstatus/nfilePerDay"

# In this csv file we write the data extracted from elog .log files
# and read it to make the e3w3 webpage
elogCsvFile = "/var/www/html_eee/monitor/EEE_data.csv"

# Web pages to write
mainWebPageFile = "/var/www/html_eee/monitor/index.html"
cnafWebPageFile = "/var/www/html_eee/monitor/index_cnaf.html"

# Path of Dqm and Dqmreport
pathDqm = "/var/www/html_eee/dqm"
pathDqmreport = "/var/www/html_eee/dqmreport"

# Path of the directory where we save transferred files plots
pathSaveFig = '/var/www/html_eee/monitor/plots/'

# Path of the MIDAS elogbook .log files
elogBookPath = "/usr/local/elog/logbooks/EEE e-log/"
