import numpy as np  
from ..settings import temp

# print statement before func_one
print('hello world 1')

def func_one():
    """
    Docstring for func_one.
    """
    print('function 01')
    print(temp)
    return np.sqrt(4)
