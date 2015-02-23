# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 16:59:30 2014

@author: Fabrizio Coccetti
"""

from datetime import datetime
from e3monitor.html.__html_headers__ import PAGE_TITLE_HTML


def compute_update():
    """Compute last update time for the webpage
    and return string with time and title
    """
    updateTime = datetime.today().strftime("%H:%M - %a %d %B %Y")
    return (PAGE_TITLE_HTML +
            '<div class=\"time\">Ultimo aggiornamento: ore ' +
            updateTime +
            '</div>')
