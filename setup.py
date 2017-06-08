# Copyright (c) 2016 The Regents of the University of Michigan
# All rights reserved.
# This software is licensed under the BSD 3-Clause License.
import sys

if sys.version_info < (2, 7, 0):
    print("Error: signac-flow requires python version >= 2.7.x.")
    sys.exit(1)

requirements = []
if sys.version_info < (3, 4, 0):
    requirements.append('enum34')

from setuptools import setup, find_packages

setup(
    name='signac-flow',
    version='0.5.1',
    packages=find_packages(),
    zip_safe=True,

    author='Carl Simon Adorf',
    author_email='csadorf@umich.edu',
    description="Simple workflow management based on signac.",
    keywords='workflow management signac framework database',

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Scientific/Engineering :: Physics",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    entry_points={
        'console_scripts': [
            'flow = flow.__main__:main',
        ],
    },
    install_requires=requirements,
)
