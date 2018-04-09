import os
import sys
import re

# Define directories and dictionary
data_dir = os.path.join(os.getcwd(), "mp3data")
mp_dict = {}

# Read the dictionary.txt for easy hashing
with open(os.path.join(data_dir, "dictionary.txt")) as f:
    for line in f:
        mp_dict[line.strip()] = 1

