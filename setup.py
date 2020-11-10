#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

version = "0.0.5"

with open("README.md", "r") as fh:
    long_description = fh.read()

# python setup.py tag
if sys.argv[-1] == 'tag':
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

# python setup.py publish
if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    sys.exit()

setup(name="izpy",
      version=version,
      description="AbstractTest class for generic calls in integration testing of API's",
      long_description=long_description,
      long_description_content_type="text/markdown",
      license="GNU GENERAL PUBLIC LICENSE",
      author="Izabela Ramos Ferreira",
      author_email="izabela.head@gmail.com",
      url="https://github.com/MissHead/izpy",
      packages=["izpy"],
      package_dir={"izpy": "izpy"},
      keywords="generic calls, curl, errors",
      zip_safe=True,
      python_requires='>=3.6')