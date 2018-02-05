
# coding: utf-8

# # Vancouver Crime Data
# 
# For my project while at The Data Incubator, I've decided to do an analysis of the crimes reported in **Vancouver, BC** to the **Vancouver Police Department (VPD)**.
# 
# I've been living in Vancouver for the past 2.5 years and it only seems fit that I choose a dataset related to this city. Vancouver is consistently ranked within the **Top 3** livable cities in the world, however, it still faces its challenges related to number of crimes.
# 
# The data was obtained from the [Open Data Catalouge](http://data.vancouver.ca/datacatalogue/crime-data.htm "Crime Data") by [VPD](http://vancouver.ca/police/ "Vancouver Police Department")

# In[27]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ### Importing Data
# 
# The data in the form of a csv file contained in a zip file. For this analysis, I've dropped the data from the current year 2018 for sake of simplicity.
# The attributes for this dataset are:
# * TYPE: The type of crime activities
# * YEAR: A four-digit field that indicates the year when the reported crime activity occurred
# * MONTH: A numeric field that indicates the month when the reported crime activity occurred
# * DAY: A two-digit field that indicates the day of the month when the reported crime activity occurred
# * HOUR: A two-digit field that indicates the hour time (in 24 hours format) when the reported crime activity occurred
# * MINUTE: A two-digit field that indicates the minute when the reported crime activity occurred
# * HUNDRED_BLOCK: Generalized location of the report crime activity
# * NEIGHBOURHOOD: The Vancouver Police Department uses the Statistics Canada definition of neighbourhoods within municipalities. Neighbourhoods within the City of Vancouver are based on the census tract (CT) concept within census metropolitan area (CMA).
# * X: Coordinate values are projected in UTM Zone 10.
# * Y: Coordinate values are projected in UTM Zone 10.
# 

# In[84]:


df = pd.read_csv('crime_csv_all_years.csv')
df = df[df.YEAR != 2018]


# In[85]:


df


# To get a rough idea regarding the types of crimes present in the dataset.

# In[29]:


df.TYPE.value_counts()


# ### Breaking down total number of crimes in each subtype by the Year

# In[88]:


year_type = pd.crosstab(index=df['TYPE'],columns=df['YEAR'])


# In[87]:


year_type


# Let's have a look these in a plot. Now, this gets a little messy considering the scales for different crimes. For example, *Theft from Vehicle* deals in values >10000 while *Homicides* are typically 10-30 in a given year.

# In[96]:


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
# ax.plot(year_type.columns,year_type.iloc[7])
for i in range(len(year_type.index)):
    plt.plot(year_type.columns,year_type.iloc[i],label = '%s'%year_type.index[i])
plt.legend()
ticks = [y for y in range(2003,2018)]
ax.set_xticks(ticks)
plt.show()


# ### Bike Theft
# 
# Let's focus on the *Theft of Bicycle*. Bike is allegedly one of the two most stole items in Vancouver (other being umbrella; it might seem weird but it's not consdering that it's always raining Vancouver, sometimes dubbed as 'Raincouver').

# In[100]:


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.plot(year_type.columns,year_type.loc['Theft of Bicycle'])
ticks = [y for y in range(2003,2018)]
ax.set_xticks(ticks)
plt.show()


# As is evident from the graph above, we see a huge increase in the bike theft from 2011 but then a sharp decrease from 2015. This is attributed to a bike registration app called [Project 529](https://project529.com/garage/) which makes it easiers to track down stolen bikes.
# 
# Now, let's take a look at bike thefts in different months.

# In[101]:


month_type = pd.crosstab(index=df['TYPE'],columns=df['MONTH'])


# In[102]:


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.plot(month_type.columns,month_type.loc['Theft of Bicycle'])
m = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec']
ticks = [m for m in range(1,13)]
ax.set_xticks(ticks)
ax.set_xticklabels(m)
plt.show()


# Unsurprisingly, bikes are used most during summer and hence a sharp increase during the sumer months peaking around July and August.

# This is the extent of my analysis so far and I will keep updating it.
