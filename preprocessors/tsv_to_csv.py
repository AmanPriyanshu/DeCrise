import os
import pandas as pd
import numpy as np
from tqdm import tqdm

def find_all_events():
	dirs = ['./'+i+'/' for i in os.listdir() if '.' not in i]
	return dirs

def convert_tsv_to_csv(path):
	files = os.listdir(path)
	for file in files:
		df = pd.read_csv(path+file, delimiter='\t')
		df.to_csv(path+file.replace('.tsv', '.csv'), index=False)

if __name__ == '__main__':
	dirs = find_all_events()
	for dir_t in tqdm(dirs):
		convert_tsv_to_csv(dir_t)
