#!/bin/env python

import libfind_projections
import numpy as np

def validate_params(ds, binsize, support, purity, mode, num_threads):
    if ds.isValid() is False:
        return False

    size = ds.getSize()

    if ( binsize <= 0 )  or ( binsize >= size ):
        return False
        
    if ( support >= size ) :
        return False
        
    if ( purity <= 0.0 ) or ( purity >= 1.0 ) :
        return False  

    if ( num_threads < 1 ) :
        return False;

    return True

class Search:
     """
     Class to perform different types of search operations
     """
     def __init__(self):
         self.search_obj = libfind_projections.search()
         
     """
     Comprehensively evaluates all possible pairs of 2-d projections in the data
     Returns all projection boxes which match search criteria
     :param ds: Datset instance created with your dataset
     :type: Datset 
     :param binsize: No. of data points for binning. Should be a positive integer
     :type: Integer
     :param support: Minimum number of data points to be present in a projection box for evaluation. Should be a positive integer
     :type: Integer
     :param purity: Minimum purity (class proportion) in a projection box. Should be in the range 0.0 - 1.0
     :type: Double
     :param mode: Used for numeric output (regression-based analysis). Valid values are 0, 1, 2.
     :type: Integer
     :param num_threads: No. of threads for multi-threaded operation. Should be a positive integer
     :type: Integer
     :returns: FeatureMap instance containing all the projection boxes found meeting the search criteria
     :rtype: FeatureMap
     """
     def search_projections(self, ds, binsize=10, support=50, purity=0.9, mode=0, num_threads=1):
         valid = validate_params(ds, binsize, support, purity, mode, num_threads)
         if valid is False:
             return None
         return FeatureMap(self.search_obj.search_projections(ds.ds, binsize, support, purity, mode, num_threads))

     """
     Learns decision list of projection boxes for easy-to-explain data (for classification/regression)
     :param ds: Datset instance created with your dataset
     :type: Datset 
     :param validation_size: Proportion of training data which is held out for validation purposes. Should be in the range 0.0 - 0.5
     :type: Double
     :param binsize: No. of data points for binning. Should be a positive integer
     :type: Integer
     :param support: Minimum number of data points to be present in a projection box for evaluation. Should be a positive integer
     :type: Integer
     :param purity: Minimum purity (class proportion) in a projection box. Should be in the range 0.0 - 1.0
     :type: Double
     :param mode: Used for numeric output (regression-based analysis). Valid values are 0, 1, 2.
     :type: Integer
     :param num_threads: No. of threads for multi-threaded operation. Should be a positive integer
     :type: Integer
     :returns: FeatureMap instance containing all the projection boxes found meeting the search criteria
     :rtype: FeatureMap
     """
     def find_easy_explain_data(self, ds, validation_size=0.1, binsize=10, support=50, purity=0.9, mode=0, num_threads=1):
         valid = validate_params(ds, binsize, support, purity, mode, num_threads)
         if valid is False:
             return None
         if ( validation_size <= 0.0 ) or ( validation_size > 0.5 ) :
             return None
         return FeatureMap(self.search_obj.find_easy_explain_data(ds.ds, validation_size, binsize, support, purity, mode, num_threads))

    
class FeatureMap:
    """
    Container class containing projection boxes found from search operations
    """
    def __init__(self, fmap):
        self.fmap = fmap
        
    """
    Returns the total number of projection boxes in this container object
    """
    def get_num_projections(self):
        return self.fmap.get_num_projections()
    
    """
    Retrieve the i'th projection-box
    """
    def get_projection(self, i):
        if ( i <  0 ) :
            return None
        return self.fmap.get_projection(i)
    
class Datset:

     """
     Create Datset instance with numpy 2-d array of floats.
     """
     def __init__(self, data):
         rows = data.shape[0]
         cols = data.shape[1]

         if data.dtype <> 'float':
             return None

         self.ds = libfind_projections.Datset(data)
        
     """
     Set output array for classification/regression task
     If output data type is int, task is classification-based projection-box finding
     If output data type is float, task is regression-based projection-box finding
     """ 
     def setOutputForClassification(self, output):
         if ( np.issubdtype(output.dtype, np.float ) ) :
            self.ds.fill_datset_output_for_classification(output)  
         else:
             raise Exception("Invalid classification data type")

     """
     Set output array for classification/regression task
     If output data type is int, task is classification-based projection-box finding
     If output data type is float, task is regression-based projection-box finding
     """ 
     def setOutputForRegression(self, output):
         if ( np.issubdtype(output.dtype, np.float ) ) :
            self.ds.fill_datset_output_for_regression(output)  
         else:
             raise Exception("Invalid regressionion data type")

     """
	 Checks if Datset instance has been populated properly.
	 """
     def isValid(self):
         return self.ds.is_valid()

     """
	 Returns the number of data points
	 """
     def getSize(self):
	     return self.ds.get_size()
