import torch
from torch import nn

def generate_model():
    model = nn.Sequential(
          nn.Linear(150,64),
          nn.ReLU(),
          nn.Linear(64,5),
          nn.ReLU()
        )
    return model
