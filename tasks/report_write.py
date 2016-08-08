# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 16:56:29 2016

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
"""
import logging
from datetime import datetime


def report_write(reportData,
                 EEE_ACTIVE_STATIONS,
                 htmlReportFile):
    '''Read the reportData class and write the html report file
    '''

    # Start logger
    logger = logging.getLogger('plain')
    logger.info('Function report_write() started.')

    # Define now
    now = datetime.today()

    # Start loop for school names (sorted)
    for schoolName in sorted(reportData.get_allData()):

        # Skip schools with no data
        if schoolName not in EEE_ACTIVE_STATIONS:
            continue

        # Check green stations (with no errors)
        if (reportData.get_transferDelayStatus(schoolName) == 0) and \
            (reportData.triggerStatus(schoolName) == 0) and \
            (reportData.trackStatus(schoolName) == 0):
                print(schoolName)

    # End
    logger.info('Function report_write() finished.')
    return True
