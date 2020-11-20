#logistic Regression(로지스틱 회귀, 수치미분)

import os
import sys
from pathlib import Path
try:
    sys.path.append(os.path.join(Path(os.getcwd()).parent, 'lib'))
    from common import gradient_descent

except ImportError:
    print('Library Module Can Not Found')

import numpy as np
from matplotlib import pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def loss(x, data_training):
    data_in, data_out = data_training
    e = data_out * np.log(sigmoid(x[0] * data_in + x[1])) + (1-data_out) * np.log(1-sigmoid(x[0] * data_in + x[1]))
    return -1 * np.mean(e)

#data
times = np.array([2,4,6,8,10,12,14])
passed = np.array([0, 0, 0, 1, 1, 1, 1])

#경사하강법
params =gradient_descent(loss, np.array([0., 0.]), lr = 0.5, epoch = 50000, data_training = (times, passed))

#graph
fig, splt = plt.subplots()
splt.scatter(times, passed)
x = np.arange(0, 15, 0.1)
y = sigmoid(params[0] * x + params[1])
splt.plot(x, y)
plt.show()

#predict
x_p = 12
print(f'{x_p}시간 공부했을 때 합격할 확률은 {sigmoid(params[0] * x_p + params[1])}입니다')