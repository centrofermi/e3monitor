#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:00:00 2016

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
Send EEE email report via Gmail
This app analyze monitorData and writes a class to write the report

Order of usage for the EEE Daily Report:
1. e3reportAnalyze.py
2. e3reportWrite.py
3. e3reportSend.py
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import locale
import os
import ConfigParser
import logging
import logging.config
import shutil
from datetime import datetime
from e3monitor.config.__files_server__ import (logConfigFile,
                                               emailConfigFile,
                                               archiveReportDir,
                                               pathWorkDir,
                                               htmlReportFile)

# Set up logging
logging.config.fileConfig(logConfigFile)
logger = logging.getLogger('full')
logger.info('Started')
logger = logging.getLogger('plain')

# Set locale to Italian
locale.setlocale(locale.LC_ALL, 'it_IT')

# Reading Email Config File
logger.info('Reading ' + emailConfigFile)
parser = ConfigParser.ConfigParser()
parser.read(emailConfigFile)
smtpServer = parser.get('gmail', 'smtpServer')
smtpPort = parser.get('gmail', 'smtpPort')
emailFrom = parser.get('gmail', 'emailFrom')
emailTo = parser.get('gmail', 'emailTo')
passwd = parser.get('gmail', 'passwd')

# Create message container - the correct MIME type is multipart/alternative.
today = datetime.today()
todayStr = today.strftime("%a %d %B %Y")
_todayStr = today.strftime("%Y-%m-%d")
# # Use both html and text messages
# msg = MIMEMultipart('alternative')
# Record the MIME types of both parts - text/plain and text/html.
# part1 = MIMEText(textText, 'plain')
# part2 = MIMEText(htmlText, 'html')

# Create the body of the message (a plain-text and an HTML version).
#with open(os.path.join(pathWorkDir, htmlReportFile), 'r') as reportFile:
#    textText = reportFile.read().replace('\n', '')

# Open the file in plain text for the body message
fp = open(os.path.join(pathWorkDir, htmlReportFile), 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

# Use only txt message
# msg = MIMEText(textText, 'plain')

msg['Subject'] = "Report giornaliero di EEE - Situazione alle ore 8:00 di " + todayStr
msg['From'] = emailFrom
msg['To'] = emailTo

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
#msg.attach(part1)
#msg.attach(part2)

# Sending message
logger.info('Sending message via Gmail')
s = smtplib.SMTP(smtpServer + ":" + smtpPort)
s.starttls()
s.login(emailFrom, passwd)
s.sendmail(emailFrom, emailTo, msg.as_string())
s.quit()

logger.info('Sending email done')

# Renaming and archiving the report
logger.info('Renaming report for the archive')
_name = 'report_message_' + _todayStr + '.txt'
shutil.copy((os.path.join(pathWorkDir, htmlReportFile)), (os.path.join(archiveReportDir, _name)))
logger.info('Finished')

