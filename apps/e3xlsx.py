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
Created on Thu Mar 12 16:04:09 2015

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]

This App writes the excel shifer-report
"""

import locale
import logging
import logging.config
from e3monitor.tasks.read_pickle import read_pickle
from e3monitor.tasks.make_shift_report_xlsx import make_shift_report_xlsx
from e3monitor.config.__stations__ import EEE_ACTIVE_STATIONS
from e3monitor.config.__files_server__ import (logConfigFile,
                                               pathWorkDir,
                                               pklMonitorFile,
                                               xlsxFile)

if __name__ == '__main__':

    # Set logging options
    logging.config.fileConfig(logConfigFile)
    logger = logging.getLogger('full')
    logger.info('Started')

    # Set locale to Italian
    locale.setlocale(locale.LC_ALL, 'it_IT')

    # Read the E3Monitor data
    monitorData = read_pickle(pathWorkDir, pklMonitorFile)
    logger.info("pickle file extracted from the "
                "database imported: E3Monitor class is loaded "
                "as monitorData")

    make_shift_report_xlsx(monitorData,
                           EEE_ACTIVE_STATIONS,
                           xlsxFile)

    # Final log message
    logger.info('Finished')
