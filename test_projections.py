#!/bin/env python27

import sys, csv
import numpy
import find_projections.search_projections as search_projections

# Read input feature set
result = numpy.random.rand(1000,2).astype("float")

ds = search_projections.Datset(result)

# CLASSIFICATION
# Read output feature for classification
output = numpy.random.randint(2, size=(1000,)).astype("float")
ds.setOutputForClassification(output)

# Create search object and parameters
search_object = search_projections.Search()
binsize = 10
support = 100
purity = 0.5
mode = 1
num_threads = 1

# Search comprehensively for projection boxes
fmap = search_object.search_projections(ds, binsize, support, purity, mode, num_threads)

num = fmap.get_num_projections()
# Loop through all the projections in order of attributes
for i in range(num):
  pr = fmap.get_projection(i)
  #print pr.get_total()
  #print pr.get_att1()
  #print pr.get_neg()
  #print pr.get_class()
  pr.pprojection()

# Search for easy-to-classify data (decision list)
validation_set = 0.1
fmap = search_object.find_easy_explain_data(ds, validation_set, binsize, support, purity, mode, num_threads)

num = fmap.get_num_projections()
# Loop through all the projections in order of attributes
for i in range(num):
  pr = fmap.get_projection(i)
  #print pr.get_total()
  #print pr.get_pos()
  #print pr.get_neg()
  #print pr.get_class()
  pr.pprojection()

# REGRESSION
ds.setOutputForRegression(output)

support = 20
# Search comprehensively for projection boxes
fmap = search_object.search_projections(ds, binsize, support, purity, mode, num_threads)

num = fmap.get_num_projections()

# Loop through all the projections in order of attributes
for i in range(num):
  pr = fmap.get_projection(i)
  #print pr.get_total()
  #print pr.get_mean()
  #print pr.get_sum_sq_error()
  pr.pprojection()
