# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 19:55:46 2015

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
"""
from datetime import datetime
import logging
from e3monitor.html.__html_headers__ import (HEADER_HTML,
                                             TABELLA1_HTML,
                                             FOOTER_HTML,
                                             BOTTOM_HTML)
from e3monitor.tasks.update_time import compute_update
from e3monitor.tasks.set_version import set_version
from e3monitor.config.__files_server__ import (mainWebPageFile)


def make_main_w3page(lastEntryPerSchool,
                     lastDqmreport,
                     schoolsDqmreportList,
                     transferData,
                     dqmData,
                     EEE_EXCLUDED_STATIONS):
    '''Make the index.html webpage with the Online main monitoring table
    '''

    logger = logging.getLogger('plain')
    logger.info('Function make_main_w3page() started')

    # Define now
    now = datetime.today()

    w = open('/var/www/html/monitor/index2.html', 'w')
    w.write(HEADER_HTML)
    w.write(compute_update())
    w.write(TABELLA1_HTML)

    for schoolName in transferData.AllData().iterkeys():
        if schoolName in EEE_EXCLUDED_STATIONS:
            continue
        try:
            timeDiff = now - transferData.transfer_timestamp(schoolName)
            print(schoolName)
            print(timeDiff.seconds)
            print(timeDiff.days)
        except:
            print(schoolName + "  <-- Error")
        # Set the color of the row of the table
        


    
    w.write('</table>')
    w.write(FOOTER_HTML)
    w.write(set_version())
    w.write(BOTTOM_HTML)
    w.close()
    logger.info('Function make_main_w3page() finished')
    return True
