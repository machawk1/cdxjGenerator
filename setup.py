#!/usr/bin/env python

from setuptools import setup
from cdxjGenerator import __version__

with open('README.md') as f:
    long_description = f.read()
desc = """Generate CDXJ TimeMaps for testing elsewhere"""

setup(
    name='cdxjGenerator',
    version=__version__,
    url='https://github.com/machawk1/cdxjGenerator',
    download_url="https://github.com/cdxjGenerator",
    author='Mat Kelly',
    author_email='me@matkelly.com',
    description=desc,
    packages=['cdxjGenerator'],
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    provides=[
        'cdxjGenerator'
    ],
    install_requires=[
        'Faker',
        'surt>=0.3.0',
        'tlds'
    ],
    entry_points="""
        [console_scripts]
        cdxjGenerator = cdxjGenerator.__main__:main
    """,
    zip_safe=False,
    keywords='web archives replay cdxj memento',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Environment :: Web Environment',

        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

        'License :: OSI Approved :: MIT License',

        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',

        'Topic :: Internet :: WWW/HTTP',
        'Topic :: System :: Archiving',
        'Topic :: System :: Archiving :: Backup',
        'Topic :: System :: Archiving :: Mirroring',
        'Topic :: Utilities'
    ]
)