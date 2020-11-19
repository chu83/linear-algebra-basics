#기울기(gradient)

import numpy as np

def f(x):
    return np.sum(x**2, axis = 0)

# s1 = f(np.array(10))
# s2 = f(np.array([3.,4.]))
# s3 = f(np.array([3,4,5]))
# print(s1)
# print(s2)
# print(s3)

#수치미분 기울기 구하기
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



#평균제곱오차(MSE, Mean Squares Error)
def mean_squares_error(x, data_tranining):
    data_x, data_y = data_tranining

    s = 0
    for i in range(len(data_x)):
        data_y_hat =x[0] * data_x[i] + x[1]
        s += ((data_y_hat - data_y[i]) ** 2 )
    e = s / len(data_x)
    # s =0
    # for i in range(len(data_x)):
    #     data_y_hat = x[0] * data_x[i] + x[1]
    #     s += ((data_y_hat - data_y[i] **2))
    # e = s / len(data_x)

    return e

#경사하강법 구현1
def gradient_descent(f, x, lr=0.01, epoch = 100):
    for i in range(epoch):
        gradient = numerical_gradient(f, x)
        #print
        print((f'epoch={i+1}, gradient = {gradient}, x = {x}'))
        x -= lr*gradient

    return x

#경사하강법 구현2 - 선형회귀
def gradient_descent_linear_regression(f, x, lr = 0.01, epoch = 100, data_training = None):
    for i in range(epoch):
        gradient = numerical_gradient_training(f, x, data_training)
        #출력
        print(f'epoch={i+1}, gradient={gradient}' )
        x -= lr * gradient

    return x


#수치미분
def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) -  f(x) )/h


#수치미분
def numerical_diff2(f, x0, x1):
    h = 1e-4
    dx0 = (f(x0+h, x1) - f(x0-h, x1) / (2*h))
    dx1 = (f(x0, x1+h) - f(x0, x1+h))(2*h)

    return (dx0, dx1)


# 수치미분
def numerical_diff3(f, x0, x1, x2):
    h = 1e-4
    dx0 = (f(x0 + h, x1, x2) - f(x0 - h, x1, x2) / (2 * h))
    dx1 = (f(x0, x1 + h, x2) - f(x0, x1 + h, x2) /(2 * h))
    dx2 = (f(x0, x1, x2+h) - f(x0, x1, x2-h)) / (2*h)
    return (dx0, dx1, x2)


# 수치미분 4(최종)
def numerical_partial_diff(f, x):
    pass
    """
    return 변수 x(벡터, 1차원 numpy array)에 대한 편미분 결과 반환(벡터, 1차원 numpy array)
    : param f: 손실함수
    : param x : 변수(벡터, 1차원 numpy array)
    """

    h = 1e-4
    dx = np.zeros_like(x)

    for i in range(x.size):
        tmp = x[i]

        x[i] = tmp + h
        h1 = f(x)

        x[i] = tmp - h
        h2 = f(x)

        dx[i] = (h1 - h2) / (2 * h)
        x[i] = tmp

    return dx

#수치편미분(변수가 3개 이상)
def numerical_partial_diff(f, x, data_training = None):
    pass
    """
    return 변수 x(벡터, 1차원 numpy array)에 대한 편미분 결과 반환(벡터, 1차원 numpy array)
    : param f: 손실함수
    : param x : 변수(벡터, 1차원 numpy array)
    """

    h = 1e-4
    dx = np.zeros_like(x)

    for i in range(x.size):
        tmp = x[i]

        x[i] = tmp + h
        if len(signature(f).parameters) ==1:
            ha = f(x)
        else:
            h1 = f(x, data_training)

        h1 = f(x)

        x[i] = tmp - h
        h2 = f(x)

        dx[i] = (h1 - h2) / (2 * h)
        x[i] = tmp

    return dx

# 기울기 구하기 = 수치편미분
numerical_gradient =numerical_partial_diff


#수치미분으로 기울기 구하기
def numerical_gradient_training(f, x, data_training):
    h = 1e-4
    gradient = np.zeros_like(x)

    for i in range(x.size):
        tmp = x[i]

        x[i] = tmp + h
        h1 = f(x, *data_training)
        x[i] = tmp - h
        h2 = f(x,*data_training)

        gradient[i] = (h1-h2) / (2*h)
        x[i] = tmp

    return gradient


#최소제곱법
#여러 점에서 직선의 기울기 구하기
def method_least_squares(x, y):
    mx = sum(x) / len(x)
    my = sum(y) / len(y)

    # case 1
    t = [(i - mx) * (j - my) for i, j in [(2, 81), (4, 93), (6, 91), (8, 97)]]

    # case 2
    s1 = 0
    for i in range(len(x)):
        s1 += (x[i] - mx) * (y[i] - my)

    s2 = 0
    for i in range(len(x)):
        s2 += (x[i] - mx) ** 2
    print(s1, s2)

    # case 3
    s1 = sum([(i - mx) * (j - my) for i, j in zip(x, y)])
    s2 = sum([(i - mx) ** 2 for i in x])
    print(s1, s2)

    mls_a = s1 / s2
    mls_b = my - (mx * mls_a)

    return mls_a, mls_b

