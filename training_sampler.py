import os
import sys

# Create a .txt file containing the numbers of the emails to be used for the training set
n = 45252 # 60% of 75419

# Create the file in the mp3data/ folder
dest_dir = os.path.join(os.getcwd(), "mp3data")

# Write to training_set.txt
fo = open(os.path.join(dest_dir, "training_set.txt"), "w")

# For each of the sampled numbers (in this case its only by order)
for i in range(n):
    fo.write("inmail.{}\n".format(i+1))

fo.close()
