#!/usr/bin/env python

__author__    = 'RADICAL Team'
__email__     = 'radical@rutgers.edu'
__copyright__ = 'Copyright 2013-16, RADICAL Research, Rutgers University'
__license__   = 'MIT'


""" Setup script, only usable via pip. """

import os
import sys

name = 'saga-python'


try:
    from setuptools import setup, Command, find_packages
except ImportError as e:
    print("%s needs setuptools to install" % name)
    sys.exit(1)

license = 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'

setup_args = {
    'name'               : name,
    'version'            : '0.60.1',
    'description'        : 'This module provides backward compatibility for '
                           'radical.saga',
    'author'             : 'RADICAL Group at Rutgers University',
    'author_email'       : 'radical@rutgers.edu',
    'maintainer'         : 'The RADICAL Group',
    'maintainer_email'   : 'radical@rutgers.edu',
    'url'                : 'http://radical-cybertools.github.io/saga-python/',
    'license'            : license,
    'keywords'           : 'radical job saga',
    'classifiers'        : [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Environment :: Console',
        license,
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix'
    ],
    'packages'           : find_packages('src'),
    'package_dir'        : {'': 'src'},
    'install_requires'   : ['radical.saga>=0.60'],
    'zip_safe'           : False,
}


# ------------------------------------------------------------------------------
#
setup(**setup_args)

os.system('rm -rf src/%s.egg-info' % name)


# ------------------------------------------------------------------------------

