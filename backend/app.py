from flask import Flask, request, jsonify
from GloVe_helper import get_embed
import pandas as pd
app = Flask(__name__)
import numpy as np
from model_trainer import train
from model_helper import get_weights_from_json, asynchronous_update

WORD_LIMIT = 10

@app.route('/', methods=['GET', 'POST'])
def index():
	return "Hello World"

@app.route('/make_tweet', methods=['POST'])
def save_data():
	data = request.get_json()
	embed = get_embed(data['post_content'])
	data.update({"embedding"+str(idx):embed[idx] for idx in range(len(embed))})
	data = {key: [value] for key, value in data.items()}
	df = pd.DataFrame(data)
	if os.path.isfile('posts.csv'):
		df.to_csv('posts.csv', index=False, mode='a', header=False)
	else:
		df.to_csv('posts.csv', index=False, mode='a', header=True)
	return jsonify({})

@app.route('/train_model', methods=['POST'])
def train_model():
  hyperparameters = request.get_json()
  score = train(epochs=hyperparameters['epochs'])
  return jsonify({'score': score})

@app.route('/volunteer', moethods=['POST'])
def get_volunteer_model():
	mm = ModelManager()
	model = request.get_json()
	weights = mm.get_weights_from_json(model)
	mm.asynchronous_update(weights)
	return jsonify({})
	
