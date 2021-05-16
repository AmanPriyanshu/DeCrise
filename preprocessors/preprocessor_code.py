import pandas as pd
import numpy as np
import preprocessor as p
import os

def find_all_events():
	dirs = ['./'+i+'/' for i in os.listdir() if '.' not in i and '__' not in i and 'cleaned' not in i]
	return dirs

def cleaner(path):
	files = os.listdir(path)
	for file in files:
		df = pd.read_csv(path+file)
		features = df.columns
		df = df.values
		df.T[1] = np.array([p.clean(i.lower()) for i in df.T[1]])
		df = pd.DataFrame(df)
		df.columns = features
		df.to_csv(path.replace('./', './cleaned_data/')+file, index=False)

if __name__ == '__main__':
	dirs = find_all_events()
	for dir_t in dirs:
		cleaner(dir_t)