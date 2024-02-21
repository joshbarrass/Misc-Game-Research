#!/usr/bin/env python3
"""
setup.py file for building gsutil

Based on setup.py from SWIG documentation.
https://swig.org/Doc4.0/Python.html#Python_nn6
"""

from distutils.core import setup, Extension

example_module = Extension(
    '_gsutil',
    sources=['gsreg.cpp', 'gsutil.cpp', 'gsutil_wrap.cxx'],
)

setup(
    name='gsutil',
    version='0.1',
    author="Murugo",
    description="""Tool for simulating GS memory""",
    ext_modules=[example_module],
    py_modules=["gsutil"],
)
