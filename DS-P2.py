#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt

# In[2]:

mtcars = pd.read_csv("C:\\Users\\CSD 29\\Downloads\\mtcars.csv")
mtcars.head()
mtcars.shape
mtcars.info()
mtcars.columns
mtcars.describe()

# In[5]:


plt.hist(mtcars['mpg'], bins=10, color='blue', edgecolor='black')
plt.xlabel('Miles per gallon (mpg)')
plt.ylabel('Frequency')
plt.title('Histogram of Miles per gallon (mpg)')
plt.show()

