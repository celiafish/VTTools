#!/usr/bin/env python

import setuptools
from distutils.core import setup, Extension
from setupext import ext_modules
import numpy as np
import os
import shutil
from subprocess import call
import sys

setup(
    name='vttools',
    version='0.0.x',
    author='Brookhaven National Lab',
    packages=["vttools",
              'vttools.vtmods'
              ],
    include_dirs=[np.get_include()],
    ext_modules=ext_modules
    )


src = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'vt_config',
                   'NSLS-II')
dst = os.path.join(os.path.expanduser('~'), '.vistrails', 'userpackages',
                   'NSLS-II')

from vttools.utils import make_symlink
make_symlink(dst=dst, src=src)