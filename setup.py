#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

version = "1.0.0"

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
      license="GNU GENERAL PUBLIC LICENSE",
      install_requires=["json","requests"],
      author="Izabela Ramos Ferreira",
      author_email="izabela.head@gmail.com",
      url="https://github.com/MissHead/izpy",
      packages = find_packages(),
      keywords= "generic calls, curl",
      zip_safe = True)