# -*- coding: utf-8 -*-
#
# To create wheel:
#     python setup.py bdist_wheel
#
from pathlib import Path

from setuptools import setup

setup(
    version='1.4',
    name='hols-uk',
    description='Python module to determine UK working days.',
    long_descriptions=Path('README.rst').read_text(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: ISC License (ISCL)',
    ],
    url='https://github.com/recombinant/hols-uk/',
    author='',
    author_email='',
    license='ISC',
    packages=['hols_uk'],
    include_package_data=True,
)
