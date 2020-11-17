# 이차방정식
from matplotlib import pyplot as plt
import numpy as np

def f(x):
    return 5 * x**2

data_x =np.arange(-10, 10, 0.1)
data_y = f(data_x)


fig, splt = plt.subplots()
plt.axvline(x = 0, color = 'red')
plt.axhline(y = 0, color = 'red')
splt.plot(data_x, data_y)

splt.set_xticks([-10, -5, 0, 5, 10])
splt.set_yticks([-100, -50, 0, 50, 100])
plt.show()