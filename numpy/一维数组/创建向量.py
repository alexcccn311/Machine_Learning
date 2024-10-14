# 作者：Alex
# 2024/10/13 19:23
import numpy as np
a = np.array([1,2,3],dtype=np.uint32)
c = np.array(('-4','5','312'),dtype=np.int16)
print(a)
print(c)
print(type(a))
print(type(c))
print(a.dtype)
print(c[0].dtype)

print('-'*50)

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(type(b))
print(b.dtype)

print('-'*50)

d = c.astype(np.int32)
print(d)
print(type(d))
print(d.dtype)

e = np.arange(2,14,1,dtype=np.int32)
print(e)
f = np.reshape(e,(3,4))
print(f)

g= np.linspace(1,51,50,endpoint=False,retstep=True,dtype=np.int32)
print(g)

h = np.logspace(1,10,10,endpoint=True,base = 2,dtype=np.int16)
print(h)

print(np.ones((4,),np.int16))
print(np.zeros((4,),"i4"))
print(np.empty((2,),"i4"))
print(np.full((2,),7,np.int16))
print(np.eye(1,4))
print(a[1])
print(a[0:3])