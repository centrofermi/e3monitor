# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 18:38:15 2014

@author: Fabrizio Coccetti
"""
from datetime import datetime
import logging
from e3monitor.html.__html_headers__ import (HEADER_HTML,
                                             TABELLA1_HTML,
                                             FOOTER_HTML,
                                             BOTTOM_HTML)
from e3monitor.tasks.update_time import compute_update
from e3monitor.tasks.set_version import set_version
from e3monitor.config.__files_server__ import (lastDataFile,
                                               mainWebPageFile)


def make_main_page(lastEntryPerSchool, runSchoolsSummary, schoolsDqmList,
                   lastDqmreport, schoolsDqmreportList, schoolNamesList):
    '''Make the index.html webpage with the Online main monitoring table
    '''

    logger = logging.getLogger('plain')
    logger.info('Function make_main_page() started')

    f = open(lastDataFile, 'r')
    w = open(mainWebPageFile, 'w')
    now = datetime.today()
    w.write(HEADER_HTML)
    w.write(compute_update())
    w.write(TABELLA1_HTML)
    classColor = 'green'
    lines = f.readlines()
    for line in lines:
        (schoolName, timeTempData, hourData,
         fileNameData, transferedFileNumber) = line.split()
        timeTempData = timeTempData+hourData
        try:
            timeData = datetime.strptime(timeTempData, '%Y-%m-%d%H:%M')
        except:
            timeData = now
        timeDiff = now - timeData
        if timeDiff.days == 0:
            if timeDiff.seconds < 14400:
                classColor = 'green'
            else:
                classColor = 'yellow'
        elif timeDiff.days == 1:
            classColor = 'yellow'
        else:
            classColor = 'red'
        w.write('<tr class=\"')
        w.write(classColor)
        w.write('\"><td>')
        w.write(schoolName)
        w.write('</td><td>')
        w.write(timeData.strftime("%a %d"))
        w.write('<br />')
        w.write(timeData.strftime("%B"))
        w.write('</td><td>')
        w.write(hourData)
        w.write('</td><td>')
        w.write(fileNameData[:13]+'<br />'+fileNameData[13:])
        w.write('</td><td class=\"right\">')
        w.write(transferedFileNumber)
        w.write('<br /><a href=\"plots/' + schoolName + '.png\">[History]</a>')
        w.write('</td><td>')
        try:
            w.write(lastEntryPerSchool[schoolName].strftime("%H:%M"))
            w.write('<br />')
            w.write(lastEntryPerSchool[schoolName].strftime("%d/%m/%Y"))
        except:
            w.write('&nbsp;')
        w.write('</td><td>')
        if schoolName not in schoolNamesList:
            w.write('')
        elif schoolName not in schoolsDqmreportList:
            w.write('')
        else:
            dateDqmReport = datetime.strptime(lastDqmreport[schoolName],
                                              '%Y-%m-%d')
            w.write('<a href=\"dqmreport/')
            w.write(schoolName+'/'+lastDqmreport[schoolName])
            w.write('/index.html\">')
            w.write(dateDqmReport.strftime("%d/%m"))
            w.write('</a><br /><a href =\"dqmreport/' + schoolName + '/\">')
            w.write('[History]')
            w.write('</a>')
        w.write('</td><td>')
        if schoolName not in schoolNamesList:
            w.write('')
        elif schoolName not in schoolsDqmList:
            w.write('')
        elif not runSchoolsSummary[schoolName][0]:
            w.write('')
        else:
            w.write(str(round(runSchoolsSummary[schoolName][0], 1)))
        w.write('</td><td>')
        if schoolName not in schoolNamesList:
            w.write('')
        elif schoolName not in schoolsDqmList:
            w.write('')
        elif not runSchoolsSummary[schoolName][1]:
            w.write('')
        else:
            w.write(str(round(runSchoolsSummary[schoolName][1], 1)))
        w.write('</td><td>')
        if schoolName not in schoolsDqmList:
            w.write('')
        else:
            w.write('<a href=\"dqm/')
            w.write(schoolName)
            w.write('/\">')
            w.write(schoolName)
            w.write('</a>')
        w.write('</td></tr>')
    w.write('</table>')
    w.write(FOOTER_HTML)
    w.write(set_version())
    w.write(BOTTOM_HTML)
    f.close()
    w.close()
    logger.info('Function make_main_page() finished')
    return True
