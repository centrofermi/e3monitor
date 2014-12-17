#!/usr/bin/env python
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
#
# Many thanks to Luca.Baldini@pi.infn.it
#
# Creation: 15 oct 2014
#
# Read info about runs, schools' elog, Dqm and Dqmreport and
# make the main webpage index.html

import locale
import logging
import logging.config
from e3monitor.config.__stations__ import EEE_ACTIVE_STATIONS
from e3monitor.tasks.read_elog import read_schools_elog
from e3monitor.tasks.read_dqm import read_dqm_summary
from e3monitor.tasks.read_dqmreport import read_dqmreport
from e3monitor.tasks.read_pickle import read_pickle
from e3monitor.db.E3SchoolsData import E3SchoolsData
from e3monitor.tasks.make_main_page import make_main_page
from e3monitor.config.__files_server__ import (pathDqm,
                                               pathDqmreport,
                                               elogCsvFile,
                                               logConfigFile)


if __name__ == '__main__':

    # Set logging options
    logging.config.fileConfig(logConfigFile)
    logger = logging.getLogger('full')
    logger.info('Started')

    # Set locale to Italian
    locale.setlocale(locale.LC_ALL, 'it_IT')

    # Determine the time and date of the last entry in the School's elogbook
    lastEntryPerSchool = read_schools_elog(elogCsvFile)

    # Determine the content of DQM .summary files for each school
    # and the list of schools that actually have a DQM directory
    runSchoolsSummary, schoolsDqmList = \
        read_dqm_summary(EEE_ACTIVE_STATIONS, pathDqm)

    # Find directory for the last daily dqmreport
    lastDqmreport, schoolsDqmreportList = \
        read_dqmreport(EEE_ACTIVE_STATIONS, pathDqmreport)

    # Read the pickle file with RUN info from the database
    dqmData = read_pickle()
    dqmData.print_AllData()

    schoolNamesList = EEE_ACTIVE_STATIONS

    # Make the HTML main page index.html
    make_main_page(lastEntryPerSchool, runSchoolsSummary, schoolsDqmList,
                   lastDqmreport, schoolsDqmreportList, EEE_ACTIVE_STATIONS)

    # Final log message
    logger.info('Finished')
