import os
import sys

# Create a .txt file containing the numbers of the emails to be used for the training set
total = 75419
n = 45252 # 60% of 75419

# Create the file in the mp3data/ folder
dest_dir = os.path.join(os.getcwd(), "mp3data")

# Write to training_set.txt
#training_set = open(os.path.join(dest_dir, "training_set.txt"), "w")
#test_set = open(os.path.join(dest_dir, "test_set.txt"), "w")
training_labels = open(os.path.join(dest_dir, "training_labels.txt"), "w")
test_labels = open(os.path.join(dest_dir, "test_labels.txt"), "w")
full_set = open(os.path.join(os.getcwd(), "trec07p", "full", "index"), "r")

# For each of the sampled numbers (in this case its only by order)
for i in range(total):
    hamspam = full_set.readline().split()[0]
    if i < n:
        #training_set.write("inmail.{}\n".format(i+1))
        training_labels.write(hamspam + '\n')
    else:
        #test_set.write("inmail.{}\n".format(i+1))
        test_labels.write(hamspam + '\n')

training_labels.close()
test_labels.close()
full_set.close()
