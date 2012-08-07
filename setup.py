#!/usr/bin/env python

from setuptools import setup, find_packages

name = "chardetails"

setup(
    name = name,
    version = "0.2.1",
    url = "http://silpa.org.in/chardetails",
    license = "LGPL-3.0",
    description = "Unicode character details Library",
    author = "Santhosh Thottingal",
    author_email = "santhosh.thottingal@gmail.com",
    long_description = "This library helps to get details of \
unicode characters.",
    packages = find_packages('.'),
    package_data = {'.':[]},
    include_package_data = True,
    setup_requires = ['setuptools-git'],
    install_requires = ['setuptools'],
    zip_safe = False,
    )
