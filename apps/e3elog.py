#!/usr/bin/env python
# *********************************************************************
# * Copyright (C) 2014 Fabrizio Coccetti                              *
# * fabrizio.coccetti@centrofermi.it                                  *
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
# Creation: 7 Oct 2014
#
# Read the Midas Elog files .log and conver them in csv
#
import os
import csv
from datetime import datetime
from e3monitor.config.__elog_tablehead__ import ELOG_HEADER
from e3monitor.config.__files_server__ import elogCsvFile, elogBookPath

# File to export data
f = open(elogCsvFile, 'w')
f_csv = csv.writer(f)
rowData = ['']*28
f_csv.writerow(ELOG_HEADER)
files = os.listdir(elogBookPath)
# Search for all files and directories
for fileName in files:
    if fileName.endswith('.log'):
        importFile = open(os.path.join(elogBookPath, fileName), 'r')
        importFileLines = importFile.readlines()
        for importLine in importFileLines:
            importLine = importLine.rstrip()
            words = importLine.split(':', 1)
            if len(words) == 2:
                if words[0] == '$@MID@$':
                    rowData[0] = words[1].strip()
                elif words[0] == 'Date':
                    words[1] = words[1][:-6]
                    date_object = datetime.strptime(words[1],
                                                    ' %a, %d %b %Y %H:%M:%S')
                    rowData[1] = date_object.strftime("%d/%m/%Y")
                    rowData[2] = date_object.strftime("%H:%M:%S")
                elif words[0] == 'Scuola':
                    rowData[3] = words[1].strip()
                elif words[0] == 'Operatore':
                    rowData[4] = words[1].strip().decode('utf-8', 'ignore')
                elif words[0] == 'MRPC1 HV_POS (V)':
                    rowData[5] = words[1].strip().replace(",", ".")
                elif words[0] == 'MRPC1 HV_NEG (V)':
                    rowData[6] = words[1].strip().replace(",", ".")
                elif words[0] == 'MRPC1 I_POS (microA)':
                    rowData[7] = words[1].strip().replace(",", ".")
                elif words[0] == 'MRPC1 I_NEG (microA)':
                    rowData[8] = words[1].strip().replace(",", ".")
                elif words[0] == 'MRPC1 LV (V)':
                    rowData[9] = words[1].strip().replace(",", ".")
                elif words[0] == 'MRPC2 HV_POS (V)':
                    rowData[10] = words[1].strip().replace(",", ".")
                elif words[0] == 'MRPC2 HV_NEG (V)':
                    rowData[11] = words[1].strip().replace(",", ".")
                elif words[0] == 'MRPC2 I_POS (microA)':
                    rowData[12] = words[1].strip().replace(",", ".")
                elif words[0] == 'MRPC2 I_NEG (microA)':
                    rowData[13] = words[1].strip().replace(",", ".")
                elif words[0] == 'MRPC2 LV (V)':
                    rowData[14] = words[1].strip().replace(",", ".")
                elif words[0] == 'MRPC3 HV_POS (V)':
                    rowData[15] = words[1].strip().replace(",", ".")
                elif words[0] == 'MRPC3 HV_NEG (V)':
                    rowData[16] = words[1].strip().replace(",", ".")
                elif words[0] == 'MRPC3 I_POS (microA)':
                    rowData[17] = words[1].strip().replace(",", ".")
                elif words[0] == 'MRPC3 I_NEG (microA)':
                    rowData[18] = words[1].strip().replace(",", ".")
                elif words[0] == 'MRPC3 LV (V)':
                    rowData[19] = words[1].strip().replace(",", ".")
                elif words[0] == 'Front-End LV (V)':
                    rowData[20] = words[1].strip().replace(",", ".")
                elif words[0] == 'SF6 (press)':
                    rowData[21] = words[1].strip().replace(",", ".")
                elif words[0] == 'C2H2F4 (press)':
                    rowData[22] = words[1].strip().replace(",", ".")
                elif words[0] == 'SF6 (flusso)':
                    rowData[23] = words[1].strip().replace(",", ".")
                elif words[0] == 'C2H2F4 (flusso)':
                    rowData[24] = words[1].strip().replace(",", ".")
                elif words[0] == 'Temp (C)':
                    rowData[25] = words[1].strip().replace(",", ".")
                elif words[0] == 'Press (mbar)':
                    rowData[26] = words[1].strip().replace(",", ".")
                elif words[0] == 'Rate (Hz)':
                    rowData[27] = words[1].strip().replace(",", ".")
                    f_csv.writerow(rowData)
                    rowData = ['']*28
        importFile.close()
f.close()
print("Success")
