# 作者：Alex
# 2024/10/14 06:23
import numpy as np


a = np.array([[1,2,3],[4,5,6],[7,8,8]])
print(a)
b = np.reshape(np.arange(2,14,1,dtype=np.int32),(3,4))
print(b)

print(np.ones((4,4),np.int16))
print(np.zeros((4,4),"i4"))
print(np.empty((2,4),"i4"))
print(np.full((5,3),7,np.int16))
print(np.full(3,4))
print(np.eye(4))
print(np.eye(5,4))
c = np.eye(5,4,-1)
print(c)
print(f'维度\t\t形状\t\t元素总个数\t每个元素的大小\t')
print(f'{c.ndim}\t\t{c.shape}\t\t{c.size}\t\t\t{c.itemsize}')
print(c.T)
for item in c.tolist():
    for i in item:
        print(int(i),end=' ')
print(' '.join(str(int(i)) for item in c.tolist() for i in item))
print(a[1,-2])
print(a[:,0:-1:2]) #array[start:stop:step]

d = a.reshape(9)
print(d)
e= np.array([[1,2],[0,1]])
f = (d[e])
print(f)
g = np.array([[1,2],[1,2]])
h = a[e,g]
print(h)
i = e @ g
i2 = np.dot(e,g)
print(i)
print(i2)
for n in np.nditer(a):
    print(n, end=' ')
print(f'\n','-'*50)
a2 = np.zeros((10,10))
a2[0,:],a2[:,-1],a2[:,0],a2[-1,:] = 1,1,1,1
for i in range(10):
    for j in range(10):
        if i == 0 or i == 9 or j== 0 or j ==9:
            a2[i,j] = 1
a2[::2,1::2] = 1
print(a2)