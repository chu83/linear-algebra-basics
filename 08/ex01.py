#기울기(gradient)
import os
import sys
from pathlib import Path
import numpy as np

try:
    #print(os.getcwd())
    #sys.path.append('F:\deep-learning\dowork\PycharmProjects\linear-algebra-basics\lib')
    #p1 = Path(os.getcwd()).parent + '\\lib'
    #p2 = os.path.join(Path(os.getcwd()).parent, 'lib')
    #print(p2)
    #sys.path.append(p2)

    sys.path.append(os.path.join(Path(os.getcwd()).parent, 'lib'))

    #import common as cm
    from common import numerical_gradient

except ImportError:
    print('Library Module Can Not Found')


def f(x):
    return np.sum(x**2, axis = 0)

#함수테스트


gra1 = numerical_gradient(f, np.array([3., 4.]))
gra2 = numerical_gradient(f, np.array([0., 2.]))
gra3 = numerical_gradient(f, np.array([3., 0.]))


print(gra1, gra2, gra3)
