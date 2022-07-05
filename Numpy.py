#!/usr/bin/env python
# coding: utf-8

# NUMPY

# In[1]:


import numpy as np


# In[2]:


mylist = [1,2,3]
type(mylist)


# In[3]:


np.array (mylist)


# In[4]:


type(mylist)


# In[5]:


arr = np.array (mylist)


# In[6]:


print(arr)


# In[7]:


type(arr)


# In[8]:


mylist = [[1,2,3],[4,5,6],[7,8,9]]
##Dimension of the array can be checked by the number of square brackets
np.array(mylist)


# In[9]:


mymatrix = np.array(mylist)


# In[10]:


mymatrix.shape


# In[11]:


mymatrix.ndim


# In[12]:


mynewmatrix = np.array(mylist)


# In[13]:


np.arange(0,11,2)


# In[14]:


np.zeros(5)


# In[15]:


type(0.0)


# In[16]:


np.zeros((4,10))


# In[17]:


np.ones((5,5)) + 4


# In[18]:


np.ones(4) * 100


# In[19]:


#This operation cant be done with the help of a list
[1,1,1,1] + 10


# In[20]:


np.ones(4) / 100


# In[21]:


#Gives 100 numbers linearly spaced within the range of inclusive 0 and 100
np.linspace(0,10,100)


# In[22]:


len(np.linspace(0,10,11))


# In[23]:


#Identity matrix
np.eye(5)


# In[24]:


np.random.rand(1)


# In[25]:


np.random.rand(5,5)


# In[26]:


np.random.randn(1)


# In[27]:


np.random.randn(10)


# In[28]:


np.random.randint(1,100,10)


# In[29]:


np.random.seed(42)
np.random.rand(4)


# In[30]:


np.random.seed(555)
np.random.rand(4)


# In[31]:


arr = np.arange(25)


# In[32]:


arr


# In[33]:


ranarr = np.random.randint(0,50,10)


# In[34]:


ranarr


# In[35]:


arr.shape


# In[36]:


arr.reshape(5,5)


# In[37]:


ranarr.max(
)


# In[38]:


ranarr.min ()


# In[39]:


ranarr


# In[40]:


ranarr.argmax()


# In[41]:


ranarr.argmin ()


# In[42]:


ranarr.dtype


# INDEXING AND SELECTION

# In[43]:


arr = np.arange(0,11)


# In[44]:


arr


# In[45]:


arr [9]


# In[46]:


arr [1:5]


# In[47]:


arr [0:5]


# In[48]:


arr[5:]


# In[49]:


arr + 100


# In[50]:


new_arr = arr / 2


# In[51]:


new_arr


# In[52]:


arr


# In[53]:


arr ** 2


# In[54]:


slice_of_arr = arr[0:6]


# In[55]:


slice_of_arr


# In[56]:


slice_of_arr[:] = 99


# In[57]:


slice_of_arr


# In[58]:


arr


# In[59]:


arr_copy = arr.copy()


# In[60]:


arr_copy[:] = 1000


# In[61]:


arr_copy


# In[62]:


arr


# In[63]:


#indexing on 2d array
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])


# In[64]:


arr_2d


# In[65]:


arr_2d. shape


# In[66]:


arr_2d [1]


# In[67]:


arr_2d [1] [1]


# In[68]:


arr_2d[1,1]


# In[69]:


arr_2d [2,2]


# In[70]:


arr_2d[:2]


# In[71]:


arr_2d[:2,1:]


# In[72]:


arr = np.arange(1,11)


# In[73]:


arr


# In[74]:


arr > 4


# In[75]:


arr [arr > 4]


# In[76]:


bool_arr = arr > 4


# In[77]:


bool_arr


# In[78]:


arr [bool_arr] 


# In[79]:


arr [arr > 4]


# In[80]:


arr [arr <= 6]


# NUMPY OPERATIONS

# In[81]:


arr = np.arange(0,10)


# In[82]:


arr


# In[83]:


arr + 100


# In[84]:


arr / 100


# In[85]:


arr ** 2


# In[86]:


(arr + 2) / 100


# In[87]:


arr


# In[88]:


arr + arr


# In[89]:


1/arr


# In[90]:


arr/arr


# In[91]:


np.sqrt (arr)


# In[92]:


np.log(arr)


# In[93]:


np.sin(arr)


# In[94]:


np.cos(arr)


# In[95]:


np.tan(arr)


# In[96]:


arr.sum()


# In[97]:


arr.mean()


# In[98]:


arr.max()


# In[99]:


arr.min()


# In[100]:


arr_2d = np.array ([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


# In[101]:


arr_2d


# In[102]:


arr_2d.shape


# In[103]:


arr_2d.sum(
)


# In[104]:


#Give me the sum across the Rows
arr_2d.sum(axis = 0)
#Sum of the all the values in the columns


# In[105]:


#Sum of all the values of the Rows
arr_2d.sum (axis = 1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




