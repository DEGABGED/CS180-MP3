import os
import sys
import numpy as np
from sklearn.naive_bayes import BernoulliNB
import scipy.sparse

# Import the CSRs
training_fv = scipy.sparse.load_npz('dataset-training-sparse.npz')
test_fv = scipy.sparse.load_npz('dataset-test-sparse.npz')
data_dir = os.path.join(os.getcwd(), "mp3data")

# Get the labels
training_labels = [i.strip() for i in open(os.path.join(data_dir, "training_labels.txt")).readlines()]
test_labels = [i.strip() for i in open(os.path.join(data_dir, "test_labels.txt")).readlines()]

nb_m = BernoulliNB()

# Fit according to training data
nb_m.fit(training_fv, training_labels)

# Predict and compare
test_results = nb_m.predict(test_fv).tolist()

acc = 0
size = len(test_results)
for i in range(size):
    if test_results[i] == test_labels[i]:
        acc += 1

print("Accuracy: {}".format(acc/size))
