# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 17:19:41 2015

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
"""

import xlsxwriter
from datetime import datetime
import logging
from e3monitor.config.__files_server__ import (lastDataFile,
                                               xlsFile)


def make_xlsx_file(lastEntryPerSchool, lastDqmreport, schoolsDqmreportList,
                   dqmData, schoolNamesList):
    '''Make the xlsx file with the Online main monitoring table
    '''

    logger = logging.getLogger('plain')
    logger.info('Function make_xlsx_file() started')

    # Define NOW
    now = datetime.today()

    # Create a workbook and add a worksheet
    workbook = xlsxwriter.Workbook(xlsFile)
    worksheet = workbook.add_worksheet('EEE')
    # Set A4 Paper
    worksheet.set_paper(9)

    # Set Headers of the worksheet
    worksheet.set_header('&CCentro Fermi')

    headers = ('Scuola',
               'NOTE dello SHIFTER',
               'Giorno',
               'Ora',
               'Nome ultimo File trasferito al CNAF',
               'Numero Files trasferiti oggi',
               'Ultima Entry e-logbook',
               'Nome ultimo File analizzato dal DQM',
               'RATE of Triggers',
               'RATE of Tracks')
    row = 0
    col = 0

    # Write headers
    # worksheet.write_row(row, col, headers)
    for _header in headers:
        worksheet.write(row, col, _header)
        col += 1

    # Define formats
    text_bold = workbook.add_format({'bold': True, 'valign': 'vcenter'})
    # wrap_format = workbook.add_format()
    # wrap_format.set_text_wrap()
    text_wrap = workbook.add_format({'text_wrap': 1, 'valign': 'top'})
    # Format headers row
    worksheet.set_row(row, 50, text_bold)
    # Format column size
    worksheet.set_column('A:A', 10)
    worksheet.set_column('B:B', 30)
    worksheet.set_column('C:D', 10)
    worksheet.set_column('E:H', 30)
    worksheet.set_column('I:J', 15)

    row = 1

    # Read file from CNAF
    f = open(lastDataFile, 'r')
    lines = f.readlines()
    for line in lines:
        (schoolName, timeTempData, hourData,
         fileNameData, transferedFileNumber) = line.split()
        timeTempData = timeTempData+hourData
        try:
            timeData = datetime.strptime(timeTempData, '%Y-%m-%d%H:%M')
        except:
            timeData = now

        # Start at the first Column for every row
        col = 0

        # Format Row Height
        worksheet.set_row(row, 50)

        # Print School Name
        worksheet.write(row, col, schoolName)
        col += 1

        # Print NOTE delle Shifter
        worksheet.write(row, col, 'Inserisci le tue note', text_wrap)
        col += 1

        # Print Day of the last transferred file at CNAF
        worksheet.write(row, col, timeData.strftime("%a %d %B"))
        col += 1

        # Print Time of the last transferred file at CNAF
        worksheet.write(row, col, hourData)
        col += 1

        # Print "Nome dell'ultimo File trasferito"
        worksheet.write(row, col, fileNameData)
        col += 1

        # Print "Numero di file trasferiti oggi"
        worksheet.write(row, col, transferedFileNumber)
        col += 1

        # Print "Ultima Entry nell'e-logbook delle Scuole"
        try:
            worksheet.write(row, col,
                            lastEntryPerSchool[schoolName].strftime(
                                "%H:%M %d/%m/%Y"))
        except:
            worksheet.write(row, col, '')
        col += 1

        # Print "Nome dell'ultimo File analizzato dal DQM"
        try:
            _runNameInDqm = (schoolName +
                             dqmData.run_date(
                                 schoolName).strftime("-%Y-%m-%d-") +
                             "{0:0>5}".format(int(
                                 dqmData.run_id(schoolName))))
            worksheet.write(row, col, _runNameInDqm)
        except:
            worksheet.write(row, col, '')
        col += 1

        # Print triggers
        try:
            worksheet.write(row, col,
                            str(round(dqmData.trigger_rate(schoolName), 1)))
        except:
            worksheet.write(row, col, '')
        col += 1

        # Print tracks (chi^2 < 10)
        try:
            worksheet.write(row, col,
                            str(round(dqmData.track_rate(schoolName))))
        except:
            worksheet.write(row, col, '')
        col += 1

        row += 1

    workbook.close()
    logger.info('Function make_xlsx_file() finished')
    return True
