import pandas as pd
import numpy as np
import os
from tqdm import tqdm

important_labels = ['displaced_people_and_evacuations', 'infrastructure_and_utility_damage', 'injured_or_dead_people', 'missing_or_found_people', 'not_humanitarian']

def find_all_events():
	dirs = ['./'+i+'/' for i in os.listdir() if '.' not in i]
	return dirs

def convert_tsv_to_csv(path):
	files = os.listdir(path)
	for file in files:
		df = pd.read_csv(path+file)
		features = df.columns
		df = df.values
		indexes = np.argwhere(np.any(np.stack([df.T[-1]==important_labels[i] for i in range(len(important_labels))]), axis=0)).flatten()
		df = df[indexes]
		df = pd.DataFrame(df)
		df.columns = features
		df.to_csv(path+file, index=False)
		
if __name__ == '__main__':
	dirs = find_all_events()
	for dir_t in tqdm(dirs):
		convert_tsv_to_csv(dir_t)