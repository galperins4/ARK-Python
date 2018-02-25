#!/usr/bin/env python

try:
    from setuptools import setup
    import wheel
except ImportError:
    from distutils.core import setup

setup(
    name='ARK Python',
    description='An ARK bridge for Python.',
    version='1.0.0',
    author='Brian Faust',
    author_email='hello@brianfaust.me',
    url='https://github.com/faustbrian/ARK-Python',
    packages=['park', 'park.api', 'park.builder', 'park.builder.templates'],
    install_requires=[
        'wheel', 'Naked', 'Jinja2', 'requests', 'pyyaml', 'MarkupSafe',
        'certifi', 'urllib3', 'chardet', 'idna'
    ])
