#!/usr/bin/env python
# coding: utf-8

# In[131]:


#Import numpy and pandas 
import numpy as np
import pandas as pd


# In[3]:


#Import visualization libraries and set %matplotlib inline.
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


#Read in the csv file as a dataframe called df
df = pd.read_csv('911.csv')


# In[5]:


#Check the head of df 
df.head()


# In[7]:


#What are the top 5 zipcodes for 911 calls?
df['zip'].value_counts().head(5)


# In[8]:


#What are the top 5 zipcodes for 911 calls?
df['twp'].value_counts().head(5)


# In[13]:


len(df['title'].unique())


# In[14]:


df['title'].nunique()


# In[19]:


#to create a new column of 'Reasons' with entry of Title Column
df['title']


# In[26]:


x = df['title'].iloc[0]


# In[27]:


x


# In[28]:


x.split()


# In[31]:


x.split(':')[0]


# In[32]:


# creating the reason column 
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])


# In[34]:


df['Reason']


# In[35]:


df['Reason'].value_counts()


# In[36]:


#Now using seaborn to create a countplot of 911 calls by Reason.
sns.countplot(x='Reason',data=df,palette='viridis')


# In[37]:


#Finding the datatype of the objects in the timeStamp column?
df.info()


# In[40]:


df['timeStamp'].iloc[0]


# In[41]:


type(df['timeStamp'].iloc[0])


# In[43]:


# Using pd.to_datetime to convert the column from strings to DateTime objects.
df['timeStamp'] = pd.to_datetime(df['timeStamp'])


# In[44]:


type(df['timeStamp'].iloc[0])


# In[50]:


#creating 3 new columns called Hour, Month, and Day of Week.
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)
 


# In[51]:


df.head()


# In[52]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


# In[53]:


df['Day of Week'] = df['Day of Week'].map(dmap)


# In[54]:


df.head()


# In[70]:


sns.countplot(x='Day of Week',data=df,hue='Reason',palette='viridis')
# To relocate the legend
plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)


# In[72]:


#  Now do the same for Month
sns.countplot(x='Month',data=df,hue='Reason',palette='viridis')

# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[73]:


byMonth = df.groupby('Month').count()
byMonth.head()


# In[76]:


# Could be any column
byMonth['twp'].plot()


# In[77]:


# Could be any column
byMonth['lat'].plot()


# In[82]:


byMonth.reset_index()


# In[83]:


sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())


# In[84]:


#Creating a new column called 'Date' that contains the date from the timeStamp column.
df['Date']=df['timeStamp'].apply(lambda t: t.date())


# In[86]:


df.head()


# In[89]:


df.groupby('Date').count().head()


# In[95]:


df.groupby('Date').count()['twp']


# In[91]:


df.groupby('Date').count()['twp'].plot()


# In[87]:


#Now groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.
df.groupby('Date').count()['twp'].plot()
plt.tight_layout()


# In[92]:


df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[97]:


# Now recreating this plot but create 3 separate plots with each plot representing a Reason for the 911 call.
df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[98]:


df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()


# In[99]:


df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()


# In[117]:


dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason']
dayHour


# In[118]:


dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
dayHour.head()


# In[122]:


plt.figure(figsize=(12,9))
sns.heatmap(dayHour,cmap='viridis')


# In[124]:


sns.clustermap(dayHour,cmap='viridis')


# In[127]:


dayMonth = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
dayMonth.head()


# In[129]:


plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='viridis')


# In[130]:


sns.clustermap(dayMonth,cmap='viridis')


# In[ ]:




