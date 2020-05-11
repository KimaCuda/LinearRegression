
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import math
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


# In[2]:


dataset = pd.read_csv('hw1data.csv')


# In[3]:


dataset_X_train = dataset.iloc[:-1,1]
dataset_X_test = np.array(dataset.iloc[-1:,1]).reshape(-1,1)
dataset_Y_train = np.array(dataset.iloc[:-1,2])
dataset_Y_test = np.array(dataset.iloc[-1:,2])


# In[4]:


dataset_X_train.replace(np.nan, np.nanmean(dataset_X_train), inplace=True)


# In[5]:


dataset_X_train = np.array(dataset.iloc[:-1,1])
dataset_X_train = dataset_X_train.reshape(-1,1)


# In[6]:


linreg = linear_model.LinearRegression()


# In[7]:


linreg.fit(dataset_X_train, dataset_Y_train)


# In[8]:


dataset_Y_pred = linreg.predict(dataset_X_test)


# In[9]:


#Creating linear regression line
xfit = np.linspace(0, 25, 50)
yfit = linreg.predict(xfit[:, np.newaxis])


# In[14]:


#plotting the graph
plt.scatter(dataset_X_train, dataset_Y_train, color='red')
plt.plot(xfit, yfit, color='blue', linewidth=3)
plt.xlabel('Revenue (m)')
plt.ylabel('Profit (m)')
plt.title('Revenue vs Profit linear regression model')


# In[11]:


dataset_Y_pred

