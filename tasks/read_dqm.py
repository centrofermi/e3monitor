# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 17:44:34 2014

@author: Fabrizio Coccetti
"""
import os


def read_dqm_summary(schoolNamesList, pathDqm):
    '''Read last run .summary in DQM directories
    The structure is /BOLO-03/2014-11-12/BOLO-03-2014-11-12-00054/.summary
    '''
    runSummary = {}
    runSchoolsSummary = {}
    # list of schools that actually have records in DQM
    schoolsDqmList = []
    for dirSchoolName in schoolNamesList:
        try:
            dirDates = os.listdir(os.path.join(pathDqm, dirSchoolName))
            schoolsDqmList.append(dirSchoolName)
        except:
            runSchoolsSummary[dirSchoolName] = ('', '', 'none')
            continue
        # Get the directory of last day of DQM
        # check if there are no runs in the directory, else proceed to
        #  the sublevel of date dir
        if len(dirDates) < 1:
            runSchoolsSummary[dirSchoolName] = ('', '', 'none')
        else:
            lastDirDate = sorted(dirDates)[-1]
            dirRunNumbers = \
                os.listdir(os.path.join(pathDqm, dirSchoolName, lastDirDate))
            try:
                lastRun = sorted(dirRunNumbers)[-1]
            except:
                runSchoolsSummary[dirSchoolName] = ('', '', 'none')
                continue
            if os.path.isfile(
                    os.path.join(pathDqm, dirSchoolName,
                                 lastDirDate, lastRun, '.summary')) is True:
                with open(os.path.join(pathDqm, dirSchoolName, lastDirDate,
                                       lastRun, '.summary'), 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        v1, v2 = line.split(':')
                        runSummary[v1.strip()] = v2.strip()
                if float(runSummary['run_duration']) > 0:
                    runRateEvents = (float(runSummary['num_events']) /
                                     float(runSummary['run_duration']))
                    runRateTracks = (float(runSummary['num_tracks']) /
                                     float(runSummary['run_duration']))
                else:
                    runRateEvents = ''
                    runRateTracks = ''
                runSchoolsSummary[dirSchoolName] = \
                    (runRateEvents, runRateTracks, runSummary['alarm_status'])
            else:
                runSchoolsSummary[dirSchoolName] = ('', '', 'none')
    return runSchoolsSummary, schoolsDqmList
