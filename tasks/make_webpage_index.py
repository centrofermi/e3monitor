# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 12:17:38 2015

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]

Make the index.html webpage with the main Monitor table
"""

import logging
from e3monitor.tasks.update_time import compute_update
from e3monitor.tasks.set_version import set_version
from e3monitor.html.__html_headers__ import (HEADER_HTML,
                                             TABELLA1_HTML,
                                             FOOTER_HTML,
                                             BOTTOM_HTML)


def make_webpage_index(monitorData, mainWebPageFileBeta):
    '''Make the index.html webpage with the main Monitor table
    '''

    logger = logging.getLogger('plain')
    logger.info('Function make_main_page() started')

    # Open index.html
    w = open(mainWebPageFileBeta, 'w')

    # Write html headers and titles of the table
    w.write(HEADER_HTML)
    w.write(compute_update())
    w.write(TABELLA1_HTML)

    # Start loop for school names (sorted)
    _monitorData = sorted(monitorData.items(), key=lambda t: t[1])
    for schoolName in _monitorData:

        # Set <tr> class color
        w.write('</tr>')

        # Print School Name in format: TEST-01
        w.write('<span style=\"font-weight: bold;\">')
        w.write(schoolName)
        w.write('</span>')
        w.write('</td>')

        # End loop for school names
        w.write('</tr>')

    w.write('</table>')
    w.write(FOOTER_HTML)
    w.write(set_version())
    w.write(BOTTOM_HTML)
    w.close()
    logger.info('Function make_webpage_index() finished')
    return True
