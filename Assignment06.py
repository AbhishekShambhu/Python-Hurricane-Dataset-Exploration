# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 22:05:20 2018

@author: Abhishek
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

os.getcwd()
os.chdir('C:/Users/Abhishek/Desktop/AIT 580/Assignments/Assignment 06')

hurridate = pd.read_csv("hurricanes.csv", sep="|")
hurridate

list(hurridate)

['Year',
 'Month',
 'States_Affected',
 'Highest_Category',
 'Central_Pressure_mb',
 'Max_Winds_kt',
 'Name']

hurridate['Month'].describe()
hurridate['Highest_Category'].describe()
hurridate['Central_Pressure_mb'].describe()
hurridate['Max_Winds_kt'].describe()

hurridate['Highest_Category'].head()
hurridate.head()
hurridate.tail()

hurridate.info()

hurridate.groupby('Month')

hurridate['Central_Pressure_mb'].plot(kind='line', legend=True)
hurridate['Max_Winds_kt'].plot(kind='line', legend=True)

plt.style.use('ggplot')
hurridate.groupby(['Month']).Month.count().plot.bar(legend=True)
plt.show()

plt.style.use('ggplot')
hurridate.groupby(['Highest_Category']).Highest_Category.count().plot.bar(legend=True)
plt.show()

#hurridate['Month'].plot(kind='bar')
#hurridate['Central_Pressure_mb'].plot(kind='bar')
#hurridate['Month'].plot.bar
#hurridate['Month'].plot(kind='line')

#hurr1 = hurridate.groupby('Month').plot()

#hurridate.hist(column='Month',bins=25, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)
#hurridate.hist(column='Highest_Category')

plt.scatter(hurridate['Highest_Category'],hurridate['Max_Winds_kt'])
plt.scatter(hurridate['Central_Pressure_mb'],hurridate['Max_Winds_kt'])

hurridate['Central_Pressure_mb'].fillna(value=hurridate['Central_Pressure_mb'].mean())
hurridate.dropna()
pd.isnull(hurridate).any()
hurridate.info()

#Missing data are very crucial in a dataset and needs to be properly handled as 
#they impact the insights that can be perceived from the model.
#From our dataset we can see that Central_Pressure_mb,Max_Winds_kt and Name has missing values which
# can either be removed or can be imputed.
#Since, we have a large number almost 1/3rd of the values missing for Max_Winds_kt it is better
# to replace(impute) with either mean, median or the mode.
# Also, as only 4 Central_Pressure_mb values are missing we can ignore those rows.
# Deleting or imputing large number of rows would definitely impact the output of the dataset and the
#dataset can be biased.


