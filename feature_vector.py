import os
import sys
import re

# Define directories and dictionary
data_dir = os.path.join(os.getcwd(), "mp3data")
training_dir = os.path.join(os.getcwd(), "sample")
mp_dict = {}
fv_dict = {}

# Read the dictionary.txt for easy hashing
with open(os.path.join(data_dir, "dictionary.txt")) as f:
    for line in f:
        line = line.strip()
        mp_dict[line] = 0
        fv_dict[line] = 0

# For all files, create a csv
