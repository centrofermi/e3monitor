#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 10:00:00 2016

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
Make the index webpage for the the daily report archive

Order of usage for the EEE Daily Report:
1. e3reportAnalyze.py
2. e3reportWrite.py
3. e3reportSend.py
4. e3reportWebIndex.py
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
                                               archiveReportDir)

# Set up logging
logging.config.fileConfig(logConfigFile)
logger = logging.getLogger('full')
logger.info('Started')
logger = logging.getLogger('plain')

# Set locale to Italian
locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')

HTML_TOP = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="it" xml:lang="it" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<meta name="author" content="Fabrizio Coccetti" />
<meta name="generator" content="e3report" />
<meta http-equiv="REFRESH" content="60"/>
<meta http-equiv="Expires" content="0"/>
<meta http-equiv="PRAGMA" content="NO-CACHE"/>
<title>EEE Report -
Museo Storico della Fisica e Centro Studi e Ricerche Enrico Fermi</title>
<link href="favicon.ico" rel="shortcut icon" type="image/vnd.microsoft.icon" />
<link rel="stylesheet" type="text/css"
href="https://fonts.googleapis.com/css?family=Ubuntu:regular,bold&subset=Latin">
<link href="../e3monitor.css" rel="stylesheet" type="text/css" />
</head>
<body>
<div>
<img src="http://www.centrofermi.it/docs/images/banner_centro_fermi.jpg"
alt="banner CF" width="900" height="120" /></div>
"""

HTML_BOTTOM = """
<p>&nbsp;<p>
<div id="footer">
<p>&nbsp;<p>
<p>Webpage made by&nbsp;
<a href="https://github.com/centrofermi/e3monitor">e3monitor</a>&nbsp;
[<a href="https://github.com/centrofermi/e3monitor/wiki/Architecture">architecture</a>]
&nbsp;[<a href="https://github.com/centrofermi/e3monitor/wiki">wiki</a>]
</p> <!-- close paragraph in footer -->
</div> <!-- close footer -->
</body>
</html>
"""
HTML_TITLE = '''
<h2><i>Progetto Extreme Energy Events - La Scienza nelle Scuole</i></h2>
<h1>EEE Shift Report: Archivio giornaliero</h1>
'''

# Make webpage
w = open(os.path.join(archiveReportDir, 'index.html'), 'w')
w.write(HTML_TOP)
w.write(HTML_TITLE)
w.write('<div class=\"time\">Ultimo aggiornamento di questa pagina: ' +
        datetime.today().strftime("%A %d %B %Y") +
        ' alle ore '+datetime.today().strftime("%H:%M")+'.</div>')
w.write('<h2>[EEE Report] <i>Automatic Shift Report Archive</i></h2>')
w.write('<p>&nbsp;</p>')
w.write('<table style=\"width:700px;\"><tbody>')
w.write('<tr><th>Link ai Report giornalieri sullo stato dei Telescopi EEE</th></tr>')
# List txt files
for reportName in sorted(os.listdir(archiveReportDir), reverse=True):
    if reportName.endswith(".txt"):
        reportDate = datetime.strptime(reportName, 'report_message_%Y-%m-%d.txt')
        w.write('<tr class=\"gray\"><td><div style=\"font-size:20px;text-align:left;margin-left:55px;\"> <a href=\"./' + reportName + '\">Shift Report inviato il giorno: <span style=\"font-weight:bold;\">' + reportDate.strftime("%A %d %B %Y") + '</span></a></div></td></tr>')
w.write('</tbody></table>')
w.write(HTML_BOTTOM)
w.close()

# End
logger.info('Finished')

