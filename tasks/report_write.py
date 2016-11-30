# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 16:56:29 2016

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
"""
import logging
import os
from datetime import datetime
from e3monitor.tasks.update_time import(day_run)


def intWithCommas(x):
    ''' Print integer with commas for old python
    '''
    if type(x) not in [type(0), type(0L)]:
        raise TypeError("Parameter must be an integer.")
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return "%d%s" % (x, result)


def report_write(reportData,
                 totalTracks,
                 EEE_ACTIVE_STATIONS,
                 pathWorkDir,
                 htmlReportFile):
    '''Read the reportData class and write the html report file
    '''

    # Array of schools with no problems
    schoolsOk = []
    schoolsTrackRed = []
    schoolsTrackYellow = []
    schoolsTransferRed = []
    schoolsTransferYellow = []
    schoolsElog = []
    schoolsMsg = []

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
            (reportData.get_trackStatus(schoolName) == 0) and \
                (reportData.get_trackStatus(schoolName) == 0):
                    schoolsOk.append(schoolName)

        # Check stations: transfer data Red
        if (reportData.get_transferDelayStatus(schoolName) == 2):
            schoolsTransferRed.append(schoolName)
        # Check stations: transfer data Yellow
        elif (reportData.get_transferDelayStatus(schoolName) == 1):
             schoolsTransferYellow.append(schoolName)
        # Check stations: if transfer is fine then track rate Red
        elif (reportData.get_trackStatus(schoolName) == -2):
             schoolsTrackRed.append(schoolName)
        # Check stations: if transfer is fine then track rate yellow
        elif (reportData.get_trackStatus(schoolName) == -1):
             schoolsTrackYellow.append(schoolName)

        # Check stations: elog Red
        if (reportData.get_elogEntryStatus(schoolName) == 2):
            schoolsElog.append(schoolName)

        # Check if there are messages for a telescope
        if reportData.get_message(schoolName) != '':
            schoolsMsg.append('   - ' + schoolName + ': ' + reportData.get_message(schoolName))

    # End of loop on schools

    # Open html file for writing
    logger.info('Opening html file for writing')
    w = open(os.path.join(pathWorkDir, htmlReportFile), 'w')
    logger.info(w)

    ################################################
    # Write the beginnig of the html file
    ################################################
    w.write('Shift Report di ')
    w.write(todayStr)
    w.write(' - RUN 3 (data taking): Giorno ')
    w.write(day_run())
    w.write('''
********************************************
NEVER REPLY TO THIS LIST!!
Please reply only to runcoord@centrofermi.it
********************************************

Come annunciato nel meeting di collaborazione EEE aperto alle scuole di ieri,
vi inviamo -da oggi- il report generato automaticamente sullo stato dei telescopi.
IMPORTANTE: non rispondete mai a questo email, per qualsisi questione
potete scrivere agli indirizzi riportati in fondo a questo messaggio.

Alle ore 8:00 di questa mattina, la situazione delle scuole risulta la seguente:\n
''')

    ################################################
    # Write the list of schools that are ok (green)
    ################################################
    if len(schoolsOk) > 1:
        w.write('- Ci sono ')
        w.write(str(len(schoolsOk)))
        w.write(' telescopi in trasmissione attiva e con parametri dei dati che sembrano buoni:\n')
        w.write(', '.join(map(str, schoolsOk)))
        w.write('.\n\n')
    elif len(schoolsOk) == 1:
        w.write('- C\'e\' un telescopio in trasmissione attiva e con parametri dei dati che sembrano buoni:\n')
        w.write(schoolsOk[0])
        w.write('.\n\n')
    else:
        w.write('Nessun telescopio mi risulta attivo, deve esserci un errore di sistema o un problema al CNAF.\n')

    ################################################
    # Write the list of schools with track rate yellow (yellow)
    ################################################
    if len(schoolsTrackYellow) > 1:
        w.write('- Ci sono ')
        w.write(str(len(schoolsTrackYellow)))
        w.write(' telescopi in trasmissione, con un rate di acquisizione delle tracce minore di 10 Hz:\n')
        w.write(', '.join(map(str, schoolsTrackYellow)))
        w.write('.\n\n')
    elif len(schoolsTrackYellow) == 1:
        w.write('- C\'e\' un telescopio in trasmissione, con un rate di acquisizione delle tracce minore di 10 Hz:\n')
        w.write(schoolsTrackYellow[0])
        w.write('.\n\n')

    ################################################
    # Write the list of schools with track rate very low (red)
    ################################################
    if len(schoolsTrackRed) > 1:
        w.write('- Ci sono ')
        w.write(str(len(schoolsTrackRed)))
        w.write(' telescopi in trasmissione, ma hanno un rate di acquisizione delle tracce inferiore a 5 Hz:\n')
        w.write(', '.join(map(str, schoolsTrackRed)))
        w.write('.\n\n')
    elif len(schoolsTrackRed) == 1:
        w.write('- C\'e\' un telescopio in trasmissione, ma ha un rate di acquisizione delle tracce inferiore a 5 Hz:\n')
        w.write(schoolsTrackRed[0])
        w.write('.\n\n')

    ################################################
    # Write the list of schools with yellow transfer
    ################################################
    if len(schoolsTransferYellow) > 1:
        w.write('- Ci sono ')
        w.write(str(len(schoolsTransferYellow)))
        w.write(' telescopi che non trasmettono dati al CNAF da piu\' di tre ore:\n')
        w.write(', '.join(map(str, schoolsTransferYellow)))
        w.write('.\n\n')
    elif len(schoolsTransferYellow) == 1:
        w.write('C\'e\' un telescopio che non trasmette dati al CNAF da piu\' di tre ore:\n')
        w.write(schoolsTransferYellow[0])
        w.write('.\n\n')

    ################################################
    # Write the list of schools with red transfer
    ################################################
    if len(schoolsTransferRed) > 1:
        w.write('- Ci sono ')
        w.write(str(len(schoolsTransferRed)))
        w.write(' telescopi che non trasmettono dati al CNAF da piu\' di due giorni:\n')
        w.write(', '.join(map(str, schoolsTransferRed)))
        w.write('.\n\n')
    elif len(schoolsTransferRed) == 1:
        w.write('C\'e\' un telescopio che non e\' in trasmissione da piu\' di due giorni:\n')
        w.write(schoolsTransferRed[0])
        w.write('.\n\n')

    ################################################
    # Write the list of schools with elog red
    ################################################
    if len(schoolsElog) > 1:
        w.write('- Ci sono ')
        w.write(str(len(schoolsElog)))
        w.write(' scuole che non compilano l\'elogbook da piu\' di due giorni:\n')
        w.write(', '.join(map(str, schoolsElog)))
        w.write('.\n\n')
    elif len(schoolsElog) == 1:
        w.write('C\'e\' una scuola che non compila l\'elogbook da piu\' di due giorni:\n')
        w.write(schoolsElog[0])
        w.write('.\n')

    ################################################
    # Message about elog for all schools
    ################################################
    w.write('Tutte le scuole sono invitate a compilare ogni giorno l\'e-logbook del Run 3\n')
    w.write('al seguente indirizzo: http://eee.centrofermi.it/elog/Run3\n\n')

    ################################################
    # Write Messages for schools if any
    ################################################
    if len(schoolsMsg) > 0:
        w.write('- Riportiamo i seguenti messaggi:\n')
        w.write('(per modificarli: http://eee.centrofermi.it/monitor/report)\n')
        w.write('\n'.join(map(str, schoolsMsg)))
        w.write('\n\n')

    ################################################
    # Write the number of total tracks
    ################################################
    w.write('Numero totale di Muoni (tracce di Muoni con X^2<10) rilevati dalla rete dei telescopi EEE fino ad oggi: ')
    w.write(intWithCommas(totalTracks))
    w.write(' [Wow!!]\n')
    w.write('Consulta il grafico aggiornato: http://eee.centrofermi.it/monitor/plots/tracks.png\n')
    w.write('Puoi scaricare il file Excel con tutti i dati delle 8:00 del mattino a questo link:\n')
    w.write('http://eee.centrofermi.it/monitor/shifter_report.xlsx\n')

    ################################################
    # Write the END of the html file
    ################################################
    w.write('''
<<<<< Link utili >>>>>
EEE Monitor: http://eee.centrofermi.it/monitor
E-logbook scuole: http://eee.centrofermi.it/elog/Run3

<<<<< Per rispondere o fare domande >>>>>
Per rispondere al presente messaggio, o per fare domande,
scrivere solo a: runcoord@centrofermi.it

<<<<< Per cancellarsi dalla mailing-list >>>>>
Mandare un email con il subject "UNSUBSCRIBE"
a: fabrizio.coccetti@centrofermi.it

EEE Report, il sistema automatico di generazione degli Shift Report di EEE,
ti saluta e ti augura una buona giornata!! 
https://github.com/centrofermi/e3monitor
    ''')

    # Close html file
    w.close()
    logger.info('html file written')
    # End
    logger.info('Function report_write() finished.')
    return True
