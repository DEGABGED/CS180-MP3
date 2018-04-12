import os
import sys
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import scipy.sparse

# Function to convert list to string
fv_noncsv = re.compile('[\[|\]|\s]')

def list2str(l):
    return re.sub(fv_noncsv, '', str(l))

# Define directories and dictionary
#data_dir = os.path.join(os.getcwd(), "mp3data")
#preprocessed_dir = os.path.join(os.getcwd(), "mp3data", "preprocessed")

def gen_feature_matrix(data_dir, preprocessed_dir, dictionary="", gen_csv=True, gen_npz=True):
    # Define dictionaries
    mp_dict = {}
    fv_dict = {}

    # Read the dictionary for easy hashing
    ndx = 0
    with open(os.path.join(data_dir, "dictionary{}.txt".format(dictionary))) as f:
        for line in f:
            line = line.strip()
            mp_dict[line] = ndx
            ndx += 1

    # Get the training set
    training_set = open(os.path.join(data_dir, "training_set.txt"), "r")
    test_set = open(os.path.join(data_dir, "test_set.txt"), "r")

    # Create the vectorizer
    vectorizer = CountVectorizer(vocabulary=mp_dict)

    # Create the list of file contents
    path_abs = lambda rel: open(os.path.join(preprocessed_dir, rel.strip()), "r").read()

    training_files = [path_abs(x) for x in training_set]
    test_files = [path_abs(x) for x in test_set]

    training_rows = len(training_files)
    test_rows = len(test_files)

    training_X = vectorizer.fit_transform(training_files)
    test_X = vectorizer.fit_transform(test_files)

    print("Done vectorizing.")

    if gen_npz:
        print("Writing to NPZ")
        scipy.sparse.save_npz("dataset-training-sparse{}".format(dictionary), training_X)
        scipy.sparse.save_npz("dataset-test-sparse{}".format(dictionary), test_X)

    if gen_csv:
        print("Writing to CSV")
        # TRAINING
        fo = open(os.path.join(data_dir, "dataset-training{}.csv".format(dictionary)), 'w')
        for r in range(training_rows):
            row = training_X[r].toarray()[0]
            for c in range(len(row)):
                if c > 0:
                    fo.write(',')
                fo.write(str(row[c]))
            fo.write('\n')
            sys.stdout.write("\rTraining set: {}/{}".format(r,training_rows))
            sys.stdout.flush()
        fo.close()
        print('\nDone\n')

        # TEST
        fo = open(os.path.join(data_dir, "dataset-test{}.csv".format(dictionary)), 'w')
        for r in range(test_rows):
            row = test_X[r].toarray()[0]
            for c in range(len(row)):
                if c > 0:
                    fo.write(',')
                fo.write(str(row[c]))
            fo.write('\n')
            sys.stdout.write("\rTest set: {}/{}".format(r,test_rows))
            sys.stdout.flush()
        fo.close()
        print('\nDone\n')

    training_set.close()
    test_set.close()
