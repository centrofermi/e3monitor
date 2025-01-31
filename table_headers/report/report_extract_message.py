#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *********************************************************************
# * Copyright (C) 2014 Fabrizio Coccetti                              *
# * fabrizio.coccetti@centrofermi.it  [www.fc8.net]                   *
# *                                                                   *
# * For the license terms see the file LICENSE, distributed           *
# * along with this software.                                         *
# *********************************************************************
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
Created on Wed Sep 27 12:19:00 2017

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
"""

messagesDict={}

# Read file with messages
with open('/var/www/html/monitor/report/report_messages.txt', 'r') as f:
    for line in f:
        try:
            _school, _textmessage = line.split('\t',1)
            messagesDict[_school] = _textmessage.rstrip()
        except:
            continue

# Return messages

for i in messagesDict:
    if messagesDict[i]: 
        print i,": " , messagesDict[i]

