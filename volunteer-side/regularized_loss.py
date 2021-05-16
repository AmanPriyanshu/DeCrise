import copy
import torch
from torch import nn

def continual_learning_loss(output, target, model):
  base_criterion = nn.CrossEntropyLoss()
  base_loss = criterion(output, target)
  
  loss = base_loss
  
  model_copy = copy.deepcopy(model)
  model_copy.backward()
  
  for param, param_new in zip(model.parameters(), model_copy.parameters()):
    loss += torch.norm(torch.abs(param - param_new))
  
  return loss
