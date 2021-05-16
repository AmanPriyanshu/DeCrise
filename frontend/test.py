import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer
import pandas as pd
import numpy as np
from helper import convert_sentences, preprocessor, open_csv
from sklearn.ensemble import RandomForestClassifier

'''
Health and Accuracy checks
'''

labels = ['displaced_people_and_evacuations', 'infrastructure_and_utility_damage', 'injured_or_dead_people', 'missing_or_found_people', 'not_humanitarian']

def test(df):
	x = df.values
	x = x.flatten()
	x = convert_sentences(x)

	with open('./frontend/text_classifier.pk', 'rb') as f:
		clf = pickle.load(f)

	y = clf.predict(x)
	y = [labels[i] for i in y]

	x = df.values
	x = x.flatten()

	data = pd.DataFrame({'x': x, 'y': y})
	return data

if __name__ == '__main__':
	df = pd.read_csv('data.csv')
	df = df.values
	df = df.T[0]
	df = pd.DataFrame({'x': df})
	df = test(df)
	df.to_csv('lol.csv', index=False)
