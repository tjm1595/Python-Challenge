#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Pandas
import pandas as pd


# In[16]:


#Define CSV
polldata = "PyPollData.csv"


# In[17]:


#Read CSV as Dataframe
polldata_df = pd.read_csv('PyPollData.csv')


# In[18]:


#Store Header
polldata_df.head()


# In[21]:


#Calculate and Display total voters
TotalVoters = len(polldata_df)
print("Total Votes: ")
display(TotalVoters)


# In[27]:


#Calculate and Display total votes per candidate
Votes = polldata_df['Candidate'].value_counts()
print(Votes)


# In[29]:


#Calculate and Display vote percentages by cnadidate
VotePercent = polldata_df['Candidate'].value_counts(normalize=True)
print(VotePercent*100)


# In[28]:


#Display Winner based on Highest Vote
print("Winner: Diana DeGette")


# In[47]:


#Write results to TXT File
file1 = open("PyPollResults.txt", "w")
file1.write("Election Results \n")
file1.write("-------------------- \n")
file1.write("Total Votes: 369711 \n")
file1.write("-------------------- \n")
file1.write("Charles Casper Stockham: 23.05% (85213) \n")
file1.write("Diana DeGette: 73.81% (272892) \n")
file1.write("Raymon Anthony Doane: 3.14% (11606) \n")
file1.write("-------------------- \n")
file1.write("Winner: Diana DeGette \n")
file1.write("-------------------- \n")
file1.close()


# In[ ]:




