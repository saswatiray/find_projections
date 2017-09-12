from setuptools import setup
from distutils.core import Extension
import os

NAME = 'find_projections'
VERSION = '1.0'

REQUIRES = ['numpy >= 1.13']

find_projections_module = Extension('libfind_projections',
		           sources = ['src/binary_tree.cpp', 'src/projection.cpp', 'src/search.cpp', 'src/helper.cpp', 'src/numeric_binary_tree.cpp', 'src/discrete_binary_tree.cpp', 'src/datset.cpp', 'src/pyfind_projections.cpp'],
				   extra_compile_args=['-pthread'],
				   extra_link_args=['-shared', '-pthread', '-lboost_python', '-lboost_numpy']
)

setup(
        name = NAME,
		version = VERSION,
		url = 'http://autonlab.org',
		author = 'Saswati Ray',
		author_email = 'sray@cs.cmu.edu',
		description = 'Search for 2-d projection boxes separating out classes/quantiles of output',
		ext_modules = [ find_projections_module ],
		packages = ['src']
)
