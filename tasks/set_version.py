# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 11:40:55 2014

@author: Fabrizio Coccetti
Return string with e3monitor version and time/date
"""
from datetime import datetime
from e3monitor.__version__ import TAG


def set_version():
    """ Return string with e3monitor version and time/date
    """
    return('version ' + TAG + '<br />' +
           'Generated on ' + datetime.today().strftime("%d/%m/%Y") +
           ' at ' + datetime.today().strftime("%H:%M"))
