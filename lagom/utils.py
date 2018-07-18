import torch
import numpy as np
import random


def set_global_seeds(seed):
    """
    Set seed for all dependencies we use. 
    
    It includes the following:
    1. PyTorch
    2. Numpy
    3. Python random
    
    Args:
        seed (int): seed
    """
    
    torch.manual_seed(seed)
    np.random.seed(seed)
    random.seed(seed)
