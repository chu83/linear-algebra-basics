#대각행렬(diagnal Matrix)

import numpy as np
v = np.arange(1, 4)
m = np.diag(v)

# diag() 함수에 대각행렬의 주대각선의 요소를 벡터로 전달하면
# 주대각선 요소를 제외한 나머지 요소를 0으로 채운 대각행렬
print(v)
print(m)

m = np.diag(v, k=1)
print(m)
m = np.diag(v, k=-2)
print(m)