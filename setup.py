#!/usr/bin/env python

from setuptools import setup

def readme():
    with open("README.rst") as it:
        return it.read()

if __name__ == '__main__':
    setup(
        name = 'the',
        version = '0.0.4',
        description = 'rspec/should.js assertion style for python test',
        long_description = readme(),
        author = "Yan Wenjun",
        author_email = "mylastnameisyan@gmail.com",
        license = 'MIT',
        url = 'https://github.com/v2e4lisp/the',
        py_modules = ["the"],
        classifiers = [
            'License :: OSI Approved :: MIT License',
            'Topic :: Software Development :: Libraries',
        ]
    )
