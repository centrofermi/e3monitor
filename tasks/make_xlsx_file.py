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

    # Create a workbook and add a worksheet
    workbook = xlsxwriter.Workbook(xlsFile)
    worksheet = workbook.add_worksheet('EEE')

    headers = ('Scuola',
               'Giorno'
               'Ora'
               'Nome ultimo File trasferito')
    row = 0
    col = 0

    for _header in headers:
        worksheet.write(row, col, _header)
        col += 1

    workbook.close()
    logger.info('Function make_xlsx_file() finished')
    return True
