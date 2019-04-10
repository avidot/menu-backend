#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    name='menu_backend',
    description="Backend de gestion de menu",
    version='0.2.10',
    author="Adrien VIDOT",
    author_email='adrien.vidot@gmail.com',
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    keywords='menu_backend',
    packages = ['menu_backend', 'menu_backend/commands', 'menu_backend/database', 'menu_backend/model', 'menu_backend/utils'],
    include_package_data=True,
    #packages=find_packages(),
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    url='https://github.com/avidot/menu_backend',
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests'
)
