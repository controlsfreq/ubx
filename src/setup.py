"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/eightdatabits/earendil
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='earendil',
    version='0.0.1',
    description='Eärendil GNSS Library',
    long_description=long_description,
    author='Liam Bucci',
    author_email='eightdatabits@gmail.com',
    license='MIT',
    url='http://github.com/eightdatabits/earendil',
    packages=[
        'earendil',
        'earendil.core',
        'earendil.nmea',
        'earendil.tools',
        'earendil.ubx'
    ],
    classifiers=[
        # Development Status
        'Development Status :: 3 - Alpha',
        # Intended Audience
        'Intended Audience :: Developers',
        # Topics
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: Software Development :: Libraries',
        # License
        'License :: OSI Approved :: MIT License',
        # Python versions supported
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    keywords='GPS GNSS UBX NMEA'
)