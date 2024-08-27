import numpy as np
""""a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype)
print(a.itemsize)
print(a.nbytes)
print(type(a))
b= np.array((4,5,6))
print(b)
print(type(b))

一维数组：[1, 2, 1] 是一个一维数组，有一个轴，轴的长度为3。这个轴上有3个元素，分别是1、2和1。
二维数组：[[1, 2, 3], [4, 5, 6]] 是一个二维数组，有两个轴。第一个轴有2个元素（对应于2行），第二个轴有3个元素（对应于3列）。
进一步解释
轴（Axis）：在NumPy中，轴是描述数组结构的概念。每个维度对应一个轴。

一维数组：只有一个轴，对应于一个长度。
二维数组：有两个轴，分别对应于行和列。
三维数组：有三个轴，比如可以想象为多层矩阵的堆叠。
长度（Length）：轴的长度是指在这个轴上有多少个元素。

对于一维数组，长度就是数组的元素数量。
对于二维数组，每个轴的长度对应于行数或列数。
"""

a = np.array([2, 3, 4])
print(a)
