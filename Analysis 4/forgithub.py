#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


customers = pd.read_csv("Ecommerce Customers")


# In[3]:


customers.head()


# In[5]:


customers.describe()


# In[7]:


customers.info()


# In[8]:


sns.jointplot(x='Time on Website',y='Yearly Amount Spent',data=customers)


# In[9]:


sns.jointplot(x='Time on App',y='Yearly Amount Spent',data=customers)


# In[10]:


sns.jointplot(x='Time on App',y='Length of Membership',kind='hex',data=customers)


# In[14]:


sns.pairplot(customers)


# In[15]:


sns.lmplot(x='Length of Membership',y='Yearly Amount Spent',data=customers)


# In[16]:


y = customers['Yearly Amount Spent']


# In[17]:


X = customers[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]


# In[18]:


from sklearn.model_selection import train_test_split


# In[19]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)


# In[20]:


from sklearn.linear_model import LinearRegression


# In[21]:


lm = LinearRegression()


# In[22]:


lm.fit(X_train,y_train)


# In[23]:


lm.coef_


# In[24]:


# The coefficients
print('Coefficients: \n', lm.coef_)


# In[27]:


predictions = lm.predict( X_test)


# In[31]:


plt.scatter(y_test,predictions)
plt.xlabel('Y Test (True Value)')
plt.ylabel('Predicted Y')


# In[33]:


from sklearn import metrics

print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))


# In[42]:


metrics.explained_variance_score(y_test,predictions)


# In[ ]:




