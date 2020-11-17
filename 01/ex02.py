#vector(Tensor 1) 확인
"""
1. 1차원배열(Tensor 1) 인 벡터는 차원과 형상을 가진다.
2. 차원은 1이며, 형상은 1개 요소를 가지고 있는 튜플이다.
"""

import numpy as np

s=np.array([50, 10, 80])
print(s.ndim, s.shape)