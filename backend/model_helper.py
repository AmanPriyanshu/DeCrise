import torch
import numpy as np
from model_generator import generate_model

class ModelManager:
	def __init__(self, model_path='./models/model.pt'):
		self.model = generate_model()
		self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
		self.model.load_state_dict(torch.load(model_path, map_location=self.device))

	def get_weights_from_json(self, dtype=np.float32):
		weights = []
		for layer in self.model:
			try:
				weights.append([np.around(layer.weight.detach().numpy().astype(dtype)), np.around(layer.bias.detach().numpy().astype(dtype))])
			except:
				continue
		return np.array(weights)
  
	def asynchronous_update(self, weights):
		index = 0
		for layer_no, layer in enumerate(self.model):
			try:
				_ = self.model[layer_no].weight
				self.model[layer_no].weight = torch.nn.Parameter(weights[index][0])
				self.model[layer_no].bias = torch.nn.Parameter(weights[index][1])
				index += 1
			except:
				continue
        
	def average_weights(self, all_weights):
		all_weights = np.array(all_weights)
		all_weights = np.mean(all_weights, axis=0)
		all_weights = [[torch.from_numpy(i[0].astype(np.float32)), torch.from_numpy(i[1].astype(np.float32))] for i in all_weights]
		return all_weights
