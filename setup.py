#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

setup(name = 'analysis_tools',
      description = 'Package for astronomical analysis tools',
      author = 'C.M. Gosmeyer',
      url = 'https://github.com/cgosmeyer/analysis_tools',
      packages = find_packages(),
      install_requires = ['astropy', 'numpy']
     )