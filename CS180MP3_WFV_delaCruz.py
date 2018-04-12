import preprocessor
import training_sampler
import english_filter
import feature_vector
import naive_bayes

import os

print("START")
message = '''
1 - Preprocess emails
2 - Generate training and test set lists
3 - Generate dictionaries
4 - Generate feature vectors (with CSV)
5 - Generate feature vectors (no CSV)
6 - Run models
7 - Do all (with CSV)
8 - Do all (no CSV)
else - Do nothing
'''

choice = int(input(message))

# Define directories
raw_data_dir = os.path.join(os.getcwd(), "trec07p", "data")
output_data_dir = os.path.join(os.getcwd(), "mp3data")
preprocessed_dir = os.path.join(os.getcwd(), "mp3data", "preprocessed")

# Run each file
if choice in [1,7,8]:
    print("### PREPROCESSING EMAILS ###")
	preprocessor.preprocess(raw_data_dir, output_data_dir)
    print("########### DONE ###########")

if choice in [2,7,8]:
	training_sampler.gen_partitioning(output_data_dir)

if choice in [3,7,8]:
	english_filter.gen_dictionary(preprocessed_dir, output_data_dir)

if choice in [4,5,7,8]:
	csv = choice in [4,7]
	print("### FEATURE VECTORS ###")
	print("Original")
	feature_vector.gen_feature_matrix(output_data_dir,
									  preprocessed_dir,
									  gen_csv=csv)

	print("Stemwords")
	feature_vector.gen_feature_matrix(output_data_dir,
									  preprocessed_dir,
									  dictionary="-stemwords",
									  gen_csv=csv)

	print("Stopwords")
	feature_vector.gen_feature_matrix(output_data_dir,
									  preprocessed_dir,
									  dictionary="-stopwords",
									  gen_csv=csv)
	print("######## DONE #########")

# Fit into the NBs
print("Running original models")
berno_orig = naive_bayes.naive_bayes(output_data_dir, model="b")
multi_orig = naive_bayes.naive_bayes(output_data_dir)
print(berno_orig)
print(multi_orig)

print("Running lambda smoothings")
multi_l1 = naive_bayes.naive_bayes(output_data_dir, alpha=0.01)
multi_l2 = naive_bayes.naive_bayes(output_data_dir, alpha=0.1)
multi_l3 = naive_bayes.naive_bayes(output_data_dir, alpha=0.2)
multi_l4 = naive_bayes.naive_bayes(output_data_dir, alpha=0.5)
multi_l5 = naive_bayes.naive_bayes(output_data_dir, alpha=1)
print(multi_l1)
print(multi_l2)
print(multi_l3)
print(multi_l4)
print(multi_l5)

print("Running stopwords dictionary")
berno_stop = naive_bayes.naive_bayes(output_data_dir, model="b", fv="-stopwords")
multi_stop = naive_bayes.naive_bayes(output_data_dir, fv="-stopwords")
print(berno_stop)
print(multi_stop)

print("Running stemwords dictionary")
berno_stem = naive_bayes.naive_bayes(output_data_dir, model="b", fv="-stemwords")
multi_stem = naive_bayes.naive_bayes(output_data_dir, fv="-stemwords")
print(berno_stem)
print(multi_stem)