#dot(@)연산

import numpy as np

m1 = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
]
)

print(m1)

m2 = np.array([
    [1,2,3,4],
    [5,6,7,8]
])

# (3*2) @(2*4) -->(3*4)
m3 = np.dot(m1, m2)
print(m3)
print(m3.shape)

# 연산자 @사용
m4 = m1@m2
print(m4)
print(m4.shape)