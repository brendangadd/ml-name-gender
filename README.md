# First Name Gender Classifier

Creates a classifier for predicting the gender of a person's first name. Due to
the way features are extracted from the training set, samples for prediction
must have the same number of features and are thus bounded in length by the
longest name used for training.

A random forest classifier was used for prediction, for no reason other than a
friend said that random forests are cool. Validation of predictions against the
training data suggests that the classifier is approximately 90% accurate in its
predictions.

Training data was obtained from the Social Security department of the US
Government: [Popular Baby Names][baby-names] ([ZIP][baby-names-zip]).

[baby-names]: https://www.ssa.gov/oact/babynames/limits.html
[baby-names-zip]: https://www.ssa.gov/oact/babynames/names.zip
