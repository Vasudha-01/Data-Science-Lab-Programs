#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


books_df = pd.read_csv("BL-Flickr-Images-Book.csv")
print("Original DataFrame:")
print(books_df.head())


# In[ ]:


irrelevant_columns = ['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner',
'Engraver', 'Contributors', 'Issuance type', 'Shelfmarks']
books_df.drop(columns=irrelevant_columns, inplace=True)


# In[ ]:


books_df.set_index('Identifier', inplace=True)
books_df['Date of Publication'] = books_df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
books_df['Date of Publication'] = pd.to_numeric(books_df['Date of Publication'], errors='coerce')


# In[ ]:


print("\nCleaned DataFrame:")
print(books_df.head())

