#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools

def main():
    setuptools.setup(
        name                 = "folktales",
        version              = "2018.05.03.0230",
        description          = "creation, access and modification of SQL databases",
        url                  = "https://github.com/wdbm/folktales",
        author               = "Will Breaden Madden",
        author_email         = "wbm@protonmail.ch",
        license              = "GPLv3",
        packages             = setuptools.find_packages(),
        install_requires     = [
                               "dataset",
                               "pandas",
                               "technicolor"
                               ],
        include_package_data = True,
        zip_safe             = False
    )

if __name__ == "__main__":
    main()
