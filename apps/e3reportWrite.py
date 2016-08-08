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
Created on Mon Aug 08 16:45:00 2016

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]

This app read the class monitorData and writes the report
"""

import locale
import logging
import logging.config
from e3monitor.tasks.read_pickle import read_pickle
from e3monitor.tasks.report_write import report_write
from e3monitor.config.__stations__ import EEE_ACTIVE_STATIONS
from e3monitor.config.__files_server__ import (logConfigFile,
                                               pathWorkDir,
                                               pklReportFile,
                                               htmlReportFile)

if __name__ == '__main__':

    # Set logging options
    logging.config.fileConfig(logConfigFile)
    logger = logging.getLogger('full')
    logger.info('Started')

    # Set locale to Italian
    locale.setlocale(locale.LC_ALL, 'it_IT')

    # Read the class E3Report data
    reportData = read_pickle(pathWorkDir, pklReportFile)
    logger.info("pickle file read: E3Report class is loaded "
                "as reportData")

    report_write(reportData,
                 EEE_ACTIVE_STATIONS,
                 htmlReportFile)

    # Final log message
    logger.info('Finished')
