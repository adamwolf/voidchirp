#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from setuptools import setup, find_packages

NAME = "voidchirp"
DESCRIPTION = "Post to Twitter from the CLI"
URL = "https://github.com/adamwolf/voidchirp"
EMAIL = "adamwolf@feelslikeburning.com"
AUTHOR = "Adam Wolf"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = "0.1.0.dev0"
LICENSE = ("AGPL-3.0",)

PROJECT_URLS = {
    "Bug Tracker": "https://github.com/adamwolf/voidchirp/issues",
    "Source Code": "https://github.com/adamwolf/voidchirp",
}

REQUIRED = ['Click', 'tweepy', 'keyring']
EXTRAS_REQUIRE = {"tests": ["pytest", "coverage"]}
EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["tests"] + ["pre-commit", "black"]


def forbid_publish():
    argv = sys.argv
    blacklist = ["register", "upload"]

    for command in blacklist:
        if command in argv:
            values = {"command": command}
            print('Command "%(command)s" has been blacklisted, exiting...' % values)
            sys.exit(2)


forbid_publish()

setup(
    name=NAME,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    project_urls=PROJECT_URLS,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=REQUIRED,
    extras_require=EXTRAS_REQUIRE,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'voidchirp=voidchirp.voidchirp_cli:cli',
            'voidchirp-configure-auth=voidchirp.voidchirp_configure_auth:cli_configure_auth'

        ]
    },
)
