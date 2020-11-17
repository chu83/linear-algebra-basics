#행렬과 벡터 @연산

import numpy as np

m1 = np.array([
    [1,2],
    [3,4],
    [5,6]
])

m2 = np.array([
    [1,2,3],
    [4,5,6]
])

v = np.array([10,100])
print(v)

#벡터와의 @연산
#행렬의 크기가 열의 크기와 같아야한다.
m3 = m1 @ v
print(m3, m3.shape)

#행렬의 크기가 행렬의 행의 크기와 같아야한다
m4 = v @ m2
print(m4, m4.shape)