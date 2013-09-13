#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import pysterisk


setup(name='pysterisk',
    version=pysterisk.__version__,
    description=pysterisk.__description__,
    long_description=pysterisk.__description__,
    author=pysterisk.__author__,
    license=pysterisk.__license__,
    packages=find_packages(exclude=('doc', 'docs', 'example')),
    package_dir={'pysterisk': 'pysterisk'},
    include_package_data=True)
