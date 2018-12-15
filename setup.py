#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'guillotina>=4.3.5']

setup_requirements = ['pytest-runner', ]

test_requirements = [
    'coverage',
    'docker',
    'pytest',
    'pytest-asyncio',
    'pytest-cov',
    'pytest-docker-fixtures',
]


setup(
    author="Md Nazrul Islam",
    author_email='email2nazrul@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="HEART (Health Relationship Trust) Python implementation.",
    entry_points={
        'console_scripts': [
            'heart=heart.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='heart',
    name='heart',
    packages=find_packages('src', include=['heart']),
    package_dir={'': 'src'},
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    extras_require={
      'test': test_requirements + setup_requirements
    },
    url='https://github.com/nazrulworld/heart',
    version='0.1.0',
    zip_safe=False,
)
