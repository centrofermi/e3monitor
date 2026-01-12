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
# Make the main plot of tracks vs date
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
import csv
import matplotlib.dates as md
import matplotlib.patches as patches
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

# Define dates of Runs
# Pilot Run 2014
# martedi 21 ottobre ore 12:00 inizio presa dati in modalita commissioning
# lunedi 27 ottobre ore 12:00      inizio presa dati
# venerdi 14 novembre ore 12:00   termine presa dati
# Run 1 2015
# 23-27 febbraio: Commissioning
#27 febbraio - 30 aprile: Presa dati ufficiale
dateRun0Start = md.date2num(datetime(2014,10,27))
dateRun0End = md.date2num(datetime(2014,11,14))
dateRun1Start = md.date2num(datetime(2015,2,27))
dateRun1End = md.date2num(datetime(2015,4,30))
dateRun2Start = md.date2num(datetime(2015,11,7))
dateRun2End = md.date2num(datetime(2016,5,20))
dateRun3Start = md.date2num(datetime(2016,11,1))
dateRun3End = md.date2num(datetime(2017,5,31))
dateRun4Start = md.date2num(datetime(2017,10,2))
dateRun4End = md.date2num(datetime(2018,5,30))
dateRun5Start = md.date2num(datetime(2018,10,15))
dateRun5End = md.date2num(datetime(2019,5,31))
dateRun6Start = md.date2num(datetime(2022,10,1))
dateRun6End = md.date2num(datetime(2023,7,31))
dateRun7Start = md.date2num(datetime(2023,11,1))
dateRun7End = md.date2num(datetime(2025,3,31))
dateEcoPilotRunStart = md.date2num(datetime(2025,4,2))
dateEcoPilotRunEnd = md.date2num(datetime(2025,11,13))
dateRun8Start = md.date2num(datetime(2025,11,14))
dateRunToday = md.date2num(datetime.today())
dateRun8End = dateRunToday

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
months = MonthLocator(range(1, 13), bymonthday=1, interval=4)
monthsFmt = DateFormatter("%d %b %Y")
# Set ylabel
sci = ticker.MultipleLocator(base=5000000000.0)
sciFmt = ticker.ScalarFormatter()
sciFmt.set_scientific(True)

fig = plt.figure(figsize=(16, 6))
ax = fig.add_subplot(111)
ax.autoscale_view()
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_title("Total number of candidate tracks vs months of data acquisition")
ax.set_xlabel("Months of data acquisition")
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthsFmt)
ax.set_ylabel("Number of tracks")
ax.yaxis.set_major_locator(sci)
ax.yaxis.set_major_formatter(sciFmt)
ax.set_ylim(0.0, 1.5e11)

# Print graph
ax.plot_date(dates, ntracks, color='#0088CC', linestyle='dotted', marker='o')
ax.fill_between(dates, 0, ntracks, facecolor='#87CEFA',zorder=1)

# ############
# Color Runs
# ###########
yMin, yMax = ax.get_ylim()
hText = 7e9

# Pilot Run
#ax.add_patch(patches.Rectangle((dateRun0Start, yMin), dateRun0End-dateRun0Start, yMax, fill=1, facecolor="#c0392b", alpha=.3))
ax.annotate('PILOT RUN', xy=(dateRun0Start-80+(dateRun0End-dateRun0Start)/2,hText+10e10),size=12,rotation='vertical',weight='bold',color='#c0392b',zorder=10)
ax.add_patch(patches.Rectangle((dateRun0Start, yMin), dateRun0End-dateRun0Start, yMax, fill=0, facecolor="#c0392b", edgecolor="#c0392b", linestyle='dashed', linewidth=2))
ax.add_patch(patches.Rectangle((dateRun0Start, yMin), dateRun0End-dateRun0Start, yMax, fill=1, facecolor="#c0392b", alpha=0.1))

