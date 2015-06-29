#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='netskope',
      version='0.1',
      description='RESTful interface to NetSkope',
      author='Josh Madeley',
      author_email='josh.madeley@me.com',
      url='https://www.github.com/joshmad/netskope',
      license = 'Apache',
      packages=['netskope'],
      install_requires = ['httplib2>=0.9.1']
     )