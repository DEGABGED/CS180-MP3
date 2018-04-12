import os
import sys
import numpy as np
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
import scipy.sparse

def naive_bayes(data_dir, model="multinomial", fv="", alpha=1.0):
    # Import the CSRs
    training_fv = scipy.sparse.load_npz("dataset-training-sparse{}.npz".format(fv))
    test_fv = scipy.sparse.load_npz("dataset-test-sparse{}.npz".format(fv))

    # Get the labels
    training_labels = [i.strip() for i in open(os.path.join(data_dir, "training_labels.txt")).readlines()]
    test_labels = [i.strip() for i in open(os.path.join(data_dir, "test_labels.txt")).readlines()]

    if model == "multinomial":
        nb_m = MultinomialNB(alpha=alpha)
    else:
        nb_m = BernoulliNB(alpha=alpha)

    # Fit according to training data
    nb_m.fit(training_fv, training_labels)

    # Predict and compare
    training_results = nb_m.predict(training_fv).tolist()
    test_results = nb_m.predict(test_fv).tolist()

    # Calculate the accuracy
    acc = 0
    size = len(test_results)
    for i in range(size):
        if test_results[i] == test_labels[i]:
            acc += 1
    test_percentage = acc*100.0/size

    acc = 0
    size = len(training_results)
    for i in range(size):
        if training_results[i] == training_labels[i]:
            acc += 1
    training_percentage = acc*100.0/size

    return (training_percentage, test_percentage)
