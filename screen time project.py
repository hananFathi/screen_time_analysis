#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


filepath=r"C:\Users\hanan\Downloads\csv-files\Screentime-App-Details.csv"


# In[3]:


data=pd.read_csv(filepath)


# In[4]:


data


# In[5]:


maxx=data['Usage'].max()
maxx


# In[6]:


maxx=data['Notifications'].max()
maxx


# In[7]:


maxx=data['Times opened'].max()
maxx


# In[8]:


data.info()


# In[9]:


maxx=data['App'].max()
maxx


# In[11]:


data.describe()


# In[13]:


data.isna().sum()


# In[16]:


grouped=data.groupby('App')
maxx=grouped['Times opened'].sum()
maxx


# In[17]:


maxx=grouped['Usage'].sum()
maxx
#most used app is whatsapp


# In[21]:


import matplotlib.pyplot as plt
x=data['Notifications']
y=data['Times opened']
plt.xlabel('notification')
plt.ylabel('Times Opened')
plt.plot(x,y)
plt.show()


# In[ ]:


users screen time is directly depended on notifications they recieve

