"""
1. 2차원 배열, 행렬의 축 기준 연산(합
2. 축이 두개이기 때문에 축 지정 유무에 따라 그 결과 다름

"""
import numpy as np

m = np.array([[10, 20],
             [1,2]])

print(m)
print(np.sum(m))

print(np.sum(m, axis=0))    #수직
print(np.sum(m, axis=1))    #수평

s1 = np.sum(m)
print(s1, type(s1))
s2 = np.sum(m, axis=0)
print(s2, type(s2))
s3 = np.sum(m, axis = 1)
print(s3, type(s3))