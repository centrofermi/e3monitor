# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 19:53:55 2014

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
"""

import pickle
import os


def read_pickle(pathWorkDir, pklFile):
    '''Read the pickle file in the work directory
    '''

    pkl_file = open(os.path.join(pathWorkDir, pklFile), 'rb')
    return pickle.load(pkl_file)
