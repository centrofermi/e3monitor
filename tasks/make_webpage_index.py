# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 12:17:38 2015

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]

Make the index.html webpage with the main Monitor table
"""

import logging
from e3monitor.tasks.update_time import compute_update
from e3monitor.tasks.set_version import set_version
from e3monitor.config.__limits__ import SEC_TRANSFER_LIMIT
from e3monitor.html.__html_headers__ import (HEADER_HTML,
                                             TABELLA1_HTML,
                                             FOOTER_HTML,
                                             BOTTOM_HTML)


def make_webpage_index(monitorData, mainWebPageFileBeta):
    '''Make the index.html webpage with the main Monitor table
    '''

    logger = logging.getLogger('plain')
    logger.info('Function make_webpage_index() started')

    # Open index.html
    w = open(mainWebPageFileBeta, 'w')

    # Write html headers and titles of the table
    w.write(HEADER_HTML)
    w.write(compute_update())
    w.write(TABELLA1_HTML)

    # Start loop for school names (sorted)
    for schoolName in sorted(monitorData.get_allData()):

        # Set <tr> class color
        if monitorData.get_transferDelayDays(schoolName) == 0:
            if monitorData.get_transferDelaySeconds(schoolName) < SEC_TRANSFER_LIMIT:
                rowColor = 'green'
                transfer_time_txt = 'green'
            else:
                rowColor = 'yellow'
                transfer_time_txt = 'yellow'
        elif monitorData.get_transferDelayDays(schoolName) == 1:
            rowColor = 'yellow'
            transfer_time_txt = 'yellow'
        else:
            rowColor = 'red'
            transfer_time_txt = 'red'
        w.write('<tr class=\"' + rowColor + '\">')

        # Print School Name in format: TEST-01
        w.write('<td>')
        w.write('<span class=\"bold\">')
        w.write(schoolName)
        w.write('</span>')
        w.write('</td>')

        # Print Day of the last transferred file at CNAF
        w.write('<td>')
        w.write('<span class=\"' + transfer_time_txt  + '">')
        try:
            w.write(monitorData.get_transferTs(schoolName).strftime("%a %d"))
            w.write('<br />')
            w.write(monitorData.get_transferTs(schoolName).strftime("%B"))
        except:
            w.write('*')
        w.write('</td>')

        # Print Hour of the last transferred file at CNAF
        w.write('<td>')
        w.write('<span class=\"' + transfer_time_txt  + '">')
        try:
            w.write(monitorData.get_transferTs(schoolName).strftime("%H:%M"))
        except:
            w.write('*')
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
