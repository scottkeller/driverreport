import os
from setuptools import setup

def readfile(*names):
    """
Helper utility. Read text from file to help keep setup.py DRY.
    """
    thisfile = os.path.abspath(__file__)
    thisfile = os.path.join(os.path.dirname(thisfile), *names)
    with open(thisfile) as fp:
        return fp.read()

setup(
    name='driverreport',
    version='0.0.1',
    packages=['driverreport',],
    author='Scott Keller',
    author_email='scottjameskeller@gmail.com',
    url='https://github.com/scottkeller/driver-report',
    description="Generates a report of drivers and trip statistics",
    license='MIT',
    long_description=readfile('README'),
    install_requires=['fire'],
    entry_points={
        'console_scripts': [
            'driverreport = driverreport.cli.cli:_main',
        ],
    },
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)