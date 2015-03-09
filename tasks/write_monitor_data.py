# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 19:55:46 2015

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
"""
from datetime import datetime
import logging
import os
import pickle
from e3monitor.db.E3Monitor import E3Monitor
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
    monitorData = E3Monitor()

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
            logger.info(schoolName + " <-- No transfer_timestamp found")

        # Name of last file transferred at CNAF
        try:
            _runNameInTranfer = (schoolName +
                                 transferData.transfer_timestamp(
                                     schoolName).strftime("-%Y-%m-%d-") +
                                 "{0:0>5}".format(
                                     int(transferData.run_id(schoolName))))
            monitorData.set_transferFileName(schoolName, _runNameInTranfer)
        except:
            logger.info(schoolName + " <-- No filename for transferred file")

        # Timestamp of the last transferred file ad CNAF
        try:
            monitorData.set_transferTs(
                schoolName,
                transferData.transfer_timestamp(schoolName))
        except:
            logger.info(schoolName + " <-- No transfer timestamp")

        # Number of files transfered today
        # TODO

        # Ultima Entry nell'e-logbook delle Scuole
        try:
            monitorData.set_elogEntryTs(
                schoolName,
                lastEntryPerSchool[schoolName])
        except:
            logger.info(schoolName + " <-- Error in last Elog Entry")

        # Name of last file analyzed by DQM
        try:
            _runNameInDqm = (schoolName +
                             dqmData.run_date(
                                 schoolName).strftime("-%Y-%m-%d-") +
                             "{0:0>5}".format(int(
                                 dqmData.run_id(schoolName))))
            monitorData.set_DqmFileName(schoolName, _runNameInDqm)
        except:
            logger.info(schoolName + " <-- No filename for last DQM file")

        # Daily report folder by DQM
        try:
            monitorData.set_dqmreportTs(schoolName, lastDqmreport[schoolName])
        except:
            logger.info(schoolName + " <-- No daily dqmreport")

        # Triggers of last Run
        try:
            monitorData.set_triggerRate(
                schoolName,
                dqmData.trigger_rate(schoolName))
        except:
            logger.info(schoolName + " <-- Error in trigger rate")

        # tracks (chi^2 < 10) last Run
        try:
            monitorData.set_trackRate(
                schoolName,
                dqmData.track_rate(schoolName))
        except:
            logger.info(schoolName + " <-- Error in track rate")

    # End loop for schoolName

    # Save the monitorData
    logger.info('Writing data to file...')
    output = open(os.path.join(pathWorkDir, pklMonitorFile), 'wb')
    pickle.dump(monitorData, output)
    output.close()
    logger = logging.getLogger('full')
    logger.info('Written ' + os.path.join(pathWorkDir, pklMonitorFile))

    logger.info('Function write_monitor_data() finished')
    return True
