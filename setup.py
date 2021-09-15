# See license.txt for license details.
# Copyright (c) 2021, Chris Withers

import os

from setuptools import setup, find_packages

base_dir = os.path.dirname(__file__)

setup(
    name='trashcan',
    version='0.0.0.dev0',
    author='Chris Withers',
    author_email='chris@withers.org',
    license='MIT',
    description=(
        "Background deletion of files and directories you no longer need."
    ),
    long_description=open('README.rst').read(),
    url='https://github.com/simplistix/trashcan',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9',
    ],
    packages=find_packages(exclude=["tests"]),
    zip_safe=False,
    include_package_data=True,
    extras_require=dict(
        test=[
            'pytest',
            'pytest-cov',
            'sybil',
            'testfixtures',
        ],
        build=['furo', 'sphinx', 'setuptools-git', 'twine', 'wheel']
    ),
)
