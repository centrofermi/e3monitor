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
# Creation: 24 feb 2016
#
# Read the number of files transferred per school per day
# and makes plots
#

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import logging
import logging.config
from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter
#import matplotlib.ticker as mtick
from matplotlib import ticker
from datetime import datetime
from e3monitor.tasks.read_pickle import read_pickle
from e3monitor.config.__files_server__ import (pathSaveFig,
                                               pklStatFile,
                                               pathWorkDir,
                                               logConfigFile)

# Define dictionary for track statistics
trackStat = {}
dates = []
ntracks = []

# Set logging
logging.config.fileConfig(logConfigFile)
logger = logging.getLogger('full')
logger.info('Started: Make plot for Statistics')

# Read pickle
trackStat = read_pickle(pathWorkDir, pklStatFile)
logger.info("pickle file extracted from the"
            "database imported: track data is loaded")

#
# Make the plot
#
logger.info("Let's make the plot...")
# First make two list with ordered values
for _dates, _ntracks in sorted(trackStat.items()):
    dates.append(datetime.strptime(_dates, '%Y-%m-%d'))
    ntracks.append(_ntracks)

# Set xlabel every interval months
months = MonthLocator(range(1, 13), bymonthday=1, interval=1)
monthsFmt = DateFormatter("%d %b %Y")
# Set ylabel
sci = ticker.MultipleLocator(base=2000000000.0)
sciFmt = ticker.ScalarFormatter()
sciFmt.set_scientific(True)

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)
ax.autoscale_view()
ax.grid(True)
ax.set_title("Total number of candidate tracks vs months of data acquisition")
ax.set_xlabel("Months of data acquisition")
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthsFmt)
ax.set_ylabel("Number of tracks")
ax.yaxis.set_major_locator(sci)
ax.yaxis.set_major_formatter(sciFmt)
ax.fill_between(dates, 0, ntracks, facecolor='#87CEFA')
#ax.fill_between(dates, 0, ntracks, facecolor='#99FF99')

ax.plot_date(dates, ntracks, color='#0088CC', linestyle='dotted', marker='o')
fig.autofmt_xdate()
fig.savefig(pathSaveFig + 'tracks.png')
logger.info("Plot saved in " + str(pathSaveFig) + 'tracksStat.png')

#
# Make the webpage
#
logger.info("Let's make the Stats webpage...")


# End
logger.info('Finished')