# Run 1
ax.add_patch(patches.Rectangle((dateRun1Start, yMin), dateRun1End-dateRun1Start, yMax, fill=0, facecolor="#c0392b", edgecolor="#c0392b", linestyle='dashed', linewidth=2))
ax.add_patch(patches.Rectangle((dateRun1Start, yMin), dateRun1End-dateRun1Start, yMax, fill=1, facecolor="#c0392b", alpha=0.1))
#ax.annotate('', xy=(dateRun1End,hText), xytext=(dateRun1Start, hText), arrowprops=dict(arrowstyle='<->',connectionstyle="arc3,rad=0.0",edgecolor='#c0392b',linewidth=2.5))
ax.annotate('RUN 1', xy=(dateRun1Start-18+(dateRun1End-dateRun1Start)/2,hText+10e10),size=12,rotation='vertical',weight='bold',color='#c0392b')

# Run 2
ax.add_patch(patches.Rectangle((dateRun2Start, yMin), dateRun2End-dateRun2Start, yMax, fill=0, facecolor="#c0392b", edgecolor="#c0392b", linestyle='dashed', linewidth=2))
ax.add_patch(patches.Rectangle((dateRun2Start, yMin), dateRun2End-dateRun2Start, yMax, fill=1, facecolor="#c0392b", alpha=0.1))
#ax.annotate('', xy=(dateRun2End,hText), xytext=(dateRun2Start, hText), arrowprops=dict(arrowstyle='<->',connectionstyle="arc3,rad=0.0",edgecolor='#c0392b',linewidth=2.5))
ax.annotate('RUN 2', xy=(dateRun2Start-18+(dateRun2End-dateRun2Start)/2,hText+10e10),size=12,rotation='vertical',weight='bold',color='#c0392b')

# Run 3
ax.add_patch(patches.Rectangle((dateRun3Start, yMin), dateRun3End-dateRun3Start, yMax, fill=0, facecolor="#c0392b", edgecolor="#c0392b", linestyle='dashed', linewidth=2))
ax.add_patch(patches.Rectangle((dateRun3Start, yMin), dateRun3End-dateRun3Start, yMax, fill=1, facecolor="#c0392b", alpha=0.1))
#ax.annotate('', xy=(dateRun3End,hText), xytext=(dateRun3Start, hText), arrowprops=dict(arrowstyle='<->',connectionstyle="arc3,rad=0.0",edgecolor='#c0392b',linewidth=2.5))
ax.annotate('RUN 3', xy=(dateRun3Start-18+(dateRun3End-dateRun3Start)/2,hText+10e10),size=12,rotation='vertical',weight='bold',color='#c0392b')

# Run 4
ax.add_patch(patches.Rectangle((dateRun4Start, yMin), dateRun4End-dateRun4Start, yMax, fill=0, facecolor="#c0392b", edgecolor="#c0392b", linestyle='dashed', linewidth=2))
ax.add_patch(patches.Rectangle((dateRun4Start, yMin), dateRun4End-dateRun4Start, yMax, fill=1, facecolor="#c0392b", alpha=0.1))
ax.annotate('RUN 4', xy=(dateRun4Start-18+(dateRun4End-dateRun4Start)/2,hText+10e10),size=12,rotation='vertical',weight='bold',color='#c0392b')

# Run 5
ax.add_patch(patches.Rectangle((dateRun5Start, yMin), dateRun5End-dateRun5Start, yMax, fill=0, facecolor="#c0392b", edgecolor="#c0392b", linestyle='dashed', linewidth=2))
ax.add_patch(patches.Rectangle((dateRun5Start, yMin), dateRun5End-dateRun5Start, yMax, fill=1, facecolor="#c0392b", alpha=0.1))
ax.annotate('RUN 5', xy=(dateRun5Start-18+(dateRun5End-dateRun5Start)/2,hText+10e10),size=12,rotation='vertical',weight='bold',color='#c0392b')

