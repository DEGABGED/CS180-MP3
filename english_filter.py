import os
import sys
import re
import enchant

d = enchant.Dict("en_US")

# Define our dictionary
mp_dict = {}

n = 45252
dc_digit = re.compile('\d')

# Define directories
src_dir = os.path.join(os.getcwd(), "mp3data", "preprocessed", "training")
dest_dir = os.path.join(os.getcwd(), "mp3data")

# Load English dictionary
en_dict = {}
with open("words.txt") as f:
    for line in f:
        en_dict[line.strip().lower()] = 1

# Write to dictionary.txt
fo = open(os.path.join(dest_dir, "dictionary.txt"), "w")

# For each of the files
ctr = 0
size = 0
filename = ""
try:
    for f in range(n):
        filename = "inmail.{}".format(f+1)
        msg = open(os.path.join(src_dir, filename), encoding='utf-8', errors='replace').read()

        # For each word in the string, check if English
        # Normal caps in the en_US, lowercase in our dictionary
        words = msg.split()
        for w in words:
            wl = w.lower()
            if not bool(re.search(dc_digit, w)) and wl in en_dict and wl not in mp_dict:
                mp_dict[wl] = 1
                size += 1
                fo.write(wl)
                fo.write('\n')

        # Print how many have been preprocessed so far
        ctr += 1
        sys.stdout.write("\r{}/{}, {} words in dictionary".format(ctr, n, size))
        sys.stdout.flush()
except:
    e = sys.exc_info()[0]
    print("\nError at {}".format(filename))
    raise(e)

print('')
