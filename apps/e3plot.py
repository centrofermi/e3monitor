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
# Creation: 17 oct 2014
#
# Read the number of files transferred per school per day
# and makes plots
#

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime
import logging
import logging.config
from e3monitor.config.__files_server__ import (lastTransferredFile,
                                               pathSaveFig,
                                               logConfigFile)
# Set logging
logging.config.fileConfig(logConfigFile)
logger = logging.getLogger('full')
logger.info('Started')

# Read input file from CNAF
f = open(lastTransferredFile, 'r')
i = 0
# define dictionary runInfo, with dates and n. of runs
runInfo = {}
lines = f.readlines()
for line in lines:
    line = line.rstrip()
    if line.startswith('day'):
        schoolName = line[-7:]
    elif line.startswith('20'):
        if not line.startswith('2015'):
            continue
        runDateTemp, runNumbers = line.split()
        runDate = datetime.strptime(runDateTemp[:10], '%Y-%m-%d')
        runInfo[runDate] = int(runNumbers)
    elif not line:
        if i == 0:
            i = 1
        elif i == 1:
            if not runInfo:
                continue
            x = []
            y = []
            s = sorted(runInfo.keys())
            for key in s:
                x.append(key.strftime("%a %d %b %y"))
                y.append(runInfo[key])
            xLocations = np.arange(len(x))
            fig = plt.figure()
            fig.suptitle('File transfer history from '+schoolName+' to CNAF')
            plt.xlabel('Days', fontsize=18)
            plt.ylabel('Number of transferred files')
            ax = fig.gca()
            ax.bar(xLocations, y, 1, color='#0088cc')
            ax.yaxis.grid('True')
            ax.set_xticks(xLocations+0.5)
            ax.set_xticklabels(x, rotation=40, ha='right')
            ax.set_xlim(0.0, xLocations.max()+1)
            fig.subplots_adjust(bottom=0.3)
            fig.savefig(pathSaveFig+schoolName)
            runInfo.clear()
            i = 0
f.close()
logger.info('Finished')

