#from setuptools import setup
from distutils.core import setup, Extension
import os

NAME = 'find_projections'
VERSION = '1.0'

REQUIRES = ['numpy >= 1.13']

find_projections_module = Extension('libfind_projections',
		           sources = ['find_projections/binary_tree.cpp', 'find_projections/projection.cpp', 'find_projections/search.cpp', 'find_projections/helper.cpp', 'find_projections/numeric_binary_tree.cpp', 'find_projections/discrete_binary_tree.cpp', 'find_projections/datset.cpp', 'find_projections/pyfind_projections.cpp'],
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
		packages = ['find_projections']
)
