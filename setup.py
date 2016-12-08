#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

setup(name = 'muttontools',
      description = 'Mutton package',
      author = 'C.M. Gosmeyer',
      url = 'https://github.com/roastmutton/muttontools',
      packages = find_packages(),
      install_requires = ['numpy', 'sqlalchemy', 'astropy', 'pyyaml',
      					  'mock']
     )