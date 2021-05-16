import torch
import numpy as np

def get_weights(self, dtype=np.float32):
		precision = self.precision
		weights = []
		for layer in self.model:
			try:
				weights.append([np.around(layer.weight.detach().numpy().astype(dtype), decimals=precision), np.around(layer.bias.detach().numpy().astype(dtype), decimals=precision)])
			except:
				continue
		return np.array(weights)
  
def set_weights(self, weights):
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
