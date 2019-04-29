import numpy as np

"""
以0为边界对数组进行切分，剔除0
"""
a = np.array([0, 1, 1, 0, 1, 3, 6, 3, 0, 1])
pos = np.where(a > 0)[0]
split = np.where(np.diff(pos) != 1)[0] + 1
print(np.split(a[pos], split))
"""
>>> [[1, 1], [1, 3, 6, 3], [1]]
"""

"""
以0为边界对数组进行切分，不剔除0
"""
a = np.array([0, 0, 0, 1, 3, 4, 0, 1, 3, 4, 0])
b = np.where(np.diff(a != 0))[0] + 1
print(b)
print(np.split(a, b))
"""
>>> [[0, 0, 0], [1, 3, 4], [0], [1, 3, 4], [0]]
"""