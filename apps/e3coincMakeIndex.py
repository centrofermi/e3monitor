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
Created on Tue Sep 05 17:51:59 2017

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]

This app writes the DQM coincidences main web page
"""
import logging
import logging.config
import os
from datetime import datetime
from e3monitor.tasks.update_time import (time_update)
from e3monitor.config.__files_server__ import (
    logConfigFile,
    coincidencesDqmDir,
    coincidencesDqmFile)
from e3monitor.html.__html_headers__ import (
    DQM_HEADER_HTML,
    DQM_TITLE_HTML,
    DQM_BOTTOM_HTML)

# Set logging options
logging.config.fileConfig(logConfigFile)
logger = logging.getLogger('full')
logger.info('Started')

logger.info('Opening file for writing: ' + coincidencesDqmFile)
with open(coincidencesDqmFile, 'wt') as outFile:
    outFile.write(DQM_HEADER_HTML)
    outFile.write(DQM_TITLE_HTML)
    outFile.write('<div class=\"time\">Last update: ' + time_update() + '</div>')
    outFile.write('\n<table>\n')
    outFile.write('<tr><th>Pair of EEE Telescopes</th>\n')
    outFile.write('<th>Last file in DQM</th>\n')
    outFile.write('<th>Coincidencies:<br />Rate and Error</th></tr>\n')
    logger.info('Opening file for reading: ' + os.path.join(coincidencesDqmDir, 'summary.txt'))
    with open(os.path.join(coincidencesDqmDir, 'summary.txt'), 'rt') as inFile:
        for line in inFile:
            name, fileName, fileColor, rate, rateError, rateMin, rateColor = line.split()
            if fileColor == '0': fileColor = 'green'
            if fileColor == '1': fileColor = 'yellow'
            if fileColor == '2': fileColor = 'red'
            if rateColor == '0': rateColor = 'green'
            if rateColor == '1': rateColor = 'yellow'
            if rateColor == '2': rateColor = 'red'
            outFile.write('<tr>\n')
            outFile.write('<td class=\"gray\"><a href=\"dqmcoincidences/' + name +  '.html\">' + name + '</a></td>\n')
            outFile.write('<td class=\"' + fileColor + '\">' + fileName + '</td>\n')
            outFile.write('<td class=\"' + rateColor + '\">' + rate + ' +/- ' + rateError + '</td>\n')
            outFile.write('</tr>\n')
    outFile.write('</table>\n')
    outFile.write(DQM_BOTTOM_HTML)

# Final log message
logger.info('Finished')
