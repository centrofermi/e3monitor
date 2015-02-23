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
               'Giorno ultimo file trasferito',
               'Ora',
               'Nome ultimo File trasferito al CNAF',
               'Numero Files trasferiti oggi',
               'Ultima Entry e-logbook',
               'Nome ultimo File analizzato dal DQM',
               'RATE of Triggers',
               'RATE of Tracks')

    # Define formats
    fHeaders = workbook.add_format({'bold': True,
                                    'text_wrap': 1,
                                    'valign': 'vcenter',
                                    'align': 'center'})
    fNotes = workbook.add_format({'text_wrap': 1,
                                  'valign': 'top'})
    fVcenter = workbook.add_format({'valign': 'vcenter'})
    fBigFonts = workbook.add_format({'bold': True,
                                     'font_size': '14'})
    fTimeStamp = workbook.add_format({'text_wrap': 1,
                                      'num_format': 'ddd dd mmmm'})

    # Write initial data
    worksheet.write(0,
                    0,
                    "Shifter Report: " + now.strftime("%a %d %B %Y"),
                    fBigFonts)
    worksheet.write(1,
                    0,
                    "Situazione alle ore: " + now.strftime("%H:%M"),
                    fBigFonts)

    row = 2
    col = 0

    # Write headers
    # worksheet.write_row(row, col, headers)
    for _header in headers:
        worksheet.write(row, col, _header)
        col += 1

    # Format headers row
    worksheet.set_row(row, 60, fHeaders)
    # Format column size
    worksheet.set_column('A:A', 10)
    worksheet.set_column('B:B', 30)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('C:D', 10)
    worksheet.set_column('E:E', 30)
    worksheet.set_column('F:F', 20)
    worksheet.set_column('G:G', 25)
    worksheet.set_column('H:H', 30)
    worksheet.set_column('I:J', 15)

    row = 3

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
        worksheet.set_row(row, 60)

        # Print School Name
        worksheet.write(row, col, schoolName, fVcenter)
        col += 1

        # Print NOTE delle Shifter
        worksheet.write(row, col, 'Inserisci_le_tue_note', fNotes)
        col += 1

        # Print Day of the last transferred file at CNAF
        worksheet.write_datetime(row,
                                 col,
                                 timeData,
                                 fTimeStamp)
        col += 1

        # Print Time of the last transferred file at CNAF
        worksheet.write(row, col, hourData, fVcenter)
        col += 1

        # Print "Nome dell'ultimo File trasferito"
        worksheet.write(row, col, fileNameData, fVcenter)
        col += 1

        # Print "Numero di file trasferiti oggi"
        worksheet.write_number(row, col, transferedFileNumber, fVcenter)
        col += 1

        # Print "Ultima Entry nell'e-logbook delle Scuole"
        try:
            worksheet.write(row, col,
                            lastEntryPerSchool[schoolName].strftime(
                                "%H:%M %d/%m/%Y"), fVcenter)
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
            worksheet.write(row, col, _runNameInDqm, fVcenter)
        except:
            worksheet.write(row, col, '')
        col += 1

        # Print triggers
        try:
            worksheet.write_number(row,
                                   col,
                                   str(round(dqmData.trigger_rate(schoolName),
                                             1)),
                                   fVcenter)
        except:
            worksheet.write(row, col, '')
        col += 1

        # Print tracks (chi^2 < 10)
        try:
            worksheet.write_number(row,
                                   col,
                                   str(round(dqmData.track_rate(schoolName),
                                             1)),
                                   fVcenter)
        except:
            worksheet.write(row, col, '')
        col += 1

        row += 1

    workbook.close()
    logger.info('Function make_xlsx_file() finished')
    return True
