#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib


# In[2]:


df1=pd.read_csv("C:/Users/91904/OneDrive/Desktop/SECOND HAND BIKE SALE/Machine learning/Used_Bikes.csv")


# In[3]:


df1.shape


# In[4]:


df1.head()


# In[5]:


df1.city.unique()


# In[6]:


df1.bike_name.unique()


# In[7]:


df1.isnull().sum()


# In[8]:


df1.city = df1.city.apply(lambda x: x.strip())
city_stats = df1['city'].value_counts(ascending=False)
city_stats


# In[9]:


df1.price.describe()


# In[10]:


city_stats_less_than_10 = city_stats[city_stats<=10]
city_stats_less_than_10


# In[11]:


df1.city = df1.city.apply(lambda x: 'other' if x in city_stats_less_than_10 else x)
len(df1.city.unique())


# In[12]:


df1


# In[ ]:





# In[13]:


index_kms = df1[ (df1['kms_driven'] <100)].index
df1.drop(index_kms , inplace=True)
df1.shape


# In[14]:


dummies = pd.get_dummies(df1.city)
dummies.head(3)


# In[15]:


df2 = pd.concat([df1,dummies.drop('other',axis='columns')],axis='columns')
df2.head()


# In[16]:


df3 = df2.drop('city',axis='columns')
df3.head(2)


# In[17]:


df3.shape


# In[18]:


dummies = pd.get_dummies(df3.brand)
dummies.head(3)
df4= pd.concat([df3,dummies],axis='columns')
df4.head()


# In[19]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df4['owner']= le.fit_transform(df4['owner'])


# In[20]:


X = df4.drop(['price','bike_name',"brand"],axis='columns')
X.head(3)
Y=df4[["price"]]


# In[21]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=10)


# In[22]:


from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score

cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)

cross_val_score(LinearRegression(), X, Y, cv=cv)


# In[23]:


#use k fold cross validation to measure accuracy of our Linear regression model


# In[24]:


from sklearn.linear_model import LinearRegression
final_model=LinearRegression()
final_model.fit(X,Y)


# In[25]:


from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score

cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)

cross_val_score(LinearRegression(), X, Y, cv=cv)


# In[26]:


X.columns


# In[36]:


def predict_price(kms_driven,owner,age,power,city,model):
    city_index=np.where(X.columns==city)[0][0]
    model_index=np.where(X.columns==model)[0][0]
    x=np.zeros(len(X.columns))
    x[0]=kms_driven
    x[1]=owner
    x[2]=age
    x[3]=power
    if city_index>=0:
        x[city_index]=1
        
    if model_index>=0:
        x[city_index]=1
    return final_model.predict([x])[0]    
    


# In[37]:


predict_price(1000,1,2,350,"Delhi","Royal Enfield")


# In[55]:


import pickle
with open('India_bike_prices_model.pickle','wb') as f:
    pickle.dump(final_model,f)


# In[56]:


import json
columns = {
    'data_columns' : [col.lower() for col in X.columns]
}
with open("columns.json","w") as f:
    f.write(json.dumps(columns))


# In[57]:


print(X.columns)


# In[58]:


i=0
for city in X.columns:
    i=i+1
    if city=='Visakhapatnam':
        print(i)
    if city=='Yamaha':
        print(i)
    
        
        
    


# In[61]:





# In[ ]:




