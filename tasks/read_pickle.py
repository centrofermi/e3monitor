# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 19:53:55 2014

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
"""

import pickle
import os
from e3monitor.config.__files_server__ import pathWorkDir, plkDataFile
from e3monitor.db.E3SchoolsData import E3SchoolsData


def read_pickle():
    '''Read the pickle file in the work directory
    '''

    pkl_file = open(os.path.join(pathWorkDir, plkDataFile), 'rb')
    dqmData = pickle.load(pkl_file)
    return dqmData
