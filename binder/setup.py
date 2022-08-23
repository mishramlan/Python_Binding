import glob
from pathlib import Path
import re
from setuptools import setup, find_packages, Extension




extensions = [Extension(name='add_fun', sources=['binder/add_fun.cpp'])]




setup(
name= 'Add_Numbers',
version='1.0',
description='Adds two numbers',
author='Amlan',
packages=find_packages(),
install_requires=['numpy>=1.16.3',
        'NuMPI>=0.3.0',
        'muFFT>=0.12.0',
        'scipy>=1.6.0',
        'matplotlib>=1.0.0',
        'python-dateutil',],
extras_require=[],
setup_requires=['setuptools_scm>=3.5.0',
        'pytest-runner', 'flake8'],
tests_require=['pytest'],
package_data={},
ext_libraries=extensions,
)


