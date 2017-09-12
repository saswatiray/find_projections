# Makefile for ~/h/find_projections
# Created by sray on:  Thu May  5 16:41:24 EDT 2016

here		= find_projections

includes	= binary_tree.hpp projection.hpp search.hpp helper.hpp numeric_binary_tree.hpp feature_tree.hpp feature_map.hpp \
		  discrete_binary_tree.hpp  discrete_projection.hpp numeric_projection.hpp datset.hpp 
	
sources		= binary_tree.cpp projection.cpp search.cpp helper.cpp numeric_binary_tree.cpp discrete_binary_tree.cpp datset.cpp pyfind_projections.cpp

private_sources =

siblings	= 

user_flags += -fexceptions -fasynchronous-unwind-tables -fno-strict-aliasing -I/usr/include/python2.7
extra_libs += -lpthread -lboost_python -lboost_numpy -lpython2.7

t:=debug

include ./gmake-magic/Make.common
