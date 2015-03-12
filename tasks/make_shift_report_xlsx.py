# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:12:07 2015

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]

Make the Shift Report xlsx file
Code in use since the Database is in place
"""

import xlsxwriter
from datetime import datetime
import logging


def make_shift_report_xlsx(monitorData,
                           EEE_ACTIVE_STATIONS,
                           xlsxFile):
    '''Make the Shift Report xlsx file
    '''
    # Start logger
    logger = logging.getLogger('plain')
    logger.info('Function make_shift_report_xlsx() started')

    # Define NOW
    now = datetime.today()

    # Create a workbook and add a worksheet
    workbook = xlsxwriter.Workbook(xlsxFile)
    worksheet = workbook.add_worksheet('EEE')
    # Set A4 Paper
    worksheet.set_paper(9)

    # Set Headers of the worksheet
    worksheet.set_header('&CCentro Fermi')

    headers = ('Scuola',
               'NOTE dello SHIFTER',
               'Data ultimo File\ntrasferito al CNAF',
               'Nome ultimo File\n trasferito al CNAF',
               'Numero Files trasferiti oggi',
               'Ultima Entry e-logbook',
               'Nome ultimo File\n analizzato dal DQM',
               'RATE of Triggers',
               'RATE of Tracks')

    # Define formats
    fHeaders = workbook.add_format({'bold': True,
                                    'bg_color': '#F0F0F0',
                                    'text_wrap': 1,
                                    'valign': 'vcenter',
                                    'align': 'center',
                                    'border': True})
    fNotes = workbook.add_format({'text_wrap': 1,
                                  'valign': 'vcenter',
                                  'border': True})
    fVcenterBold = workbook.add_format({'bold': True,
                                        'valign': 'vcenter',
                                        'align': 'center',
                                        'border': True})
    fVcenter = workbook.add_format({'valign': 'vcenter',
                                    'align': 'center',
                                    'border': True})
    fNumInt = workbook.add_format({'valign': 'vcenter',
                                   'align': 'center',
                                   'border': True,
                                   'num_format': '0'})
    fNumDec = workbook.add_format({'valign': 'vcenter',
                                   'align': 'center',
                                   'border': True,
                                   'num_format': '0.#'})
    fBigFonts = workbook.add_format({'bold': True,
                                     'font_color': '#0088CC',
                                     'font_size': '14'})
    fTimeStamp = workbook.add_format({'text_wrap': 1,
                                      'valign': 'vcenter',
                                      'align': 'center',
                                      'border': True,
                                      'num_format': 'hh:mm dd/mm/yyyy'})

    # Write initial data
    worksheet.set_row(0, 30)
    worksheet.set_row(1, 30)
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
        worksheet.write(row, col, _header, fHeaders)
        col += 1

    # Format headers row
    worksheet.set_row(row, 60)
    # Format column size
    worksheet.set_column('A:A', 10)
    worksheet.set_column('B:B', 30)
    worksheet.set_column('C:C', 25)
    worksheet.set_column('D:D', 25)
    worksheet.set_column('E:E', 10)
    worksheet.set_column('F:F', 25)
    worksheet.set_column('G:G', 25)
    worksheet.set_column('H:I', 15)

    row = 3

    # Start loop for school names (sorted)
    for schoolName in sorted(monitorData.get_allData()):

        # Skip schools with no data
        if schoolName not in EEE_ACTIVE_STATIONS:
            continue

        # Start at the first Column for every row
        col = 0

        # Format Row Height
        worksheet.set_row(row, 60)

        # Print School Name
        worksheet.write(row, col, schoolName, fVcenterBold)
        col += 1

        # Print NOTE delle Shifter
        worksheet.write(row, col, 'Inserisci_le_tue_note', fNotes)
        col += 1

        # Print Day of the last transferred file at CNAF
        try:
            worksheet.write_datetime(
                row,
                col,
                monitorData.get_transferTs(schoolName),
                fTimeStamp)
        except:
            logger.info('Error for get_transferTs(' + schoolName + ')')
        col += 1

        # Print "Nome dell'ultimo File trasferito"
        worksheet.write(
            row,
            col,
            monitorData.get_transferFileName(schoolName),
            fVcenter
            )
        col += 1

        # Print "Numero di file trasferiti oggi"
        worksheet.write_number(
            row,
            col,
            int(monitorData.get_transferFileNum(schoolName)),
            fNumInt
            )
        col += 1

        # Print "Ultima Entry nell'e-logbook delle Scuole"
        try:
            worksheet.write(
                row,
                col,
                monitorData.get_elogEntryTs(schoolName),
                fVcenter
                )
        except:
            logger.info('Error for get_elogEntryTs(' + schoolName + ')')
            col += 1

        # Print "Nome dell'ultimo File analizzato dal DQM"
        try:
            worksheet.write(
                row,
                col,
                monitorData.get_DqmFileName(schoolName),
                fVcenter
                )
        except:
            logger.info('Error for get_DqmFileName(' + schoolName + ')')
        col += 1

        # Print triggers
        try:
            worksheet.write_number(
                row,
                col,
                float(monitorData.get_triggerRate(schoolName)),
                fNumDec
                )
        except:
            logger.info('Error for get_DqmFileName(' + schoolName + ')')
        col += 1

        # Print tracks (chi^2 < 10)
        try:
            worksheet.write_number(
                row,
                col,
                float(monitorData.get_trackRate(schoolName)),
                fNumDec
                )
        except:
            logger.info('Error for get_DqmFileName(' + schoolName + ')')
        col += 1

        # End of loop for schoolName. Now move to the next line
        row += 1

    workbook.close()
    logger.info('Function make_shift_report_xlsx() finished')
    return True
