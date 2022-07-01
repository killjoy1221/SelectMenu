#!/usr/bin/env python
# coding: utf-8
import re

from setuptools import setup, find_packages

with open("README.rst", "r", encoding="utf-8") as fp:
    long_description = fp.read()

with open("requirements.txt") as fp:
    requirements = fp.readlines()

init_vars = {}
with open("selectmenu/__init__.py") as fp:
    for line in fp:
        m = re.match(r'^(\w+) *= *"(.+)"$', line)
        if m:
            name, value = m.groups()
            init_vars[name] = value

__author__ = init_vars["__author__"]
__version__ = init_vars["__version__"]

setup(
    name="SelectMenu",
    author=__author__,
    author_email="takemehighermore@gmail.com",
    description=(
        "SelectMenu is the input form to choose from menu by arrow keys."),
    long_description=long_description,
    version=__version__,
    license="MIT License",
    url="https://github.com/alice1017/SelectMenu",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'License :: OSI Approved :: MIT License',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ]
)
