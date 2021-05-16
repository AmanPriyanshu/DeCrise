import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer
import pandas as pd

def preprocessor(X):
	stemmer = WordNetLemmatizer()
	documents = []
	for sen in trange(0, len(X)):
		document = re.sub(r'\W', ' ', str(X[sen]))
		document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
		document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
		document = re.sub(r'\s+', ' ', document, flags=re.I)
		document = re.sub(r'^b\s+', '', document)
		document = document.lower()
		document = document.split()
		document = [stemmer.lemmatize(word) for word in document]
		document = ' '.join(document)
		documents.append(document)
	return documents

def get_tfidf(path='vectorizer.pk'):
    with open(path, 'rb') as f:
        tfidfconverter = pickle.load(f)
    return tfidfconverter

def convert_sentences(x):
	tfidfconverter = get_tfidf()
	return tfidfconverter.transform(x).toarray()

def open_csv(path='data.csv'):
	df = pd.read_csv(path)
	df = df.values
	return df.T[0], df.T[1]