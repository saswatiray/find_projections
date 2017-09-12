/*
 *    File:        datset.hpp
 *    Author(s):   Saswati Ray
 *    Created:     Wed Aug 30 10:19:52 EDT 2017
 *    Description: 
 *    Copyright (c) 2017 Carnegie Mellon University
 *    */

#ifndef DATSET_H_
#define DATSET_H_

#include <boost/python/numpy.hpp>

namespace p = boost::python;
namespace np = boost::python::numpy;

#include <boost/numeric/ublas/matrix.hpp>

using namespace boost::numeric::ublas;

/*
 * Class representing user data.
 * Consists of input feature space (matrix) and output vector.
 * Datset can be created by loading from csv file or by feeding in values from numpy arrays
 */
class Datset {
 private:
  matrix<double> *darray;
  std::vector<int> *output_class;
  std::vector<double> *output_regress;
  int rows, cols, num_classes;
  bool is_classifier;

 public:
  Datset();
  Datset(np::ndarray & array);

  void fill_datset_output_for_classification(np::ndarray  & array);
  void fill_datset_output_for_regression(np::ndarray & array);
  double ds_real_ref(int i, int j);
  double ds_output_ref(int i);
  int get_num_classes() {
    return num_classes;
  }

  ~Datset();

  bool is_classification() {
    return is_classifier;
  }

  bool is_valid() {
    return (darray && (output_class || output_regress));
  }

  int get_rows() {
    return rows;
  }
  int get_cols() {
    return cols;
  }
};

#endif
