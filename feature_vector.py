import os
import sys
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# Function to convert list to string
fv_noncsv = re.compile('[\[|\]|\s]')

def list2str(l):
    return re.sub(fv_noncsv, '', str(l))

# Define directories and dictionary
data_dir = os.path.join(os.getcwd(), "mp3data")
training_dir = os.path.join(os.getcwd(), "mp3data", "preprocessed")
mp_dict = {}
fv_dict = {}

# Read the dictionary.txt for easy hashing
ndx = 0
with open(os.path.join(data_dir, "dictionary.txt")) as f:
    for line in f:
        line = line.strip()
        mp_dict[line] = ndx
        ndx += 1

# Get the training set
training_set = open(os.path.join(data_dir, "training_set.txt"), "r")
test_set = open(os.path.join(data_dir, "test_set.txt"), "r")

# Create the vectorizer
vectorizer = CountVectorizer(vocabulary=mp_dict)

## TRAINING SET
# Create the list of file contents
path_abs = lambda rel: open(os.path.join(training_dir, rel.strip()), "r").read()
files = [path_abs(x) for x in test_set]
rows = len(files)

X = vectorizer.fit_transform(files)

print(str(X))
print("Done vectorizing, will now print to CSV")

# Import to csv file
#fo = open(os.path.join(data_dir, "dataset-training.csv"), 'w')
#fo_csr = open(os.path.join(data_dir, "dataset-training-sparse.npz"), 'w')

np.savez('dataset-test-sparse.npz', data=X.data, indices=X.indices, indptr=X.indptr, shape=X.shape)

'''
for r in range(rows):
    row = X[r].toarray()[0]
    #fo.write(list2str(X[r].toarray()[0].tolist()))
    for c in range(len(row)):
        if c > 0:
            fo.write(',')
        fo.write(str(row[c]))
    fo.write('\n')
    sys.stdout.write("\r{}/{}".format(r,rows))
    sys.stdout.flush()

fo.close()
training_set.close()
test_set.close()
'''