# Run 6
ax.add_patch(patches.Rectangle((dateRun6Start, yMin), dateRun6End-dateRun6Start, yMax, fill=0, facecolor="#c0392b", edgecolor="#c0392b", linestyle='dashed', linewidth=2))
ax.add_patch(patches.Rectangle((dateRun6Start, yMin), dateRun6End-dateRun6Start, yMax, fill=1, facecolor="#c0392b", alpha=0.1))
ax.annotate('RUN 6', xy=(dateRun6Start-18+(dateRun6End-dateRun6Start)/2, hText+10e10), size=12, rotation='vertical', weight='bold', color='#c0392b')

# Run 7
ax.add_patch(patches.Rectangle((dateRun7Start, yMin), dateRun7End-dateRun7Start, yMax, fill=0, facecolor="#c0392b", edgecolor="#c0392b", linestyle='dashed', linewidth=2))
ax.add_patch(patches.Rectangle((dateRun7Start, yMin), dateRun7End-dateRun7Start, yMax, fill=1, facecolor="#c0392b", alpha=0.1))
ax.annotate('RUN 7', xy=(dateRun7Start-18+(dateRun7End-dateRun7Start)/2, hText+10e10), size=12, rotation='vertical', weight='bold', color='#c0392b')

# Eco Pilot Run
ax.add_patch(patches.Rectangle((dateEcoPilotRunStart, yMin), dateEcoPilotRunEnd-dateEcoPilotRunStart, yMax, fill=0, facecolor="#c0392b", edgecolor="#c0392b", linestyle='dashed', linewidth=2))
ax.add_patch(patches.Rectangle((dateEcoPilotRunStart, yMin), dateEcoPilotRunEnd-dateEcoPilotRunStart, yMax, fill=1, facecolor="#c0392b", alpha=0.1))
ax.annotate('Eco Pilot Run', xy=(dateEcoPilotRunStart-18+(dateEcoPilotRunEnd-dateEcoPilotRunStart)/2, hText+10e10), size=12, rotation='vertical', weight='bold', color='#c0392b')

# Run 8
ax.add_patch(patches.Rectangle((dateRun8Start, yMin), dateRun8End-dateRun8Start, yMax, fill=0, facecolor="#c0392b", edgecolor="#c0392b", linestyle='dashed', linewidth=2))
ax.add_patch(patches.Rectangle((dateRun8Start, yMin), dateRun8End-dateRun8Start, yMax, fill=1, facecolor="#c0392b", alpha=0.1))
ax.annotate('RUN 8 (active)', xy=(dateRun8Start-18+(dateRun8End-dateRun8Start)/2, hText+10e10), size=10, rotation='vertical', weight='bold', color='#c0392b')

# FOLLOWING THREE LINES for RUN 9
#ax.add_patch(patches.Rectangle((dateRun5Start, yMin), dateRunToday-dateRun5Start, yMax, fill=0, facecolor="#c0392b", edgecolor="#c0392b", linestyle='dashed',linewidth=2))
#ax.annotate('', xy=(dateRunToday-2,hText), xytext=(dateRun5Start, hText), arrowprops=dict(arrowstyle='<->',connectionstyle="arc3,rad=0.0",edgecolor='#c0392b',linewidth=2.5))
#ax.annotate('RUN 5', xy=(dateRun5Start-40+(dateRunToday-dateRun5Start)/2,hText+1e9),size=18,weight='bold',color='#c0392b', backgroundcolor='#87CEFA')

# Save plot
fig.autofmt_xdate()
fig.savefig(pathSaveFig + 'tracks.png')
logger.info("Plot saved in " + str(pathSaveFig) + 'tracks.png')
# Save data to CSV
csv_file_path = pathSaveFig + 'tracks.csv'
with open(csv_file_path, mode='wb') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Number of Tracks'])
    for date, ntrack in zip(dates, ntracks):
        writer.writerow([date.strftime('%Y-%m-%d'), ntrack])

logger.info("Data saved in " + csv_file_path)
#
# Make the webpage
#
logger.info("Let's make the Stats webpage...")


# End
logger.info('Finished')

