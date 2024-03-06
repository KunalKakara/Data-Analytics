#!/usr/bin/env python
# coding: utf-8

# # Super store Data Analysis

# # Question To Be Solved
# #1.Monthly sales Analysis
# #2.Analysis of the sales by category
# #3.Analysis of monthly profit
# #4.Profit analysis by category
# #5.Sales amd the Profit analysis by segmentation

# In[132]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default="plotly_white"
import warnings
warnings.filterwarnings('ignore')


# In[84]:


df=pd.read_csv('Sample_ Superstore.csv')


# In[85]:


df


# In[86]:


df.tail()


# In[87]:


df.describe()


# In[88]:


df.isnull().sum()


# In[89]:


df.info()


# In[90]:


df['Ship Date']=pd.to_datetime(df['Ship Date'])
df['Order Date']=pd.to_datetime(df['Order Date'])

df['Order Month']=df['Order Date'].dt.month
df['Order Day']=df['Order Date'].dt.day
df['Order year']=df['Order Date'].dt.year


# In[91]:


df.info()


# In[92]:


for col in df.describe(include='object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[93]:


fig=px.bar(df,x='Product Name',y='Sales')
fig.show()


# In[94]:


Sales_by_month=df.groupby('Order Month')['Sales'].sum().reset_index()
Sales_by_month


# In[101]:


fig=px.line(Sales_by_month,x='Order Month',y='Sales')
fig.show()


# In[96]:


Sales_by_year=df.groupby('Order year')['Sales'].sum().reset_index()
Sales_by_year


# In[97]:


fig=px.bar(Sales_by_year,x='Order year',y='Sales',color='Sales')
fig.show()


# In[120]:


Category_1=df.groupby('Category')['Sales'].sum().reset_index()
Category_1


# In[124]:


fig=px.pie(Category_1,names='Category',values='Sales',color='Category',hole=0.5)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text='Sales Analysis by Category')
fig.show()


# In[125]:


Profit_monthly=df.groupby('Order Month')['Profit'].sum().reset_index()
Profit_monthly


# In[126]:


fig=px.line(Profit_monthly,x='Order Month',y='Profit')
fig.show()


# In[127]:


Category_profit=df.groupby('Category')['Profit'].sum().reset_index()
Category_profit


# In[129]:


fig=px.bar(Category_profit,x='Category',y='Profit',color='Category')
fig.show()


# In[135]:


import plotly.graph_objects as go
import plotly.express as px

# Calculate sales and profit by segment
sales_profit_by_segment = df.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

# Define color palette
color_palette = px.colors.qualitative.Pastel

# Create a figure
fig = go.Figure()

# Add bar traces for sales and profit
fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'], y=sales_profit_by_segment['Sales'], name='Sales', marker_color=color_palette[6]))
fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'], y=sales_profit_by_segment['Profit'], name='Profit', marker_color=color_palette[0]))

# Update layout
fig.update_layout(title='Sales and Profit Analysis by Customer Segment', xaxis_title='Customer Segment', yaxis_title='Amount')

# Show the figure
fig.show()


# In[ ]:




