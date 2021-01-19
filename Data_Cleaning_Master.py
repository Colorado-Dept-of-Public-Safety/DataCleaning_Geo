#!/usr/bin/env python
# coding: utf-8

# <h2><u> Data Cleaning Master List</u></h2>
# <h4> This Notebook provides a series of python scripts that can be run for cleaning data. 
#     <p> The scripts consist of the following:</p></h4>
#     <p> 1.) Remove all Null Data  </p>
#     <p> 2.) Remove Duplicate Rows </p>
#     <p> 3.) Make Rows Proper Case </p> 
#     <p> 4.) Convert PDF to CSV </p>
#     <p> 5.) Dropping Columns </p> 
#     <p> 6.) Rename Columns </p>  
#     <h4><u> Dependancies Used:</u> </h4>
#         <p> 1.) Pandas </p>
#         <p> 2.) Geopandas </p>
#         <p> 3.) Numpy </p>
#     <h4><u> Dataset Used for Examples:</u> <a href="https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-crime"> <p> Denver Crime Data- Last 5 years</p></a></h4>
#            

# <h2><u> 1. Removing All Null Data</u></h2> 
# <h4> Source:  <a href= "https://code.likeagirl.io/how-to-use-python-to-remove-or-modify-empty-values-in-a-csv-dataset-34426c816347"> How-To Use Python to Remove or Modify Empty Values in a CSV Dataset By Leah Cole</a> 
#     <p>  TLDR: There are two options for removing null values from a data set.</p> 
#     <p> 1.) Remove all null values and put them in a seperate data frame. </p> 
#     <p> 2.) Replace empty values with a space. </p>

# In[1]:


# Step 1: Import your dependancies 
import pandas as pd
import numpy as np


# In[2]:


# Step 2: Bring your csv file info a Dataframe
crimes = pd.read_csv(r"./Denver_Crime.csv")
# Step 2a: Show the first 5 rows by using  the head command. 
crimes.head()


# In[3]:


# Step 3: Check the shape of your data using .shape command This tells you how many columns and rows you have in your dataset.
crimes.shape 


# In[4]:


# Step 4: Check for null values in your data set using the .isnull() command.
crimes.isnull()


# In[5]:


# Step 5: Get a sum of how many null values exisit in your data set. Use .isnull().sum 
crimes.isnull().sum()


# In[6]:


# Step 6: Check how many null values are in a specific column
crimes["LAST_OCCURRENCE_DATE"].isnull().sum()


# In[7]:


#Step 7: We are going to start with Option 2. Replacing all null values with a space. 
modifiedcrimes=crimes.fillna("")
#Check to see if there are any null values left. 
modifiedcrimes.isnull().sum()


# In[8]:


# Step 8: Save your modified dataset to a new CSV
modifiedcrimes.to_csv('modifiedcrimes.csv',index=False)


# In[9]:


# Option 2: Deleting the null values completely 
# Reminder you have two dataframes. Your crimes DF and modified crimes DF.
#Step 1: Use .dropna()
modified_crimes = crimes.dropna()


# In[10]:


# Step 2: confirm that your modified_crimes dataframe doesnt have any null values by using the .sum() 
modified_crimes.isnull().sum()


# In[11]:


#Step 3: You can once again make a CSV with the null values deleted competely. 
modified_crimes.to_csv('modified_crimes.csv',index=False)


# <h2><u> 2. Remove Duplicate Rows </u></h2> 
# <h4> Source: <a href = "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html">Pandas Drop Duplicate Rows </a>

# In[12]:


crimes.drop_duplicates()


# In[13]:


# Drop duplicates in a specfic column
crimes.drop_duplicates(subset=['LAST_OCCURRENCE_DATE'])


# <h2><u> 3. Make Rows Proper Case </u></h2> 
# <h4> Source: <a href="https://www.geeksforgeeks.org/python-pandas-series-str-lower-upper-and-title/"> GeeksforGeeks</a></h4>
# <p> Note: The crimes dataframe is already properly cased. I'll run through each example of how to make the data upper, lower and proper or title case.  </p> 

# In[14]:


# Make a column all upper case
crimes["OFFENSE_TYPE_ID"]= crimes["OFFENSE_TYPE_ID"].str.upper()
crimes.head() # Notice that the text in the Offense_Type_id column is now all upper case. 


# In[15]:


# Make the OFFENSE_TYPE_ID column title case. 
crimes["OFFENSE_TYPE_ID"]= crimes["OFFENSE_TYPE_ID"].str.upper().str.title()
crimes.head() # In the forementioned column, the text is now proper case with the beginning of the word, being captialized. 


# In[16]:


# Make column lowercase 
crimes["OFFENSE_TYPE_ID"]= crimes["OFFENSE_TYPE_ID"].str.lower()
crimes.head() #Now the data is returned to it's orginal state, which was all lowercase. 


# <h2> 4. Convert a PDF File to a CSV </h2> 
# <h4> Notes: I created a specfic script for this task based on a 500 page pdf file. 
# <p> You'll need to import another package using pip to get thsi script to work. 
#     <p> Dependancy:<a href="https://pypi.org/project/tabula-py/">tabula-py</a> 
#     <p> Data Set can be found  In CHSS Google Folder- DHSEM </p> 

# In[4]:


import tabula
import os


# In[14]:


# insert file 
file = r'.\DEHS_ManufacturedFood_ApprovedSourceList_Updated.pdf' # This wont work due to remove of the absolute path
# Use tabula.read_pdf to read the PDF into the system.
table = tabula.read_pdf(file, pages = "all", multiple_tables = True)


# In[15]:


#Convert PDF to CSV 
tabula.convert_into(file, r'insert path name and name of csv', pages="all")


# <h2> 5. Drop Columns </h2>
# <p> Source: <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html"> Pandas Main Website </a></p>
# <p> Data Source : Denver Crimes </p> 

# In[18]:


# Get rid of columsn that aren't needed in the overall dataset. 
modified_crimes.drop(columns=['INCIDENT_ADDRESS', 'GEO_X', 'GEO_Y'])
# You will the note that at the bottom of the chart, the shape of your data frame has changed from 19 to 16, cause you removed three columns. 


# In[ ]:




