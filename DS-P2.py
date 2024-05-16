#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt

!dir mtc*
mtcars = pd.read_csv("mtcars.csv")

mtcars.head()
mtcars.shape
mtcars.info()
mtcars.columns
mtcars.describe()

plt.hist(mtcars['mpg'], bins=10, color='blue', edgecolor='black')
plt.xlabel('Miles per gallon (mpg)')
plt.ylabel('Frequency')
plt.title('Histogram of Miles per gallon (mpg)')
plt.show()
