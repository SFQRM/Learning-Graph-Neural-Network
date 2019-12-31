"""
稀疏矩阵
常用的稀疏矩阵存储格式有CSR。
CSR的存储策略：
    需要三类数据来表达：数值，列号，以及行偏移。
    第一个数组：数值，非零元素的数值；
    第二个数组：列号，非零元所在的列序号；
    第三个数组：行偏移，共有rows+1个元素，每一个元素表示某一行的第一个元素在values里面的起始偏移位置。
scipy.sparse：
    scipy.sparse定义了七种稀疏矩阵以及基矩阵，还有稀疏矩阵的各种函数。
    scipy.sparse 官方文档：https://docs.scipy.org/doc/scipy/reference/sparse.html
    格式：csr_matrix((data, indices, indptr), [shape=(M, N)])
"""

import numpy as np
from scipy.sparse import csr_matrix

data = np.array([1, 7, 2, 8, 5, 3, 9, 6, 4])
indices = np.array([0, 1, 1, 2, 0, 2, 3, 1, 3])
indptr = np.array([0, 2, 4, 7, 9])

A = csr_matrix((data, indices, indptr), shape=(4, 4)).toarray()

print(A)

"""
Output:
    [[1 7 0 0]
    [0 2 8 0]
    [5 0 3 9]
    [0 6 0 4]]
"""
