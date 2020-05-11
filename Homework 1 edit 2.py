
# coding: utf-8

# LINEAR REGRESSION

# In[1]:


X = [7, 2, 6, 4, 14, 16, 12, 14, 20, 15, 7]


# In[2]:


mis_val = sum(X)/len(X)


# In[3]:


X = [7, 2, 6, 4, 14, mis_val, 16, 12, 14, 20, 15, 7]
Y = [0.15, 0.10, 0.13, 0.15, 0.25, 0.27, 0.24, 0.20, 0.27, 0.44, 0.34, 0.17]


# In[4]:


sigma_x_2 = 0
sigma_y_2 = 0
sigma_xy = 0


# In[5]:


for i in range(len(X)):
    sigma_x_2 = sigma_x_2 + (X[i]**2)
    sigma_y_2 = sigma_y_2 + (Y[i]**2)
    sigma_xy = sigma_xy + (X[i]*Y[i])


# In[6]:


b = ((len(X)*(sigma_xy)) - (sum(X)*sum(Y))) / ((len(X)*(sigma_x_2)) - ((sum(X))**2))
mean_Y = sum(Y)/len(Y)
mean_X = sum(X)/len(Y)
a = mean_Y - (b*mean_X)


# In[7]:


y = a + (b*10)


# In[8]:


y


# In[9]:


a


# In[10]:


b

