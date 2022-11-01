#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)


# In[3]:


# Bank of America
BAC = data.DataReader("BAC", 'yahoo', start, end)


# In[4]:


BAC.head()


# In[5]:


# CitiGroup
C = data.DataReader("C", 'yahoo', start, end)

# Goldman Sachs
GS = data.DataReader("GS", 'yahoo', start, end)

# JPMorgan Chase
JPM = data.DataReader("JPM", 'yahoo', start, end)

# Morgan Stanley
MS = data.DataReader("MS", 'yahoo', start, end)

# Wells Fargo
WFC = data.DataReader("WFC", 'yahoo', start, end)


# In[6]:


tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']


# In[7]:


bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC],axis=1,keys=tickers)


# In[8]:


bank_stocks.columns.names = ['Bank Ticker','Stock Info']


# In[9]:


bank_stocks


# In[10]:


for tick in tickers:
   print(tick, "=" ,bank_stocks[tick]['Close'].max())


# In[11]:


returns = pd.DataFrame()


# In[12]:


for tick in tickers:
    returns[tick+' Return'] = bank_stocks[tick]['Close'].pct_change()
returns.head()


# In[13]:


#returns[1:]
import seaborn as sns
sns.pairplot(returns[1:])


# In[14]:


# Worst Drop (4 of them on Inauguration day)
returns.min()


# In[15]:


returns.idxmin()


# In[16]:


# Best Single Day Gain
# citigroup stock split in May 2011, but also JPM day after inauguration.
returns.idxmax()


# In[17]:


# Citigroup riskiest
returns.std() 


# In[18]:


# Very similar risk profiles, but Morgan Stanley or BofA
returns.loc['2015-01-01':'2015-12-31'].std() 


# In[19]:


#Creating a distplot using seaborn of the 2015 returns for Morgan Stanley 
sns.distplot(returns.loc['2015-01-01':'2015-12-31']['MS Return'],color='green',bins=100)


# In[20]:


#Creating a distplot using seaborn of the 2008 returns for CitiGroup
sns.distplot(returns.loc['2008-01-01':'2008-12-31']['C Return'],color='red',bins=100)


# In[21]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')

# Optional Plotly Method Imports
import plotly
import cufflinks as cf
cf.go_offline()


# In[22]:


#Create a line plot showing Close price for each bank for the entire index of time.
for tick in tickers:
    bank_stocks[tick]['Close'].plot(figsize=(12,4),label=tick)
plt.legend()


# In[27]:


bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot()


# In[24]:


# plotly
bank_stocks.xs(key='Close',axis=1,level='Stock Info').iplot()


# In[28]:


#Ploting the rolling 30 day average against the Close Price for Bank Of America's stock for the year 2008
plt.figure(figsize=(12,6))
BAC['Close'].loc['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 Day Avg')
BAC['Close'].loc['2008-01-01':'2009-01-01'].plot(label='BAC CLOSE')
plt.legend()


# In[30]:


bank_stocks.xs(key='Close',axis=1,level='Stock Info')


# In[32]:


bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr()


# In[33]:


#Creating a heatmap of the correlation between the stocks Close Price.
sns.heatmap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)


# In[34]:


sns.clustermap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)


# In[51]:


close_corr=bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr()
close_corr


# In[52]:


close_corr.iplot(kind='heatmap',colorscale='rdylbu')


# In[54]:


BAC


# In[57]:


# Using .iplot(kind='candle) to create a candle plot of Bank of America's stock from Jan 1st 2015 to Jan 1st 2016.
basic15 = BAC[['Open', 'High', 'Low', 'Close']].loc['2015-01-01':'2016-01-01']
basic15.iplot(kind='candle')


# In[59]:


#Using .ta_plot(study='boll') to create a Bollinger Band Plot for Bank of America for the year 2015.
BAC['Close'].loc['2015-01-01':'2016-01-01'].ta_plot(study='boll')


# In[ ]:




