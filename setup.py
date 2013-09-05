#!/usr/bin/env python

from setuptools import setup

if __name__ == '__main__':
    setup(
        name = 'the',
        version = '0.0.1',
        description = 'rspec assertion style for python test',
        long_description = 'rspec assertion style for python test',
        author = "Yan Wenjun",
        author_email = "mylastnameisyan@gmail.com",
        license = 'MIT',
        url = 'https://github.com/v2e4lisp/the',
        scripts = [],
        packages = ['src'],
        classifiers = [
            'License :: OSI Approved :: MIT License',
            'Topic :: Software Development :: Libraries',
            'Topic :: Test'
        ]
    )
