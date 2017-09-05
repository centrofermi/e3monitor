# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 16:59:30 2014

@author: Fabrizio Coccetti
"""

from datetime import datetime
from datetime import date
from e3monitor.html.__html_headers__ import (PAGE_TITLE_HTML,
                                             PAGE_SUBTILE_HTML)


def compute_update():
    """Computes last update time for the webpage
    and return string with time and title
    """
    updateTime = datetime.today().strftime("%H:%M - %A %d %B %Y")
    return (PAGE_TITLE_HTML +
            '<div class=\"time\">Ultimo aggiornamento: ore ' +
            updateTime +
            ' [by <a href=\"https://github.com/centrofermi/e3monitor\">'
            'e3monitor</a>]</div>')


def time_update():
    """Computes last update time for the webpage
    and return string with time
    """
    timeUpdate = datetime.today().strftime("%H:%M - %A %d %B %Y")
    return (timeUpdate)


def day_of_run():
    """Computes the day of the run
    """
    today = date.today()
    startRun = date(2016, 11, 1)
    daysOfRun = today - startRun
    return(PAGE_SUBTILE_HTML + str(daysOfRun.days+1) + '</i></h2>')


def day_run():
    """Computes the day of the Run, returns only that day
    """
    today = date.today()
    startRun = date(2016, 11, 1)
    daysOfRun = today - startRun
    return(str(daysOfRun.days+1))
