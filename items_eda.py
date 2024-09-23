#!/usr/bin/env python
# coding: utf-8

# In[106]:


import pandas as pd


# In[107]:


items=pd.read_csv('items.csv')
items.head()


# In[108]:


type(items)


# In[57]:


#i. Read `items.csv` making `item_name` as index.
items.set_index('item_name')


# In[109]:


#ii. Show no of nan values
items.isna().sum()


# In[120]:


items['item_price']


# In[130]:


#ii. Item price is given in $, so convert it to rupees without currency symbol.
items['item_price']=items['item_price'].str.replace('$','').str.strip().values


# In[166]:


#iii. Make data type of newly made series as float.
items['item_price']=items['item_price'].astype('float')*80


# In[167]:


#iv. Fill nan with mean of the series
mean_value=items['item_price'].mean()
items['item_price']=items['item_price'].fillna(mean_value)


# In[168]:


items['item_price'].isna().sum()


# In[169]:


#i. Find mean price
mean_val=items['item_price'].mean()
mean_val


# In[170]:


#ii. Find 30th and 6th percentile value
percentile_30=items['item_price'].quantile(.30)
percentile_6=items['item_price'].quantile(.06)
print("percentile_30=",percentile_30,"\npercentile_6=",percentile_6 )


# In[171]:


#iii. Plot Histogram on price with bin size 50values
items['item_price'].plot(kind='hist',bins=50)


# In[172]:


import matplotlib.pyplot as plt
plt.hist(items['item_price'],bins=50)
plt.show()


# In[173]:


get_ipython().system('pip install seaborn')
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(items['item_price'], bins=50)
plt.show()


# In[174]:


#iv. No of items price lies between [1000 to 2000]
filtered_items = items[(items['item_price'] > 1000) & (items['item_price'] < 2000)]


# In[175]:


filtered_items


# In[ ]:




