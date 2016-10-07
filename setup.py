# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

setup(
    name='q2cli',
    version='0.0.3',
    license='BSD-3-Clause',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['click', 'qiime >= 2.0.2', 'pip'],
    scripts=['bin/register-qiime-completion'],
    entry_points='''
        [console_scripts]
        qiime=q2cli.__main__:qiime
    ''',
)
