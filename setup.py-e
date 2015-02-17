#!/usr/bin/env python
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
#
# Many thanks to Luca.Baldini@pi.infn.it

from distutils.core import setup
import glob

from __version__ import TAG


_NAME = 'e3monitor'

_DESCRIPTION = 'Online monitoring tool for the EEE experiment'

with open('README') as file:
    _LONG_DESCRIPTION = file.read()

_AUTHOR = 'Fabrizio Coccetti'

_AUTHOR_EMAIL = 'fabrizio.coccetti@centrofermi.it'

_LICENSE = 'GNU General Public License v3 or later'

_URL = 'https://bitbucket.org/centrofermi/e3monitor'

_PACKAGES = ['e3monitor', 'e3monitor.config',
             'e3monitor.html', 'e3monitor.tasks']

_PACKAGE_DIR = {'e3monitor': '.'}

_PACKAGE_DATA = {
    'e3monitor': ['LICENSE', 'README', 'apps'],
    'e3monitor.config': [],
    'e3monitor.html': ['e3monitor.css'],
    'e3monitor.tasks': []
    }

_SCRIPTS = glob.glob('apps/*.py')

_CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: '
    'GNU General Public License v3 or later (GPLv3+)',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering :: Physics'
    ]


if __name__ == '__main__':

    setup(name=_NAME,
          description=_DESCRIPTION,
          long_description=_LONG_DESCRIPTION,
          version=TAG,
          author=_AUTHOR,
          author_email=_AUTHOR_EMAIL,
          license=_LICENSE,
          url=_URL,
          packages=_PACKAGES,
          package_dir=_PACKAGE_DIR,
          package_data=_PACKAGE_DATA,
          scripts=_SCRIPTS,
          classifiers=_CLASSIFIERS)
