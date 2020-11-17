#matrix(Tensor 2) 확인
""""
1. 행렬은 두 개의 축을 가지며 2차원(Tensor 2)
2. 수평 방향을 행(row), 수직방향을 열(colum)
"""
import numpy as np

m = np.array([[50,10,80],
              [50,11,88]])
print(m.ndim, m.shape)
print(m)
