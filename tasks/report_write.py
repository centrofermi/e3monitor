# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 16:56:29 2016

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
"""
import logging
import os
from datetime import datetime
from e3monitor.tasks.update_time import(day_run)


def report_write(reportData,
                 EEE_ACTIVE_STATIONS,
                 pathWorkDir,
                 htmlReportFile):
    '''Read the reportData class and write the html report file
    '''

    # Array of schools with no problems
    schoolsOk = []
    schoolsTriggerRed = []
    schoolsTransferRed = []
    schoolsElog = []

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
                    schoolsOk.append(schoolName)

        # Check stations: trigger Red
        if (reportData.get_triggerStatus(schoolName) == -2):
            schoolsTransferRed.append(schoolName)

        # Check stations: transfer data Red
        if (reportData.get_transferDelayStatus(schoolName) == 2):
            schoolsTransferRed.append(schoolName)

        # Check stations: elog Red
        if (reportData.get_elogEntryStatus(schoolName) == 2):
            schoolsElog.append(schoolName)


    # Open html file for writing
    logger.info('Opening html file for writing')
    w = open(os.path.join(pathWorkDir, htmlReportFile), 'w')
    logger.info(w)

    ################################################
    # Write the beginnig of the html file
    ################################################
    w.write('Shift Report di ')
    w.write(todayStr)
    w.write(' - RUN 3: Giorno ')
    w.write(day_run())
    w.write('''
********************************************
NEVER REPLY TO THIS LIST!!
Please reply only to runcoord@centrofermi.it
********************************************

Alle ore 8:00 del mattino, la situazione delle scuole risulta la seguente:\n
''')

    ################################################
    # Write the list of schools that are ok (green)
    ################################################
    w.write('- Ci sono ')
    w.write(str(len(schoolsOk)))
    w.write(' telescopi in trasmissione attiva e con parametri dei dati che sembrano buoni:\n')
    w.write(', '.join(map(str, schoolsOk)))
    w.write('.\n')

    ################################################
    # Write the list of schools with trigger very low (red)
    ################################################
    w.write('- Ci sono ')
    w.write(str(len(schoolsTriggerRed)))
    w.write(' telescopi che sono in trasmissione, ma hanno un rate inferiore a 5 Hz:\n')
    w.write(', '.join(map(str, schoolsTriggerRed)))
    w.write('.\n')

    ################################################
    # Write the list of schools with red transfer
    ################################################
    w.write('- Ci sono ')
    w.write(str(len(schoolsTransferRed)))
    w.write(' telescopi che non sono in trasmissione da più di due giorni:\n')
    w.write(', '.join(map(str, schoolsTransferRed)))
    w.write('.\n')

    ################################################
    # Write the list of schools with elog red
    ################################################
    w.write('- Ci sono ')
    w.write(str(len(schoolsElog)))
    w.write(' scuole che non compilano l\'elogbook da più di due giorni:\n')
    w.write(', '.join(map(str, schoolsElog)))
    w.write('.\n')

    ################################################
    # Write the END of the html file
    ################################################
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

e3report, il sistema automatico di generazione degli shift report,
ti augura una buona giornata e ti ricorda che è solo grazie a lui
che tu non devi più fare gli shift giornalieri.
    ''')

    # Close html file
    w.close()
    logger.info('html file written')
    # End
    logger.info('Function report_write() finished.')
    return True
