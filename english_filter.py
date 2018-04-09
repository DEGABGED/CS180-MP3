import os
import sys
import re
import enchant

d = enchant.Dict("en_US")

# Define our dictionary
mp_dict = {}

n = 1000
dc_digit = re.compile('\d')

# Define directories
src_dir = os.path.join(os.getcwd(), "sample")
dest_dir = os.path.join(os.getcwd(), "pp2")

# Write to dictionary.txt
fo = open("dictionary.txt", "w")

# For each of the files
ctr = 0
size = 0
filename = ""
try:
    for f in os.listdir(src_dir):
        filename = f # For debugging
        msg = open(os.path.join(src_dir, f), encoding='utf-8', errors='replace').read()

        # For each word in the string, check if English
        # Normal caps in the en_US, lowercase in our dictionary
        words = msg.split()
        for w in words:
            wl = w.lower()
            if d.check(w) and not bool(re.search(dc_digit, w)) and wl not in mp_dict:
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
