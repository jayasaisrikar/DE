#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[13]:


data = pd.read_csv(r"C:\Users\JAYA SAI SRIKAR\OneDrive\Desktop\data1.csv")


# In[14]:


data.describe()


# In[15]:


data.head()


# In[16]:


data.tail()


# In[17]:


data.columns


# In[18]:


data.dropna()


# In[19]:


data.columns


# In[20]:


# Add a new column to the data frame
data['mycolumn'] = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

# Rename a column
data.rename(columns={'Maxpulse': 'Maximum Pulse'}, inplace=True)


# In[21]:


data.columns


# In[23]:


sub_data=data[['mycolumn','Calories']]


# In[24]:


sub_data


# In[29]:


import numpy as np
filtered_data=data[data['Calories']>280]


# In[30]:


filtered_data


# In[33]:


data.dropna()


# In[34]:


data.fillna(200)


# In[38]:


# Recognizing missing values
data.isnull()  # check for missing values
data.isnull().sum()  # count the missing values in each column

# Handling outliers
data[(data['Calories'] > lower_threshold) & (data['Calories'] < upper_threshold)]  # filter rows based on outlier thresholds


# In[39]:


df = pd.read_csv(r"C:\Users\JAYA SAI SRIKAR\OneDrive\Desktop\data1.csv")


# In[41]:


grouped = df.groupby('Calories')  # group the data based on a column


# In[43]:


grouped['Calories'].sum()  # apply a sum function to a specific column within each group


# In[55]:


# Add a new column to the data frame
df['mycolumn'] = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

pivot_table = df.pivot_table(values='Calories', index='Duration', columns='mycolumn')


# In[56]:


pivot_table


# In[57]:


cross_tab = pd.crosstab(df['Calories'], df['mycolumn'])  # create a cross-tabulation table


# In[58]:


cross_tab


# In[60]:


merged_df = pd.merge(data, df, on='mycolumn')  # merge two DataFrames based on a common column
concatenated_df = pd.concat([data, df])  # concatenate DataFrames vertically


# In[61]:


concatenated_df


# In[62]:


transposed_df = df.T  # transpose the DataFrame


# In[63]:


transposed_df


# In[66]:


sorted_df = df.sort_values('Calories', ascending=True)  # sort the DataFrame by a specific column


# In[67]:


sorted_df


# In[69]:


rem_dup=df.drop_duplicates(subset='mycolumn', keep='first', inplace=True)  # remove duplicate values from a column


# In[71]:


df


# In[76]:


df['Calories'] = df['mycolumn'].map(tuple)  # apply a function element-wise to a column


# In[77]:


df.describe()  # provide summary statistics of the DataFrame


# In[78]:


covariance = df['Calories'].cov(df['mycolumn'])  # calculate the covariance between two columns


# In[80]:


covariance


# In[81]:


correlation = df['Calories'].corr(df['mycolumn'])  # calculate the correlation between two columns


# In[82]:


correlation


# In[83]:


df['Calories'].hist()  # create a histogram of a column


# In[85]:


df.plot.scatter(x='mycolumn', y='Calories')  # create a scatter plot


# In[86]:


df.plot.area()  # create an area plot


# In[87]:


df.plot.line()  # create a line plot


# In[89]:


df['Calories'].plot.kde()  # create a KDE plot of a column


# In[ ]:




