#!/usr/bin/env python
# coding: utf-8

# In[26]:


get_ipython().system('pip install pandas-datareader ')
get_ipython().system('pip install yfinance')
import pandas_datareader as pdr
import pandas as pd
import yfinance as yfin

from datetime import datetime


# In[36]:


df_tesla=yfin.download(tickers='TSLA', period='5y', interval='1d')


# In[37]:


df_tesla


# In[39]:


type(df_tesla)


# In[40]:


df_tesla.tail()


# In[45]:


plt.figure(figsize=(12,4))
df_tesla['High'].plot()
plt.show()


# In[52]:


#x limit and y limit

df_tesla['High'].plot(xlim=['2020-01-01','2021-09-01'],ylim=[0,900],c='green',figsize=(12,4))
plt.show()


# In[53]:


df_tesla.index


# In[60]:


index=df_tesla.loc['2020-01-01':'2021-09-01'].index
shareprice_open=df_tesla.loc['2020-01-01':'2021-09-01']['Open']
shareprice_open


# In[61]:


index


# In[62]:


import matplotlib.pyplot as plt


# In[67]:


plt.figure(figsize=(12,4))
axis=plt.subplot()
axis.plot(index,shareprice_open)
plt.show()


# # Date Time Index

# In[78]:


df_tesla=df_tesla.reset_index()


# In[79]:


df_tesla.info()


# In[80]:


pd.to_datetime(df_tesla['Date'])


# In[81]:


df_tesla=df_tesla.set_index('Date',drop=True)
df_tesla


# # Resampling

# In[84]:


df_tesla.resample(rule='A').min()


# In[85]:


df_tesla.resample(rule='A').max()


# In[87]:


df_tesla.resample(rule='A').max()['Open'].plot()
plt.show()


# In[88]:


df_tesla.resample(rule='QS').max()['High'].plot()
plt.show()


# In[89]:


df_tesla.resample(rule='BA').max()['High'].plot()
plt.show()


# In[94]:


df_tesla['Open'].resample(rule='BA').mean().plot(kind='bar')
plt.show()


# In[101]:


plt.figure(figsize=(12,4))
df_tesla['Open'].resample(rule='M').max()
df_tesla['Open'].resample(rule='M').max().plot(kind='bar')
plt.show()


# In[103]:


df_tesla['High'].rolling(10).mean().head(20)


# In[104]:


df_tesla['open:30 Days rolling']=df_tesla['Open'].rolling(30).mean()
df_tesla


# In[115]:


df_tesla[['Open','open:30 Days rolling']].plot(figsize=(12,4))
plt.show()


# In[ ]:




