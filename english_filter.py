import os
import sys
import re
import enchant
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

d = enchant.Dict("en_US")

# Define our dictionary
mp_dict = {}
stop_dict = {}
stem_dict = {}

n = 45252
dc_digit = re.compile('\d')

# Define directories
src_dir = os.path.join(os.getcwd(), "mp3data", "preprocessed")
dest_dir = os.path.join(os.getcwd(), "mp3data")

# Load English dictionary
en_dict = {}
with open("words.txt") as f:
    for line in f:
        en_dict[line.strip().lower()] = 1

# Write to dictionary.txt
fo = open(os.path.join(dest_dir, "dictionary.txt"), "w")
fo_stop = open(os.path.join(dest_dir, "dictionary_stopwords.txt"), "w")
fo_stem = open(os.path.join(dest_dir, "dictionary_stemwords.txt"), "w")

# Load corpora and stemmer
stops = stopwords.words('english')
stems = PorterStemmer()

# Load the training set list
train_list = open(os.path.join(dest_dir, "training_set.txt"), "r")

# For each of the files
ctr = 0
size = 0
filename = ""
try:
    for filename in train_list:
        filename = filename.strip()
        msg = open(os.path.join(src_dir, filename), encoding='utf-8', errors='replace').read()

        # For each word in the string, check if English
        # Normal caps in the en_US, lowercase in our dictionary
        words = msg.split()
        for w in words:
            wl = w.lower()
            if bool(re.search(dc_digit, w)) or wl not in en_dict:
                continue

            w_stem = stems.stem(wl)

            # Writing the actual word in the original dictionary
            if wl not in mp_dict:
                mp_dict[wl] = 1
                size += 1
                fo.write(wl)
                fo.write('\n')

            # Stopwords-less dictionary
            if wl not in stop_dict and wl not in stops:
                stop_dict[wl] = 1
                fo_stop.write(wl)
                fo_stop.write('\n')

            # Stemwords dictionary
            if w_stem not in stem_dict:
                stem_dict[w_stem] = 1
                fo_stem.write(w_stem)
                fo_stem.write('\n')

        # Print how many have been preprocessed so far
        ctr += 1
        sys.stdout.write("\r{}/{}, {} words in dictionary".format(ctr, n, size))
        sys.stdout.flush()
except:
    e = sys.exc_info()[0]
    print("\nError at {}".format(filename))
    raise(e)

print('')

fo.close()
fo_stop.close()
fo_stem.close()
train_list.close()
