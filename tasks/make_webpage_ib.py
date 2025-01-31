# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 12:17:38 2015

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]

Make the index.html webpage with the main Monitor table
This code in use since the Database is in place
"""
import logging
from datetime import datetime
from e3monitor.tasks.update_time import (compute_update,
                                         day_of_run)
from e3monitor.tasks.set_version import set_version
from e3monitor.config.__limits__ import (
    TRANSFER_SEC_LIMIT,
    ELOG_WARNING,
    ELOG_ERROR,
    TRACKS_ERROR_HIGH,
    TRACKS_WARNING_HIGH,
    TRACKS_WARNING_LOW,
    TRACKS_ERROR_LOW
    )
from e3monitor.table_headers.__html_headers__ import (
    HEADER_HTML,
    TABELLA1_HTML,
    TABELLA1_P2_HTML,
    FOOTER_HTML,
    BOTTOM_HTML
    )


def make_webpage_ib(monitorData,
                    totalTracks,
                    EEE_ACTIVE_STATIONS,
                    mainWebPageFile):
    '''Make the index.html webpage with the main Monitor table
    '''

    # Start logger
    logger = logging.getLogger('plain')
    logger.info('Function make_webpage_index() started')

    # Define now
    now = datetime.today()

    # Open index.html
    w = open(mainWebPageFile, 'w')

    # Write html headers and titles of the table
    w.write(HEADER_HTML)
    w.write(compute_update())
    w.write(TABELLA1_HTML)
    # Day of run 
    w.write(day_of_run())
    ### Generic message
    #w.write('<h2 style="margin:0;">[EEE Monitor info] <i>RUN 2 ended on May 20, 2016.</i></h2>')
    #w.write('<h2 style="margin:0;">[EEE Monitor info] <i>RUN 3 will start in autumn.</i></h2>')
    #w.write('<h3 style="margin-top:3px;"><i>RUN 2 ended on May 20, 2016. RUN 3 will start in autumn.</i></h3>')
    w.write("<h3>Total number of candidate tracks (X^2<10) in the database: ")
    w.write(str(totalTracks) + "</h3>")
    w.write(TABELLA1_P2_HTML)

    # Start loop for school names (sorted)
    for schoolName in sorted(monitorData.get_allData()):

        # Skip schools with no data
        if schoolName not in EEE_ACTIVE_STATIONS:
            continue

        # Get Transfer timestamp and set <tr> class color
        try:
            transferDelay = now - monitorData.get_transferTs(schoolName)
        except:
            transferDelay = -1

        # Set <tr> class color
        if transferDelay == -1:
            rowColor = 'red_ib'
            transfer_time_txt = 'red_ib'
        elif transferDelay.days == 0:
            if transferDelay.seconds < TRANSFER_SEC_LIMIT:
                transfer_time_txt = 'green'
                try:
                    _tracks = round(monitorData.get_trackRate(schoolName))
                    if (_tracks < TRACKS_ERROR_LOW or
                            _tracks > TRACKS_ERROR_HIGH):
                        rowColor = 'red_ib'
                    elif (_tracks < TRACKS_WARNING_LOW or
                            _tracks > TRACKS_WARNING_HIGH):
                        rowColor = 'yellow_ib'
                    else:
                        rowColor = 'green'
                except:
                    rowColor = 'red_ib'
                    continue
            else:
                transfer_time_txt = 'yellow_ib'
                try:
                    _tracks = round(monitorData.get_trackRate(schoolName))
                    if (_tracks < TRACKS_ERROR_LOW or
                            _tracks > TRACKS_ERROR_HIGH):
                        rowColor = 'red_ib'
                    else:
                        rowColor = 'yellow_ib'
                except:
                    rowColor = 'red_ib'
                    continue
        elif transferDelay.days == 1:
            transfer_time_txt = 'yellow_ib'
            try:
                _tracks = round(monitorData.get_trackRate(schoolName))
                if (_tracks < TRACKS_ERROR_LOW or
                        _tracks > TRACKS_ERROR_HIGH):
                    rowColor = 'red_ib'
                else:
                    rowColor = 'yellow_ib'
            except:
                rowColor = 'yellow_ib'
                continue
        else:
            rowColor = 'red_ib'
            transfer_time_txt = 'red_ib'
        ## Print only green telescopes :-)
        #if rowColor != 'green':
        #    continue
        w.write('<tr class=\"' + rowColor + '\">')

        # Print School Name in format: TEST-01
        w.write('<td>')
        w.write('<span class=\"bold\">')
        w.write(schoolName)
        w.write('</span>')
        w.write('</td>')

        # Print Day of the last transferred file at CNAF
        w.write('<td>')
        w.write('<span class=\"' + transfer_time_txt + '">')
        try:
            w.write(monitorData.get_transferTs(schoolName).strftime("%a %d"))
            w.write('<br />')
            w.write(monitorData.get_transferTs(schoolName).strftime("%B"))
        except:
            w.write('')
        w.write('</span>')
        w.write('</td>')

        # Print Hour of the last transferred file at CNAF
        w.write('<td>')
        w.write('<span class=\"' + transfer_time_txt + '">')
        try:
            w.write(monitorData.get_transferTs(schoolName).strftime("%H:%M"))
        except:
            w.write('')
        w.write('</span>')
        w.write('</td>')

        # Print "Nome dell'ultimo File trasferito"
        w.write('<td>')
        w.write('<span class=\"' + transfer_time_txt + '">')
        try:
            w.write(monitorData.get_transferFileName(schoolName)[:13] +
                    '<br />' +
                    monitorData.get_transferFileName(schoolName)[13:])
            if (monitorData.get_transferFileName(schoolName) is not ''):
                w.write('.bin')
        except:
            w.write('')
        w.write('</span>')
        w.write('</td>')

        # Print 'numero di files trasferiti oggi'
        w.write('<td>')
        try:
            w.write(str(monitorData.get_transferFileNum(schoolName)))
        except:
            w.write('*')
        w.write('<br /><a href=\"plots/' + schoolName + '.png\">[History]</a>')
        w.write('</td>')

        # Print "Ultima Entry nell'e-logbook delle Scuole"
        w.write('<td>')
        try:
            elogDelay = now - monitorData.get_elogEntryTs(schoolName)
            if elogDelay.days <= ELOG_WARNING:
                elog_time_txt = 'gray'
            elif elogDelay.days <= ELOG_ERROR:
                elog_time_txt = 'yellow_ib'
            else:
                elog_time_txt = 'red_ib'
            w.write('<span class=\"' + elog_time_txt + '\">')
            w.write(monitorData.get_elogEntryTs(
                schoolName).strftime("%H:%M"))
            w.write('<br />')
            w.write(monitorData.get_elogEntryTs(
                schoolName).strftime("%d/%m/%Y"))
            w.write('</span>')
        except:
            w.write('*')
        w.write('</td>')

        # Print "Nome dell'ultimo File analizzato dal DQM"
        w.write('<td>')
        try:
            w.write(monitorData.get_DqmFileName(schoolName)[:13] + '<br />' +
                    monitorData.get_DqmFileName(schoolName)[13:])
            if (monitorData.get_DqmFileName(schoolName) is not ''):
                w.write('.bin')
        except:
            w.write('*')
        w.write('</td>')

        # Print "Report giornaliero DQM"
        w.write('<td>')
        try:
            _dqmreportTs = datetime.strptime(
                monitorData.get_dqmreportTs(schoolName), '%Y-%m-%d')
            w.write('<a href=\"dqmreport/' + schoolName + '/')
            w.write(monitorData.get_dqmreportTs(schoolName))
            w.write('/\">')
            w.write(_dqmreportTs.strftime("%d/%m"))
            w.write('</a> <br />')
            w.write('<a href =\"dqmreport/' + schoolName + '/?C=M;O=D\">')
            w.write('[History]')
            w.write('</a>')
        except:
            w.write('*')
        w.write('</td>')

        # Print triggers
        w.write('<td>')
        try:
            _triggers = round(monitorData.get_triggerRate(schoolName))
            if (_triggers < TRACKS_ERROR_LOW or
                    _triggers > TRACKS_ERROR_HIGH):
                triggers_txt = 'red_ib'
            elif (_triggers < TRACKS_WARNING_LOW or
                    _triggers > TRACKS_WARNING_HIGH):
                triggers_txt = 'yellow_ib'
            else:
                triggers_txt = 'gray'
            w.write('<span class=\"' + triggers_txt + '\">')
            w.write(str(_triggers))
            w.write('</span>')
        except:
            w.write('*')
        w.write('</td>')

        # Print tracks (chi^2 < 10)
        w.write('<td>')
        try:
            _tracks = round(monitorData.get_trackRate(schoolName))
            if (_tracks < TRACKS_ERROR_LOW or
                    _tracks > TRACKS_ERROR_HIGH):
                tracks_txt = 'red_ib'
            elif (_tracks < TRACKS_WARNING_LOW or
                    _tracks > TRACKS_WARNING_HIGH):
                tracks_txt = 'yellow_ib'
            else:
                tracks_txt = 'gray'
            w.write('<span class=\"' + tracks_txt + '\">')
            w.write(str(_tracks))
            w.write('</span>')
        except:
            w.write('*')
        w.write('</td>')

        # Print link to DMQ directory
        w.write('<td>')
        w.write('<a href=\"dqm/' + schoolName + '/?C=M;O=D\">')
        w.write(schoolName)
        w.write('</a>')
        w.write('</td>')

        # End loop for school names
        w.write('</tr>\n')

    w.write('</table>')
    w.write(FOOTER_HTML)
    w.write(set_version())
    w.write(BOTTOM_HTML)
    w.close()
    logger.info('Function make_webpage_index() finished')
    return True
