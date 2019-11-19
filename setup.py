#!/usr/bin/env python

import os, sys
from distutils.core import setup
from glob import glob

from setuptools import find_packages

setup(name='scc',
      version='1.0',
      description='Site-Connectivity-Checker',
      author='Zidong Zhang',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      py_modules=[os.path.splitext(os.path.basename(path))[0] for path in glob('src/*.py')],
     )