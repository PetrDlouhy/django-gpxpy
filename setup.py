#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='django-gpxpy',
    version='0.0.0',
    description='Django integration of GpxPy',
    long_description='Django integration of GpxPy',
    author=', '.join((
        'Petr Dlouhý <petr.dlouhy@email.cz>',
    )),
    author_email='petr.dlouhy@email.cz',
    url='https://github.com/PetrDlouhy/django-gpxpy',
    download_url='https://github.com/PetrDlouhy/django-gpxpy/archive/master.zip',
    install_requires=[
        'gpxpy',
    ],
    classifiers=[
        "Development Status :: 1 - Pre-Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
    packages=[
        'django-gpxpy',
    ],
)