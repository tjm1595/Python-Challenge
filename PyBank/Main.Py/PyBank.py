#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Pandas
import pandas as pd


# In[10]:


#Name CSV File
bankdata = "PyBankData.csv"


# In[28]:


#CSV File as Dataframe
bankdata_df = pd.read_csv('PyBankData.csv')


# In[29]:


#Store Headers
bankdata_df.head()


# In[31]:


#Count Months
len(bankdata_df)


# In[32]:


#Display Number of Months
print("Total Months: ")
display(len(bankdata_df))


# In[33]:


#Calculate Profit Total
ProfitTotal = bankdata_df['Profit/Losses'].sum()
print(ProfitTotal)


# In[34]:


#Display Profit Total
print("Total: $" )
display(ProfitTotal)


# In[35]:


#Calculate Average Change over the period of time
Average = bankdata_df.iloc[85,1] - bankdata_df.iloc[0,1]
AverageChange = Average / 85
print(AverageChange)


# In[36]:


#Display Average Change
print("Average Change: $")
display(AverageChange)
      


# In[59]:


#Calculate Profit Changes on Month to Month Basis

bankdata_df["Changes"] = bankdata_df["Profit/Losses"].diff()
print(bankdata_df)
    


# In[72]:


#Find Minimum row using Index
Min = pd.Series(bankdata_df["Changes"]).idxmin()
print(Min)


# In[73]:


#Display row of minimum change
print(bankdata_df.loc[[49]])


# In[82]:


#Find Maximum row using Index
Max = pd.Series(bankdata_df["Changes"]).idxmax()
print(Max)


# In[76]:


#Display row of maximum change
print(bankdata_df.loc[[79]])


# In[81]:


#Write results to TXT file
file1 = open("PyBankResults.txt", "w")
file1.write("Financial Analysis \n")
file1.write("-------------------- \n")
file1.write("Total Months: 86 \n")
file1.write("Total: $22564198 \n")
file1.write("Average Change: $-8311.11 \n")
file1.write("Greatest Increase in Profit: 16-Aug $1862002.00 \n")
file1.write("Greatest Decrease in Profit: 14-Feb $-1825558.00 \n")
file1.close()


# In[ ]:




