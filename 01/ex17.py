#행렬과 스칼라 사칙연산

import numpy as np
m1 = np.array([
    [10,20,30],
    [40,50,90]
])

#스칼라는 2차원 행렬로 변환한 후, 사칙연산
m2 = m1 + 10
print(m2)

m3 = m1 - 10
print(m3)

m4 = m1 * 10
print(m4)

m5 = m1 /10
print(m5)

#add(), subtract(), multiply(), divide()

m6 = np.add(m1, 10)
print(m6)

m7 = np.subtract(m1, 10)
print(m7)

m8 = np.multiply(m1, 10)
print(m8)

m9 = np.divide(m1, 10)
print(m9)







