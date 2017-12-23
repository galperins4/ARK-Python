#!/usr/bin/env python

try:
    from setuptools import setup
    import wheel
except ImportError:
    from distutils.core import setup

setup(
    name='ARK Python Client',
    description='An Ark Client for Python 3',
    version='1.0.0',
    author='Brian Faust',
    author_email='hello@brianfaust.me',
    url='https://github.com/faustbrian/ARK-Python-Client',
    packages=['park', 'park.api', 'park.builder'],
    install_requires=['wheel', 'Naked', 'Jinja2', 'requests', 'pyyaml', 'MarkupSafe', 'certifi', 'urllib3', 'chardet', 'idna']
)
