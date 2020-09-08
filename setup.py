# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# S3 Repository Demo is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""An OArepo repository instance using S3 for records attachments storage"""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

OAREPO_VERSION = os.environ.get('OAREPO_VERSION', '3.3.0')

tests_require = []

install_requires = [
    'oarepo-micro-api>=1.0.2',
    'invenio-s3'
]

setup_requires = []

extras_require = {
    'all': []
}

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('s3_demo', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='s3-demo',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='s3-demo Invenio',
    license='MIT',
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    author='Miroslav Bauer',
    author_email='bauer@cesnet.cz',
    url='https://github.com/oarepo/s3-demo',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            's3-demo = invenio_app.cli:cli',
        ]
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)
