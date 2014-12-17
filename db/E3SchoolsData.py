# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 16:06:54 2014

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
"""


class E3SchoolsData:

    def __init__(self):
        self.name = []
        self.name.dqmdata = []

    def addSchool(self, school):
        self.name.append(school)

    def displaySchools(self):
        print(self.name)

    def displayDqm(self, name):
        print(self.name.dqmdata)
