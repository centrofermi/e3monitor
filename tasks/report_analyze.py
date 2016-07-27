# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 17:17:00 2016

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]

Task to read the monitorData class and write the reportData class
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
from e3monitor.html.__html_headers__ import (
    HEADER_HTML,
    TABELLA1_HTML,
    TABELLA1_P2_HTML,
    FOOTER_HTML,
    BOTTOM_HTML
    )


def report_analyze(monitorData,
                   EEE_ACTIVE_STATIONS,
                   pklReportFile):
    '''Read the monitorData class and write the reportData class
    '''

    # Start logger
    logger = logging.getLogger('plain')
    logger.info('Function report_analyze() started.')

    # Define now
    now = datetime.today()


    # End
    logger.info('Function report_analyze() finished.')
    return True

