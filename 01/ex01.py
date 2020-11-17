#scalar 확인
"""
1. 스칼라는 차원을 확인하면 0 (Tensor 0)
2. 형상을 확인하면 빈 튜플

"""

import numpy as np

s=np.array(50)
print(s.ndim, s.shape, s.dtype)