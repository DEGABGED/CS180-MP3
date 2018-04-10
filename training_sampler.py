import os
import sys

# Create a .txt file containing the numbers of the emails to be used for the training set
total = 75419
n = 45252 # 60% of 75419

# Create the file in the mp3data/ folder
dest_dir = os.path.join(os.getcwd(), "mp3data")

# Write to training_set.txt
training_set = open(os.path.join(dest_dir, "training_set.txt"), "w")
test_set = open(os.path.join(dest_dir, "test_set.txt"), "w")

# For each of the sampled numbers (in this case its only by order)
for i in range(total):
    if i < n:
        training_set.write("inmail.{}\n".format(i+1))
    else:
        test_set.write("inmail.{}\n".format(i+1))

training_set.close()
test_set.close()
