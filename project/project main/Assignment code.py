#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd

# Define the API key
api_key = "YOUR_API_KEY"

# Define the list of companies
companies = ["AAPL", "AMZN", "DIS", "MSFT", "TSLA"]

# Define the base URL for the API request
base_url = "https://www.alphavantage.co/query?"

# Define the parameters for the API request
params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": " ",
    "apikey": "api_key"
}

# Loop through the list of companies
for company in companies:
    # Update the symbol parameter
    params["symbol"] = company
    
    # Make the API request
    response = requests.get(base_url, params=params)
    
    # Convert the API response to a pandas dataframe
    df = pd.DataFrame.from_dict(response.json()['Time Series (Daily)'])

#    spy_daily = pd.DataFrame.from_dict(res.json()['Time Series (Daily)'], orient='index')
    #spy_daily.head()

    
    # Transpose the dataframe
    df = df.transpose()
    
    # Save the dataframe to a csv file
    df.to_csv(f"{company}.csv")
    
    print(company+' downloaded successfully')


# In[2]:


#importing default data base sqlite3 and pandas 
import sqlite3
import pandas as pd 
#connect to the database
connection = sqlite3.connect('apple.db')
#extracting the dowloaded data
df = pd.read_csv('AAPL.csv')

df.columns = df.columns.str.strip()

    
df.to_sql('data',connection, if_exists = 'replace')
#create a crusor
v = connection.cursor()
#query the database
v.execute("CREATE TABLE apple (date integer,open integer,high integer, low integer, close integer, adjusted_close integer, volume integer, dividend_amount integer, split_coefficient integer)")
with open('AAPL.csv','r') as file:
    records = 0
    for row in file:
        v.execute("INSERT INTO apple VALUES(?,?,?,?,?,?,?,?,?)",row.split(","))
        connection.commit()
        records +=1
    
    print('record transfer completed')


# In[3]:


#importing default data base sqlite3 and pandas 
import sqlite3
import pandas as pd 
#connect to the database
connection = sqlite3.connect('amazon.db')
#extracting the dowloaded data
df = pd.read_csv('AMZN.csv')

df.columns = df.columns.str.strip()

    
df.to_sql('data',connection, if_exists = 'replace')
#create a crusor
v = connection.cursor()
#query the database
v.execute("CREATE TABLE amazon (date integer,open integer,high integer, low integer, close integer, adjusted_close integer, volume integer, dividend_amount integer, split_coefficient integer)")
with open('AMZN.csv','r') as file:
    records = 0
    for row in file:
        v.execute("INSERT INTO amazon VALUES(?,?,?,?,?,?,?,?,?)",row.split(","))
        connection.commit()
        records +=1
    
    print('record transfer completed')


# In[4]:


#importing default data base sqlite3 and pandas 
import sqlite3
import pandas as pd 
#connect to the database
connection = sqlite3.connect('disney.db')
#extracting the dowloaded data
df = pd.read_csv('DIS.csv')

df.columns = df.columns.str.strip()

    
df.to_sql('data',connection, if_exists = 'replace')
#create a crusor
v = connection.cursor()
#query the database
v.execute("CREATE TABLE disney (date integer,open integer,high integer, low integer, close integer, adjusted_close integer, volume integer, dividend_amount integer, split_coefficient integer)")
with open('DIS.csv','r') as file:
    records = 0
    for row in file:
        v.execute("INSERT INTO disney VALUES(?,?,?,?,?,?,?,?,?)",row.split(","))
        connection.commit()
        records +=1
    
    print('record transfer completed')


# In[5]:


#importing default data base sqlite3 and pandas 
import sqlite3
import pandas as pd 
#connect to the database
connection = sqlite3.connect('microsoft.db')
#extracting the dowloaded data
df = pd.read_csv('MSFT.csv')
df.columns = df.columns.str.strip()    
df.to_sql('data',connection, if_exists = 'replace')

#create a crusor
v = connection.cursor()
#query the database
v.execute("CREATE TABLE microsoft (date integer,open integer,high integer, low integer, close integer, adjusted_close integer, volume integer, dividend_amount integer, split_coefficient integer)")
with open('MSFT.csv','r') as file:
    records = 0
    for row in file:
        v.execute("INSERT INTO microsoft VALUES(?,?,?,?,?,?,?,?,?)",row.split(","))
        connection.commit()
        records +=1
    
    print('record transfer completed')


# In[7]:


#importing default data base sqlite3 and pandas 
import sqlite3
import pandas as pd 
#connect to the database
connection = sqlite3.connect('tesla.db')
#extracting the dowloaded data
df = pd.read_csv('TSLA.csv')

df.columns = df.columns.str.strip()

    
df.to_sql('data',connection, if_exists = 'replace')
#create a crusor
v = connection.cursor()
#query the database
v.execute("CREATE TABLE tesla (date integer,open integer,high integer, low integer, close integer, adjusted_close integer, volume integer, dividend_amount integer, split_coefficient integer)")
with open('TSLA.csv','r') as file:
    records = 0
    for row in file:
        v.execute("INSERT INTO amazon VALUES(?,?,?,?,?,?,?,?,?)",row.split(","))
        connection.commit()
        records +=1
    
    print('record transfer completed')


# In[9]:


#created an simple app to adding,deleting of data etc., can be done here for the amazon database table
import sqlite3

def show_all():
    con = sqlite3.connect ('amazon.db') 
    c = con.cursor()
    
    c.execute("SELECT rowid, * FROM amazon")
    items = c.fetchall()
    
    for item in items:
        print(item)
        
    con.commit()
    con.close()
#add new record to the table 
def add_one(date ,open ,high , low , close , adjusted_close , volume , dividend_amount , split_coefficient ):
    con = sqlite3.connect ('amazon.db') 
    c = con.cursor()
    c.execute("INSERT INTO amazon VALUES(?,?,?,?,?,?,?,?,?)",(date ,open ,high , low , close , adjusted_close , volume , dividend_amount , split_coefficient ))
    
    con.commit()
    con.close()


# In[10]:


show_all()


# In[14]:


add_one('2022-08-30',132,32,32,433,32,43,22,34)


# In[15]:


def delete_one():
    con = sqlite3.connect ('amazon.db') 
    c = con.cursor()
    c.execute("DELETE from amazon where low = 32")
    
    con.commit()
    con.close()


# In[16]:


delete_one()


# In[17]:


show_all()

