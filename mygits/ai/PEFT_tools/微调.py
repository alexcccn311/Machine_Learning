import torch
from functions import get_loader, get_model

device = 'cuda' if torch.cuda.is_available() else 'cpu'
_, _, loader = get_loader()
model, _, _ = get_model()
