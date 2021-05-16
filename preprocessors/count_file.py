from matplotlib import pyplot as plt
import pandas as pd
import os
import numpy as np

def find_all_events():
	dirs = ['./'+i+'/' for i in os.listdir() if '.' not in i and '__' not in i]
	return dirs

def counter(path):
	files = os.listdir(path)
	data = None
	for file in files:
		df = pd.read_csv(path+file)
		df = df.values
		if data is None:
			data = df
		else:
			data = np.concatenate((data, df), axis=0)
	values, counts = np.unique(data.T[-1], return_counts=True)
	print(values, counts)

if __name__ == '__main__':
	dirs = find_all_events()
	for dir_t in dirs:
		counter(dir_t)