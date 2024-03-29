#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

arr1=np.array([1,2,3,4,5,6])
arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)
print(arr2)
print(arr1.ndim)
print(arr2.ndim)
print(arr1.dtype)
print(arr1.size)
print(arr1.shape)
print(arr2.shape)
print(arr1.itemsize)
arr3=np.array([[1,2,3],[4,5,6]])
print(arr3.shape)
arr4=np.zeros(5)
print(arr4)
arr5=np.zeros((2,2))
print(arr5)
arr6=np.ones(3)
print(arr6)
arr7=np.eye(3)
print(arr7)
arr8=np.random.rand(4)
print(arr8)
arr9=np.random.rand(3,3)
print(arr9)
arr10=np.random.randint(10,211,6)
print(arr10)
arr11=np.full([3,4],0.11)
print(arr11)
arr12=np.arange(0,30,5)
print(arr12)
arr13=np.arange(1,10)
print(arr13)
arr14=np.arange(1,10).reshape(3,3)
print(arr14)
arr15=np.linspace(1,3,10)
print(arr15)
arr16=arr13.reshape(3,3)
print(arr16)
arr17=np.array([1,2,3,4,5,6,7])
print(arr17[5])
print(arr17[1:3])
print(arr17[-1:3])
print(arr17.max())
print(arr17.min())
print(arr17.argmax())
print(arr17.argmin())
print(arr17.sum())
print(arr2.sum(axis=0))
print(arr2.sum(axis=1))
print(arr2.cumsum(axis=0))
print(arr2.cumsum(axis=1))
print(arr2[1:-1,1:-1])


# In[ ]:




