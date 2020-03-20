# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="securitytxt-parsing",
    version="1.0",
    description="Python security.txt parser",
    license="MIT",
    author="Tom CHAMBARETAUD",
    packages=find_packages(),
    install_requires=["requests"],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ]
)