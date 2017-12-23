#!/usr/bin/python

from distutils.core import setup

setup(
    name='ARK Python Client',
    description='An Ark Client for Python 3',
    version='1.0.0',
    author='Brian Faust',
    author_email='hello@brianfaust.me',
    url='https://github.com/faustbrian/ARK-Python-Client',
    packages=[
        'park'
        'park.api',
        'park.builder',
        # 'park.api.account',
        # 'park.api.block',
        # 'park.api.delegate',
        # 'park.api.loader',
        # 'park.api.multisignature',
        # 'park.api.peer',
        # 'park.api.signature',
        # 'park.api.transaction',
        # 'park.api.transport',
        # 'park.api.vote',
        # 'park.builder.delegate',
        # 'park.builder.multisignature',
        # 'park.builder.signature',
        # 'park.builder.transaction',
        # 'park.builder.vote',
    ],
    install_requires=['Naked', 'Jinja2', 'requests', 'pyyaml', 'MarkupSafe', 'certifi', 'urllib3', 'chardet', 'idna']
)
