#!/usr/bin/env python

from setuptools import setup

def main():
    setup(
        name='blodgie',
        version='0.0',
        scripts=['blodgie'],
        install_requires=['ikea_api','tabulate'],
    )

if __name__ == '__main__':
    main()