import glob
from pathlib import Path
import re
import pybind11
from setuptools import setup, find_packages, Extension



extensions = [Extension(name='add_fun', sources=['add_fun.cpp'], include_dirs=[pybind11.get_include(False),pybind11.get_include(True),],language='c++'),]




setup(
name= 'Add_Numbers',
version='1.0',
description='Adds two numbers',
author='Amlan',
packages=find_packages(),
install_requires=['numpy>=1.16.3',
        'scipy>=1.6.0',
        'matplotlib>=1.0.0',
        'python-dateutil',
        'pybind11>=2.2.0'],
setup_requires=['setuptools_scm>=3.5.0',
        'pytest-runner', 'flake8'],
tests_require=['pytest'],
zip_safe=False,
ext_modules=extensions,
package_data={},
)


