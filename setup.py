# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='metadata',
    version='0.2',
    description='Metadata for Humans',
    long_description="""Metadata extract metadatas from files.""",
    author='Timothée Peignier',
    author_email='timothee.peignier@tryphon.org',
    url='https://github.com/cyberdelia/metadata',
    packages=find_packages(),
    install_requires=[
        'hachoir-core==1.3.3',
        'hachoir-metadata==1.3.3',
        'hachoir-parser==1.3.4',
    ],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)