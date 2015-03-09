#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *********************************************************************
# * Copyright (C) 2014 Fabrizio Coccetti                              *
# * fabrizio.coccetti@centrofermi.it  [www.fc8.net]                   *
# *                                                                   *
# * For the license terms see the file LICENSE, distributed           *
# * along with this software.                                         *
# *********************************************************************
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
Created on Mon Mar  9 20:17:29 2015

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]

This app writes the file with the E3Monitor class data
"""

import logging
import logging.config
from e3monitor.tasks.read_elog import read_schools_elog
from e3monitor.tasks.read_dqmreport import read_dqmreport
from e3monitor.tasks.read_pickle import read_pickle
from e3monitor.tasks.write_monitor_data import write_monitor_data
from e3monitor.config.__stations__ import (EEE_EXCLUDED_STATIONS,
                                           EEE_ACTIVE_STATIONS)
from e3monitor.config.__files_server__ import (logConfigFile,
                                               elogCsvFile,
                                               pathDqmreport,
                                               pathWorkDir,
                                               pklTransferFile,
                                               pklDqmFile)

if __name__ == '__main__':

    # Set logging options
    logging.config.fileConfig(logConfigFile)
    logger = logging.getLogger('full')
    logger.info('Started')

    # Determine the time and date of the last entry in the School's elogbook
    lastEntryPerSchool = read_schools_elog(elogCsvFile)

    # Find directory for the last daily dqmreport
    lastDqmreport, schoolsDqmreportList = \
        read_dqmreport(EEE_ACTIVE_STATIONS, pathDqmreport)

    # Read the pickle file with Transfer RUN info from the database
    transferData = read_pickle(pathWorkDir, pklTransferFile)
    logger.info("pickle file extracted from the"
                "database imported: transferData is loaded")

    # Read the pickle file with DQM RUN info from the database
    dqmData = read_pickle(pathWorkDir, pklDqmFile)
    logger.info("pickle file extracted from the"
                "database imported: dqmData is loaded")

    # Combine data into E3Monitor class and write pickle file
    write_monitor_data(lastEntryPerSchool,
                       lastDqmreport,
                       schoolsDqmreportList,
                       transferData,
                       dqmData,
                       EEE_EXCLUDED_STATIONS)

    # Final log message
    logger.info('Finished')
