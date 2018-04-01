import sys
import os
import shutil
import random

n = int(sys.argv[1])
files = random.sample(range(1,75419), n)
dest = os.path.join(os.getcwd(), "sample/")

for i in files:
  filename = os.path.join(os.getcwd(), "trec07p", "data", "inmail.{}".format(i))
  print(filename)
  shutil.copy(filename, dest)
