# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='farm_management',
    version=version,
    description='An app to complement ERPNext for commercial farmers',
    author='Ifitwala Farm Ltd.',
    author_email='francois@ifitwala.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
