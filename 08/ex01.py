#기울기(gradient)

import numpy as np

def f(x):

    return np.sum(x**2, axis = 0)

s1 = f(np.array(10))
s2 = f(np.array([3.,4.]))
s3 = f(np.array([3,4,5]))
print(s1)
print(s2)
print(s3)


def numerical_gradient(f, x):
    h = 1e-4
    gradient = np.zeros_like(x)
    #x = [3, 4]
    # h1 = f(np.array([x[0]+h], x[1))
    # h2 = f(np.array([x[0]-h], x[1]))
    # gradient[0] = (h1-h2) / (2*h)
    #
    # h1 = f(np.array([x[0], x[1]+h]))
    # h2 = f(np.array([x[0], x1[1]-h]))
    # gradient[1] = (h1 - h2) / (2 * h)

    for i in range(x.size):
        tmp = x[i]
        x[i] = x[i] + h
        h1 = f(x)


        x[i] = tmp - h
        h2 = f(x)

        gradient[i] = (h1-h2) / (2*h)
        x[i] = tmp

    return gradient
#함수 테스트
#print(f(np.array([3, 4])))

gra1 = numerical_gradient(f, np.array(f, np.array[3., 4.]))
gra2 = numerical_gradient(f, np.array(f, np.array[0., 2.]))
gra3 = numerical_gradient(f, np.array(f, np.array[3., 0.]))







