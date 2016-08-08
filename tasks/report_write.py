# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 16:56:29 2016

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
"""
import logging
import os
from datetime import datetime
from e3monitor.tasks.update_time import(day_of_run)


def report_write(reportData,
                 EEE_ACTIVE_STATIONS,
                 pathWorkDir,
                 htmlReportFile):
    '''Read the reportData class and write the html report file
    '''

    # Start logger
    logger = logging.getLogger('plain')
    logger.info('Function report_write() started.')

    # Define now
    today = datetime.today()
    todayStr = today.strftime("%a %d %B %Y")

    # Start loop for school names (sorted)
    for schoolName in sorted(reportData.get_allData()):

        # Skip schools with no data
        if schoolName not in EEE_ACTIVE_STATIONS:
            continue

        # Check green stations (with no errors)
        if (reportData.get_transferDelayStatus(schoolName) == 0) and \
            (reportData.get_triggerStatus(schoolName) == 0) and \
                (reportData.get_trackStatus(schoolName) == 0):
                    print(schoolName)

    # Open html file for writing
    logger.info('Opening html file for writing')
    w = open(os.path.join(pathWorkDir, htmlReportFile), 'w')
    logger.info(w)
    w.write('Shift Report di ')
    w.write(todayStr)
    w.write('- RUN 2: Giorno ')
    w.write(day_of_run())

    w.write('''
****************************
NEVER REPLY TO THIS LIST!!
Please reply only to runcoord@centrofermi.it
****************************

Alle ore 8:00 del mattino, la situazione delle scuole risulta la seguente:
''')

    w.write('''
<<<<< Link utili >>>>>
EEE Monitor: http://eee.centrofermi.it/monitor
E-logbook scuole: http://www.centrofermi.it/elog/Run3

<<<<< Per rispondere >>>>>
Se si vuole rispondere al presente messaggio,
scrivere solo al mittente e a: runcoord@centrofermi.it

<<<<< Per cancellarsi dalla mailing-list >>>>>
Mandare un email con il subject “UNSUBSCRIBE”
a: fabrizio.coccetti@centrofermi.it
    ''')

    # Close html file
    w.close()
    logger.info('html file written')
    # End
    logger.info('Function report_write() finished.')
    return True
