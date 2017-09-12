Dataset should be a csv file with no missing values.
Label attribute can be categorical (0,1,2 or apples,oranges,bananas) or numeric(0.25,3.67..)

Two modes of running program -
-------------------------------

1) Search for informative projection boxes.
Run as -
./find_projections ds <csv_file> label <label_name> [binsize <value>] [support <value>] [purity <value>] [threads <value>] [mode <value>]

IF OUTPUT/LABEL ATTRIBUTE IS CATEGORICAL -
Searches for maximum sum boxes.
ELSE
Searches for low variance (default) or high mean or low mean (tight confidence band of 1 standard error width) regions.

Prints out all projection boxes which meet the criteria in an output file called boxes.csv.
This is done for each feature pair and for each class (for categorical output).

2) For categorical output, run the following command to split data into train and validation (random 10%) sets.
   Decision list(exclusive set of rules) is learnt from training data where each rule meets similar or better purity than supplied.
   The objective is to find how much proportion of data(any of the classes) is easy explained with 2-d projections.
 
   ./find_projections option easy ds <csv_file> label <label_name> [binsize <value>] [support <value>] [purity <value>] [threads <value>]

3) Run 10-fold CV on a dataset.
Run as -
./find_projections option kfold ds <csv_file> label <label_name> [binsize <value>] [support <value>] [purity <value>] 

Outputs predictions.csv file containing classwise sum-of-probabilities from each projection in training data for discrete output problem.
Outputs predictions.csv file containing aggregated mean, sum-sq-error from each projection in training data for numeric output problem.


Default values -
-----------------
binsize - 10 (Should be positive integer denoting the min. number of data points at each leaf
threads - 1 (If >1, will run multi-threaded on Linux)
support - 100 (Min. no. of data points in each projection found)
purity - 0.9 (Purity of each projection found)
mode - 0 (For numeric output, tries to find low variance boxes)
output_prefix - NULL (Specify prefix for output file boxes.csv. This could be a path too.)

Valid values for mode(0) are -
-------------------------------
0 : Tries to find low variance boxes
1 : Tries to find high mean boxes
2 : Tries to find low mean boxes
