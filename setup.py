#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import urllib
import tarfile
import logging
import tempfile
from distutils.core import setup
from subprocess import check_call
from setuptools import setup
from setuptools import find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop


parsed_requirements = parse_requirements(
    'requirements.txt',
    session=PipSession())
parsed_test_requirements = parse_requirements(
    'requirements_dev.txt',
    session=PipSession())
requirements = [str(ir.req) for ir in parsed_requirements]
test_requirements = [str(tr.req) for tr in parsed_test_requirements]


setup(name='textnormalizer',
      version='0.1',
      description='Text normalization package for natural language processing',
      url='http://github.com/cyrta/textnormaler',
      author='Pawel Cyrta',
      author_email='pawel@cyrta.com',
      license='MIT',
      packages=[''],
      zip_safe=False,
      include_package_data=True,
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Environment :: Other Environment',
       ],
      keywords=[ 'text normalization', 'text cleaning', 'NLP', 'natural language processing'] 
      python_requires='>=3.6',
      install_requires=requirements,
      tests_require=test_requirements,
      entry_points = {
       "console_scripts": [ 'textnormalizer = textnormalize.cli:main'],
      }
	
    )

