#!/usr/bin/env python
# coding: utf-8

# # Hotel cancellation Analysis

# In[208]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[209]:


df=pd.read_csv("hotel_booking.csv")
df


# In[210]:


df.shape


# In[211]:


df.describe()


# In[212]:


df.isnull().sum()


# In[213]:


df.info()


# In[214]:


df['reservation_status_date']=pd.to_datetime(df['reservation_status_date'])


# In[215]:


df.info()


# In[216]:


for col in df.describe(include='object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[217]:


df.drop(["company","agent"],axis=1,inplace=True)
df.dropna(inplace=True)


# In[218]:


df.isnull().sum()


# In[219]:


df.describe()


# In[220]:


df=df[df['adr']<5000]


# In[221]:


df.describe()


# # Data Analysis And Visualization

# In[222]:


cancelled_perc=df['is_canceled'].value_counts(normalize=True)
cancelled_perc
plt.figure(figsize=(4,4))
plt.bar(['Not Canceled','Canceled'],df['is_canceled'].value_counts(),width=0.5)
plt.title("Reservation Status Count")
plt.show()


# In[223]:


plt.figure(figsize = (8,4))
ax1= sns.countplot(x = 'hotel', data = df,hue = 'is_canceled', palette = 'Blues')
plt.title('Reservation status in different hotels', size = 20)
plt.xlabel('hotel')
plt.ylabel('number of reservations')
plt.legend(["not canceled","canceled"])
plt.show()


# In[224]:


resort_hotel=df[df['hotel']=='Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)


# In[225]:


city_hotel=df[df['hotel']=='City Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)


# In[226]:


resort_hotel=resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel=city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[227]:


plt.figure(figsize=(20,8))
plt.plot(resort_hotel.index,resort_hotel['adr'],label='Resort hotel')
plt.plot(city_hotel.index,city_hotel['adr'],label='City hotel')
plt.legend()
plt.show()


# In[228]:


df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize=(12,8))
ax= sns.countplot(x = 'month',hue = 'is_canceled',data=df, palette = 'Blues')
plt.legend(['not_canceled','canceled'])
plt.show()


# In[229]:


plt.figure(figsize=(14,8))
plt.title('ADR per month',fontsize=30)
sns.barplot('month','adr',data=df[df['is_canceled']==1].groupby('month')['adr'].sum().reset_index())
plt.show()


# In[230]:


cancelled_data=df[df['is_canceled']==1]
top_10_country=canceled_data['country'].value_counts()[:10]
plt.figure(figsize=(8,8))
plt.pie(top_10_country,autopct='%2.f',labels=top_10_country.index)
plt.show()


# In[231]:


mode=df['market_segment'].value_counts()
mode


# In[232]:


mode=df['market_segment'].value_counts(normalize=True)
mode


# In[233]:


cancelled_data['market_segment'].value_counts(normalize=True)


# In[235]:


cancelled_df_adr = cancelled_data.groupby('reservation_status_date') [['adr']].mean()
cancelled_df_adr.reset_index(inplace = True)
cancelled_df_adr.sort_values('reservation_status_date', inplace = True)

not_cancelled_df=df[df['is_canceled']==0]
not_cancelled_df_adr = not_cancelled_df.groupby('reservation_status_date') [['adr']].mean()
not_cancelled_df_adr.reset_index(inplace = True)
not_cancelled_df_adr.sort_values('reservation_status_date', inplace = True)

plt.figure(figsize = (20,6))
plt.title('Average Daily Rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'], not_cancelled_df_adr['adr'], label = 'not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'], cancelled_df_adr['adr'], label = 'cancelled')
plt.legend()


# In[242]:


cancelled_df_adr=cancelled_df_adr[(cancelled_df_adr['reservation_status_date']>'2016') & (cancelled_df_adr['reservation_status_date']<'2018')]
not_cancelled_df_adr=not_cancelled_df_adr[(not_cancelled_df_adr['reservation_status_date']>'2016') & (not_cancelled_df_adr['reservation_status_date']<'2018')]


# In[243]:


plt.figure(figsize = (20,6))
plt.title('Average Daily Rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'], not_cancelled_df_adr['adr'], label = 'not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'], cancelled_df_adr['adr'], label = 'cancelled')
plt.legend()


# In[ ]:




