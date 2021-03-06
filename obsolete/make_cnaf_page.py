# -*- coding: utf-8 -*-
# DISMISSED
"""
Created on Tue Nov 18 23:18:29 2014

@author: Fabrizio Coccetti
This software is not in use anymore (since Feb 2015)
Replaced when switching from Virtual Machine to BTSync
"""
from datetime import datetime
import logging
from e3monitor.html.__html_headers__ import (HEADER_HTML,
                                            TABELLA2_HTML,
                                            FOOTER_HTML,
                                            BOTTOM_HTML)
from e3monitor.tasks.update_time import compute_update
from e3monitor.tasks.set_version import set_version
from e3monitor.config.__files_server__ import lastTestFile, cnafWebPageFile


def make_cnaf_page():
    '''Make the index.html webpage with the Netstatus main table
    '''

    logger = logging.getLogger('plain')
    logger.info('Function make_cnaf_page() started')

    f = open(lastTestFile, 'r')
    w = open(cnafWebPageFile, 'w')
    now = datetime.today()
    w.write(HEADER_HTML)
    w.write(compute_update())
    w.write(TABELLA2_HTML)
    lines = f.readlines()
    for line in lines:
        schoolName, timeTempTest, hourTest, versioneTrasf = line.split(' ')
        timeTempTest = hourTest + timeTempTest
        timeTest = datetime.strptime(timeTempTest, '%H%Y-%m-%d')
        timeDiff = now - timeTest
        if timeDiff.days == 0:
            if timeDiff.seconds < 7300:
                classColor = 'green'
            elif timeDiff.seconds < 10900:
                classColor = 'yellow'
            else:
                classColor = 'red'
        else:
            classColor = 'red'
        w.write('<tr class=\"')
        w.write(classColor)
        w.write('\"><td>')
        w.write(schoolName)
        w.write('</td><td>')
        w.write(timeTest.strftime("%a %d %B %Y"))
        w.write('</td><td>')
        w.write(timeTest.strftime("%H:%M"))
        w.write('</td><td>')
        w.write(versioneTrasf.replace('v', 'Versione '))
        w.write('</td></tr>')
    w.write('</table>')
    w.write(FOOTER_HTML)
    w.write(set_version())
    w.write(BOTTOM_HTML)
    w.write(BOTTOM_HTML)
    f.close()
    w.close()
    logger.info('Function make_main_page() finished')
    return True
