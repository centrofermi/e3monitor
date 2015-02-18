# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 19:55:46 2015

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
"""
from datetime import datetime
import logging
from e3monitor.tasks.update_time import compute_update
from e3monitor.tasks.set_version import set_version
from e3monitor.db.E3W3MonitorSchools import E3W3MonitorSchools
from e3monitor.config.__files_server__ import pklMonitorFile, pathWorkDir


def write_monitor_data(lastEntryPerSchool,
                       lastDqmreport,
                       schoolsDqmreportList,
                       transferData,
                       dqmData,
                       EEE_EXCLUDED_STATIONS):
    '''Write a dictionary with the All the monitor data
    '''

    logger = logging.getLogger('plain')
    logger.info('Function write_monitor_data() started')

    # Define class for saving all monitor data
    monitorData = E3W3MonitorSchools()

    # Define now
    now = datetime.today()

    for schoolName in transferData.AllData().iterkeys():
        if schoolName in EEE_EXCLUDED_STATIONS:
            continue

        # Initialize School List
        monitorData.init_School(schoolName)

        # Compute delay of the last transferred file at CNAF
        try:
            timeDiff = now - transferData.transfer_timestamp(schoolName)
            monitorData.set_transferDelayDays(schoolName, timeDiff.days)
            monitorData.set_transferDelaySeconds(schoolName, timeDiff.seconds)
        except:
            print(schoolName + "  <-- Error")
        print(monitorData.get_transferDelayDays(schoolName))
        print(monitorData.get_transferDelaySeconds(schoolName))

    logger.info('Function write_monitor_data() finished')
    return True
