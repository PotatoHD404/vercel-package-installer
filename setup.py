#! /usr/bin/env python
import json

from setuptools import setup


with open('package.json') as f:
    package_data = json.loads(f.read())
    version = package_data['version']

# vercel-package-installer
"""A barebones setup for tests
"""
setup(
    name='vercel-package-installer',
    version=version,
    packages=[
        'vercel_package_installer'
    ],
    install_requires=[
        'Werkzeug==1.0.1',
        'apig-wsgi'
    ]
)
