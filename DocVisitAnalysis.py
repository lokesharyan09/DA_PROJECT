#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# # Importing Dataset
# 
# 

# In[5]:


df=pd.read_csv("DoctorVisits .CSV")


# # First 15 Rows of data

# In[6]:


df.head(15)


# #  Last 15 rows of data

# In[13]:


df.tail(15)


# # Information of Dataset
# 

# In[7]:


df.info()


# # Statistical description of data

# In[8]:


df.describe()


# # Frequency of people visting doctor
# 

# In[10]:


df['gender'].value_counts()


# # Number of people suffering with number of diseases   

# In[11]:


df["illness"].value_counts()


# #  Number of vistings of people with doctor

# In[12]:


df["visits"].value_counts()


# # Number of people with private field

# In[14]:


df["private"].value_counts()


# #  Visualise and analyze the maximum, minimum and median of income

# In[15]:


y=list(df.income)
plt.boxplot(y)
plt.show()


# #  Number of reduced activity days of male and female due to illness

# In[16]:


df.groupby(['gender','reduced']).mean()


# # Cleaning the data whether if any empty values are present

# # # using heatmap 

# In[20]:


sns.heatmap(df.isnull(),cbar=True,cmap='viridis')


# In[22]:


sns.heatmap(df.isnull(),cbar=False,cmap='viridis')


# # Income of patients related with visits to the hospital

# In[24]:


plt.figure(figsize=(10,10))

plt.scatter(x='visits',y='income',data=df)
plt.xlabel('visits')
plt.ylabel('income')


# #  Ratio of males and females with illness

# In[26]:


sns.histplot(df.gender,bins=2)


# #  Co-relation between different variables in the given dataset 

# In[27]:


plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),cbar=True, annot=True, cmap='Blues')


# # Horizontal bar chart to analyze the reduced days of activity due to illness based on gender 

# In[38]:


db=df.groupby('gender')['reduced'].sum().to_frame().reset_index()
plt.barh(db['gender'],db['reduced'],color=['red','palegreen'])
plt.title('BAR GRAPH')
plt.xlabel('gender')
plt.ylabel('Reduced activity')
plt.show()


# In[40]:


plt.figure(figsize=(20,20))
sns.pairplot(df)


# # To analyze the reduced days of activity due to illness based on gender with pie charts

# In[48]:




label=['yes','no']
y=df[df['freerepat']=='yes']
n=df[df['freerepat']=='no']
x=[y.shape[0],n.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% of old age people getting health insurance from government")
plt.show()

label=['yes','no']
y=df[df['freepoor']=='yes']
n=df[df['freepoor']=='no']
x=[y.shape[0],n.shape[0]]
plt.figure(figsize=(6,6))
plt.pie(x,labels=label)
plt.title("% of people getting Health Insurance from government for having less income")
plt.show()
        
        
label=['yes','no']
y=df[df['private']=='yes']
n=df[df['private']=='no']
x=[y.shape[0],n.shape[0]]
plt.figure(figsize=(6,6))
plt.pie(x,labels=label)
plt.title("% of people getting health insurance from private field")
plt.show()


# In[ ]:




