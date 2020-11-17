# y = -log(1-x)

from matplotlib import pyplot as plt
import numpy as np

def f1(x):
    return -np.log(x)

def f2(x):
    return -np.log(1-x)

data_x1 = np.arang(0.01, 1.5,  0.01)
