# pylint: disable=missing-docstring
#
# Copyright (C) 2016 srforge project developers.
#
# See the COPYRIGHT file at the top-level directory of this distribution and at
# https://github.com/alunduil/srforge/blob/master/COPYRIGHT
#
# srforge is freely distributable under the terms of an MIT-style license.
# See LICENSE or http://www.opensource.org/licenses/mit-license.php.

import os

from codecs import open  # pylint: disable=redefined-builtin
from setuptools import find_packages
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'srforge', 'information.py'), 'r', encoding = 'utf-8') as fh:
    exec(fh.read(), globals(), locals())  # pylint: disable=exec-used

PARAMS = {}

PARAMS['name'] = NAME  # provided by exec—pylint: disable=undefined-variable
PARAMS['version'] = VERSION  # provided by exec—pylint: disable=undefined-variable
PARAMS['description'] = DESCRIPTION  # provided by exec—pylint: disable=undefined-variable

with open('README.rst', 'r', encoding = 'utf-8') as fh:
    PARAMS['long_description'] = fh.read()

PARAMS['url'] = URL  # provided by exec—pylint: disable=undefined-variable
PARAMS['author'] = AUTHOR  # provided by exec—pylint: disable=undefined-variable
PARAMS['author_email'] = AUTHOR_EMAIL  # provided by exec—pylint: disable=undefined-variable
PARAMS['license'] = LICENSE  # provided by exec—pylint: disable=undefined-variable

PARAMS['classifiers'] = [
    'Development Status :: 1 - Planning',
    # 'Development Status :: 2 - Pre-Alpha',
    # 'Development Status :: 3 - Alpha',
    # 'Development Status :: 4 - Beta',
    # 'Development Status :: 5 - Production/Stable',
    # 'Development Status :: 6 - Mature',
    # 'Development Status :: 7 - Inactive',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Games/Entertainment',
    'Topic :: Games/Entertainment :: Role-Playing',
]

PARAMS['keywords'] = [
    'shadowrun',
    'shadworun fifth edition',
]

PARAMS['packages'] = find_packages(exclude = [ '*_tests', ])

PARAMS['install_requires'] = [
    'mypy-lang',
]

PARAMS['tests_require'] = [
    'behave',
    'coverage',
    'hypothesis',
    'nose',
]

PARAMS['data_files'] = [
    ( 'share/doc/{P[name])-{P[version]}'.format(P = PARAMS), [  # pylint: disable=bad-format-string
        'README.rst',
    ]),
]

setup(**PARAMS)
