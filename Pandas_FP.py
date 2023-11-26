import pandas as pd
import numpy as np
pf = pd.read_excel('Power BI Dataset.xlsx')

'''
What is Pandas?
Pandas is a Python library to deal with sequential and tabular data. 
It includes many tools to manage, analyze and manipulate data in a convenient and efficient manner. 
We can think of its data structures as akin to database tables or spreadsheets.

Pandas is built on top of the Numpy library and has two primary data structures viz. 
Series (1-dimensional) and DataFrame (2- dimensional). 

What is Series (1-dimensional) or homogeneous data?

Series is designed to represent one-dimensional data structures, and the square brackets are used to denote an ordered sequence of values. 
In Pandas when defining the values for a Series because they denote a collection of ordered values, which is a fundamental aspect of this data structure.

What is DataFrame (2-dimension) or heterogeneous data? 
DataFrame is a combination of Rows and Cloumns.

It can handle both homogeneous and heterogeneous data, and some of its many capabilities are:
• ETL tools (Extraction, Transformation and Load tools)
• Dealing with missing data (NaN)
• Dealing with data files (csv, xls, db, hdf5, etc.)
• Time-series manipulation tools

Pandas works with homogeneous data series (1-Dimension) and heterogeneous tabular data series (2-Dimensions). 
It includes a multitude of tools to work with these data types, such as:
• Indexes and labels.
• Searching of elements.
• Insertion, deletion and modification of elements.
• Apply set techniques, such as grouping, joining, selecting, etc.
• Data processing and cleaning.
• Work with time series.
• Make statistical calculations
• Draw graphics
• Connectors for multiple data file formats, such as, csv, xlsx, hdf5, etc.
'''
s = pd.Series([1,2,3,4,5,6,'1','a'])
print(type(s))

s = pd.Series(['a','b',1,2.0])
print(type(s))

# Pandas Series in Dictionary

import pandas as pd
dictionary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
s = pd.Series(dictionary)

print(s[4]) # 5
print(s[[1,4]]) # b 2 e 5

print(s[2:]) 
print(s[2:4])
print(s[:3])
print(s[-2:-1])

# print(s[1])
# s[1]=99
# print(s[1])
# s.pop('a') #deleting the selected value
# s.pop
# print(s)
# print(s.get('b'))

# dictionary = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
# s = pd.Series(dictionary)
# #Addition, subraction, Multiplication & Division process in Pandas Series
# print(s**3)

# # We can perform the same operations over two Pandas Series although these must be aligned, 
# # that is, to have the same index, in other case, perform a Union operation.
# #print(s+s)

# # Unaligned series
# a = [1,2,3,4,5]
# s1 = pd.Series(a)
# print(s+s1)

# Pandas DataFrame

# Pandas DataFrame is a heterogeneous two-dimensional object.
# The data are of the same type within each column but it could be a different data type for each column 
# and are implicitly or explicitly labeled with an index

# s = pd.DataFrame()
# print(s)

# #Output
# #Empty DataFrame
# #Columns: []
# #Index: []

# a = {'Emp_id':[100,101,102,103,104],'FirstName':['King','John','Blake','Scott','Smith']
#      ,'LastName':['Solomon','Smith','Null','Null','Null'],'Mgr':[100,101,100,102,103],'Sal':[12000,12001,12000,10000,12000]
#      ,'Hiredate':['1993-01-01','1998-01-01','1996-01-01','1997-01-01','2000-01-01']}
# s=pd.DataFrame(a, index=range(1,6))
# print(s[1])

# # How to read a Excel file
# pf = pd.read_excel('Power BI Dataset.xlsx')
# print(pf)

# # Printing the First 5 Lines from the Excel sheet
# print(pf.head()) #Displays the First 5 rows

# # Printing the Last 5 Lines from the Excel sheet
# print(pf.tail()) #Displays the Last 5 rows

# #Displays the number of records present under each column
# print(pf.count()) 

# #Displays number of Rows and Columns present 
# print(pf.shape) 

# # To get all the Columns List
# print(pf.columns)

# # To get the Index details
# print(pf.index)  #RangeIndex(start=0, stop=4115, step=1)

# # To rename a column 
# print(pf.rename(columns={'Sales':'Sales_List'}))

# # To rename multiple column
# print(pf.rename(columns={'Sales':'Sales_List', 'Order ID':'Order_ID'}))

# How to set the data display

# pd.set_option('Display_max_column', None)
# print(pf.head(2))

# pd.set_option('Display_max_column',7)
# print(pf.head(3))

# pd.set_option('Display_max_column', 3)
# print(pf.head(1))

# pf = pd.read_excel('Power BI Dataset.xlsx')
# pd.set_option('display.max_columns', 5)
# print(pf.iloc[:,:5].head(2))
# print(pf.iloc[1:5,:5])
# print(pf.iloc[:,3:5])

# # Selecting a single column
# df=pf['Sales']
# print(df)

# # Selecting Multiple column
# df=pf[['Sales','Region']]
# print(df)

# Setting a column as Index
# df = pf.set_index('Order ID')
# print(df)

# # Selecting a row
# df = pf.iloc[0]
# print(df, sep=' ')

# # Selecting Multiple rows using iloc
# df = pf.iloc[0:5]
# print(df, sep=' ')

# # Selecting Multiple rows using loc
# df = pf.loc[0:5]
# print(df, sep=' ')

# # What is loc and iloc? What is the difference?
# # loc & iloc are two important selection methods in Pandas.

# # loc: Label-based selection method in Pandas for rows and columns.
# # iloc: Integer-based selection method in Pandas for rows and columns.

# # Selecting Multiple rows
# df = pf.loc[[0,1]]
# print(df, sep=' ')

# # Selecting Multiple rows using Slicing
# df = pf.loc[0:1]
# print(df, sep=' ')

# # Selecting Multiple rows of a specific column using loc
# df = pf.loc[[0,1],'Order ID']
# print(df, sep=' ')

# # Selecting Multiple rows of a specific column using iloc
# df = pf.iloc[[0,1],1]
# print(df, sep=' ')

# # Selecting Multiple rows from Multiple columns using loc
# df = pf.loc[[0,1],['Order ID','Order Date']]
# print(df, sep=' ')

# # Selecting Multiple rows from Multiple columns uinsg iloc
# df = pf.iloc[[0,1],[0,1]]
# print(df, sep=' ')

# # Printing a particular column details
# df = pf['Order Date']
# print(df, sep=' ')

# # To extract a particular column value
# print(pf.loc[0:3,'Order Date'])
# print(pf[['Order Date']].head(3))
# print(pf[['Order Date','Order ID']].head(2))

# # Adding a new column
# pf['Original Returns']=round(pf['Profit']/pf['Cost']*pf['Quantity'])
# print(pf)

# # Setting an Index and fetching a particular record
# df = pf.set_index('Order ID')
# print(df.loc[[1,2]])

# # How to drop a row
# print(df.drop(1,axis=0))

# ## Condition Filtering
# # 1. In Pandas, condition filtering is a common operation where you filter rows from a DataFrame based on specific conditions or criteria. 
# # 2. You can achieve this using boolean indexing or the query() method.

# # Boolean Indexing
# # You can create a boolean Series that represents the condition you want to filter on and then use this Series to filter the DataFrame.
# # Example: df[df['Age'] > 25]

# # Query() Method
# # The query() method allows you to filter a DataFrame using a query expression.
# # Example: df.query('Age > 25')

# # Boolean Filter
# # Filter a Particular Customer details
# df = pf[(pf['Customer Name'] =='Adam Harte')]
# print(df)

# df = pf[(pf['Customer Name']).isin(['Adam Harte','Joel Mckean'])]
# print(df[['Order ID','Order Date','Customer Name']])

# # Filter a Multiple Customer details (OR Condition |)
# df = pf[(pf['Customer Name'] =='Adam Harte') | (pf['Customer Name']=='Joel McKean')]
# print(df)

# # Display the count of orders placed between the 2020-01-01 to 2020-01-31 ( And Operator)
# df = pf[(pf['Order Date']>'2020-01-01') & (pf['Order Date'] <='2020-01-31')]
# print(df)

# # Filter all the customer details whose Name starts with C
# df = pf[pf['Customer Name'].str.startswith('C')]
# print(df)

# # Filter all the customer details whose Name has letter 'a' at 3rd position
# df = pf[pf['Customer Name'].str[3]=='a']
# print(df)

# # Display the count of orders placed between the 2020-01-01 to 2020-01-31
# df = pf[(pf['Order Date']>'2020-01-01') & (pf['Order Date'] <='2020-01-31') | (pf['Customer Name'].str.startswith('Ka'))].count()
# print(df['Order ID'])

# # Display the orders placed between the 2020-01-01 to 2020-01-31 except the Customer name starts with 'Ka' (Not Operator)
# df = pf[(pf['Order Date']>'2020-01-01') & (pf['Order Date'] <='2020-01-31') & (~pf['Customer Name'].str.startswith('Ka'))]
# print(df)

# # Display the total no of orders placed between the 2020-01-01 to 2020-01-31 except the Customer name starts with 'Ka'
# df = pf[(pf['Order Date']>'2020-01-01') & (pf['Order Date'] <='2020-01-31') & (~pf['Customer Name'].str.startswith('Ka'))]
# print(df.groupby('Order Date').size())

# # Any, All and IN

# # How to find the Multiple values 
# df = pf[pf['Customer Name'].isin(['Ruby Patel','Jose Gambino'])]
# print(df)

# value = ['Ruby Patel','Jose Gambino']
# df = pf[pf['Customer Name'].isin(value)]
# print(df)


# df = pf[pf['Order Date'].isin(['2020-01-01','2023-01-02'])]
# ef = df[['Order Date','City']]
# print(ef)

# # How to find all the Order details related to City Pantin
# df = pf[pf['Order Date'].isin(['2020-01-01','2023-01-02']) & (pf['City']=='Pantin')]
# ef=df[['Order Date','City']]
# print(ef)

# # Any and All

# # Sorting
# # Ascending & Descending Order 

# # Display all the records in desc order based on Order Date
# df = pf.sort_values('Order Date', ascending =True )
# print(df)

# # Display all the records in asc order based on Order Date
# df = pf.sort_values('Order Date', ascending =False)
# print(df)

# # How to sort multiple fields
# df = pf.sort_values(['Order Date', 'City'])
# print(df)

# # How to Sort Mutliple fields in Ascending and Desending order
# df = pf.sort_values(['Order Date', 'City'], ascending=[False, True])
# print(df)

# df = pf.sort_values(['Order Date', 'City'], ascending=False)
# print(df)

# df = pf.sort_values(['Order Date', 'City'], ascending=[True, False])
# print(df)

# sorted_value = pf.sort_values(['Order ID', 'Profit'], ascending=[False, True])
# print(sorted_value)
# print(sorted_value.iloc[1])

# sorted_df = pf.apply(lambda x: x.sort_values(ascending=True) if x.name == ['Order ID','Profit'] else x)
# print(sorted_df.iloc[3])

# # Aggregate Functions - Min, Max, count, Length, Sum, mean
# df = pf['Order Date'].min()
# print(df)

# df = pf['Profit'].min()
# print(df)

# df = pf['Profit'].idxmin()
# print(df)

# df = pf['Profit'].max()
# print(df)

# df = pf['Profit'].idxmax()
# print(df)

# df = pf['Order Date'].max()
# print(df)

# df = pf[pf['Order Date']=='2020-01-01' ].count()
# ef = df['Order ID']
# print(ef)

# df = pf['Profit' ].sum()
# print(df)

# df = pf[(pf['Profit']) & (pf['City']=='Pantin')]
# ef=df['Profit'].sum()
# print(ef)

# Average
# df = pf[(pf['Profit']) & (pf['City']=='Pantin')]
# ef=df['Profit'].mean()
# print(ef)

# # Length
# df = pf[pf['City']=='Pantin']
# ef = df['Customer Name'].str.len()
# print(ef)

# # Value_counts, unique, nunique, duplicated, map, 

# Dataseries = {
#      'Emp_id':[100,101,102,103,104,104]
#      ,'FirstName':['King','John','Blake','Scott','Smith','Smith']
#      ,'LastName':['Solomon','Smith',None,None,None,None]
#      ,'Mgr':[100,101,100,102,103,103]
#      ,'Sal':[12000,12001,12000,10000,12000,12000]
#      ,'Designation':['Accountant','Accountant','BA','Devloper','Tester','Tester']
#      ,'Hiredate':['1993-01-01','1998-01-01','1996-01-01','1997-01-01','2000-01-01','2000-01-01']    
# }


# pf= pd.DataFrame(Dataseries)

# # What is value_Counts()
# # value_counts() is used to count the frequency of unique values in a Series.

# print(pf.value_counts()) #2

# # What is count()
# # while count() is used to count the number of non-null values in a DataFrame or Series. 
# print(pf.count()) #5

# # How to find the Distinct values
# print(pf['Mgr'].unique())

# # How to find the number of unquie values
# print(pf['Mgr'].nunique())

# # How to replace a value
# df = pf['Emp_id'].replace(100, 1001)
# print(df)

# # How to replace a mutliple values
# df = pf['Emp_id'].replace([100,101],[1000,1001])
# print(df)

# # How to replace multiple values in mutliple coulmns
# replace_values = {100:'1000', 101:'1001', 'King':'King A', 'John':'John A'}
# pf[['Emp_id','FirstName']] = pf[['Emp_id','FirstName']].replace(replace_values)
# print(pf)

# # we first define the replace_values dictionary to specify the mappings. 
# # Then, we apply the replace method to the subset of columns 'Emp_id' and 'FirstName' in the DataFrame

# # How to filter the records based on a particular condition
# df=pf[pf['Designation'].isin(['Tester','Accountant'])]
# print(df)

# # How to find the duplicates
# print(pf.duplicated())

# # How to list the duplicate recods
# df=pf[pf.duplicated()]
# print(df.head())

# # How to find the duplicates
# df=pf[pf.duplicated(keep=False)]
# print(df)

# ef=pf[pf.duplicated(keep='last')] #Mark the last occurrence as the only duplicate
# print(ef)

# df=pf[pf.duplicated(keep=False)] #Mark all occurrence as the only duplicate
# print(df)

# ef=pf[pf.duplicated(keep='first')] #Mark the first occurrence as the only duplicate
# print(ef)

# # Between And
# df = pf['Sal'].between(1000,5000)
# print(df)

# df = pf[pf['Sal'].between(1000,5000)]
# print(df)

# # nlargest, nsmallest

# Display the 2nd max salary
# df = pf.nlargest(2,'Sal')
# print(df)

# Display the 2nd Minimum Salary

# df = pf.nsmallest(2,'Sal')
# print(df)

# Display the 2nd smallest profit in the Country Itally
# ef = pf[(pf['Country']=='Italy')]
# df = ef['Profit'].nsmallest(2).iloc[-1]
# af = ef[ef['Profit']==df]
# print(af)

# Display the 10th larget profit in the country Itally

# ef = pf[(pf['Country']=='Italy')]
# df = ef['Profit'].nlargest(10).iloc[-1]
# af = ef[ef['Profit']==df]
# print(af)

# print(pf.iloc[:2])
# print(pf['Profit'].sum())  #626967
# print(pf['Profit'].max()) #3460
# print(pf['Profit'].min()) #1
# print(pf['Profit'].mean()) #152.36136087484812
# print(pf['Profit'].median())
# print(pf['Profit'].nlargest(10))
# print(pf['Sal'].nsmallest(2))
# print(pf.nsmallest(2,'Sal'))
# print(pf['Profit'].idxmax()) #3460
# print(pf['Profit'].idxmin()) #1
# print(pf.isnull())
# print(pf['Emp_id'].is_unique)
# print(pf['Sal'].add(100)) 
# print(pf['Sal'].duplicated())

# How to print Null values under the field 'LastName'
# ef = pf['LastName']
# print(ef.isnull())
# print(pf[ef.isnull()])

# Display all the records of Not null 
# ef = pf['LastName'].notnull()
# print(pf[ef])

# Display the records where LastName isNull() and FirstName isnotnull()
# print(pf[(pf['LastName'].isnull()) & (pf['FirstName'].notnull())])

# What is ISNULL, ISNA
# pf['LastName']=pf['LastName'].apply(lambda x: x if x is not None else float('Nan'))

# print(pf[pf['LastName'].isnull()])
# print(pf.isna())
# print(pf.fillna('XYZ'))

# Grouping Function in Pandas
# Display the total no. of employees working in each department

data = {
    'empid': [101, 102, 103, 104, 105, 106, 107, 108, 109],
    'firstname': ['John', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah'],
    'lastname': [None, 'Johnson', 'Williams', 'Brown', 'Davis', 'Lee', 'Wilson', 'Allen', 'Adams'],
    'sal': [None, 45000, 75000, None, 75000, 68000, 43000, 59000, 58000],
    'deptno': [None, 2, 1, 3, 1, 3, 1, 1, 3],
    'manager': [None, 101, None, None, 102, 103, np.nan, 101, 102],
    'hiredate': [None, '2022-03-10', '2022-02-20', '2022-04-05', '2022-03-01', '2022-05-12', '2022-01-20', '2022-02-15', '2022-03-25'],
    'technology': [None, 'Java', 'SQL', 'JavaScript', 'Python', 'Java', 'SQL', 'C++', 'Python'],
    'location': [None, None , 'New York', 'Los Angeles', 'San Francisco', 'Los Angeles', 'New York', 'San Francisco', 'Los Angeles'],
    'age': [33,36,26,24,23,'20',np.nan,None,0], 
    'date': ['2020-12-01 08-PM','2014-02-25 11-AM','2018-06-28 09-AM','2003-10-22 02-PM','2004-09-19 05-PM','2001-06-01 08-PM',
             '2023-03-29 12-PM','2010-12-25 10-PM','2010-12-25 10-PM']
}

df = pd.DataFrame(data)
pd.set_option('Display.max_column',None)
pd.set_option('Display.max_row', 20)

grouped_data = df.groupby(['deptno'])
pf = grouped_data['empid'].count()
print(pf)

# Display the no of employees working in each deptno with location
ef = df.groupby(['deptno','location'])
print(ef[['location']].count())

# Display the total salary for each deparment
grouped_data = df.groupby(['deptno'])
pf = grouped_data['sal'].sum()
print(pf)

# Dispaly the Dept whose total no of employees are greater than 3
grouped_data = df.groupby(['deptno'])
pf = grouped_data['empid'].count()>3
print(pf)

# Another method
grouped_data = df.groupby('deptno')
pf = grouped_data['empid'].count()
ef = pf[pf > 3]
print(ef)

# Display total sal of employees whose location is Newyork

grouped_data = df.groupby('location')
pf = grouped_data['sal'].sum()
print(pf)

# Display the total sal whose technology is SQL and location is New York
grouped_data = df.groupby(['location', 'technology'])
pf = grouped_data['sal'].sum()
ef = pf.loc['New York','SQL']
print(ef)

# Display total sal under the Location New York
grouped_data = df.groupby(['location', 'technology'])
pf = grouped_data['sal'].sum()
ef = pf.loc['New York']
print(ef)

# Display total sal under the Location San Fransico and New York
grouped_data = df.groupby(['location', 'technology'])
pf = grouped_data['sal'].sum()
ef = pf.loc[['San Francisco','New York']]
print(ef)

# Display the duplicate sal in each dept
grouped_data = df.groupby(['deptno', 'sal'])
ef = grouped_data['deptno']
print(ef.count()>=2)

grouped_data = df.groupby(['deptno', 'sal'])
ef = grouped_data['deptno'].count()
print(ef[ef>=2])

# Data Cleansing and handling missing values
# How to drop the null values in data frame
pf = df.dropna()
print(pf)

#Note: How to make the changes permanently
pf = df.dropna(inplace=True)
print(pf)  # None (check)

# Replacing an empty value to a user-defined value
pf = df.fillna('XYZ', inplace=True)
print(pf)

pf = df['location'].fillna('XYZ', inplace=True)
print(pf)

ef = df.dropna(axis='index', how='all')
print(ef)

ef = df.dropna(axis='index', how='any')
print(ef)

ef = df.dropna(axis='columns', how='all')
print(ef)

ef = df.dropna(axis='index', how='any', subset=['manager'])
print(ef)

ef = df.dropna(axis='index', how='all', subset=['sal','manager'])
print(ef)

# Replacing values to a specific column

df['firstname'] = df['firstname'].replace('John','John S')
print(df.head(1))

df['firstname'] = df['firstname'].replace({'John':'John S', 'Alice':'Alice A'})
print(df.head(3))

df['firstname'] = df['firstname'].replace(['John','Alice'],'John S')
print(df.head(2))

df[['firstname','lastname']] = df[['firstname','lastname']].replace({'John':'John S', 'Alice':'Alice A', 'Smith':'Smith S','Davis':'Davis D'})
print(df.head(5))

replaced_values = {'John':'John S', 'William':'Alice A', 'Smith':'Smith S','Davis':'Davis D'}
df[['firstname','lastname']] = df[['firstname','lastname']].replace(replaced_values)
print(df)

# Type Casting
# How to find the datatypes of each column
print(df.dtypes)

# How to change a field data type from Str to Int or float
print(df.dtypes)
df['age'] = df['age'].astype(float)
print(df.dtypes)

# DateTime Series
# How to find out the day or week or month from a date field
df['date']= pd.to_datetime(df['date'], format='%Y-%m-%d %I-%p')

print(df.loc[0,'date'].day_name())
print(df.loc[0,'date'].date())
print(df.loc[0,'date'].day_of_week)
print(df.loc[0,'date'].day_of_year)
print(df.loc[0,'date'].month_name())

# To display all the date into dayname
af = df['date'].dt.day_name()
print(af)

# To display the min date in the field
af = df['date'].min()
print(af)

# To display the max date in the field
af = df['date'].max()
print(af)

# To dispaly the no of employees joined between '2014-02-25' and '2020-12-01'
af = df['date'].between('2014-02-25','2020-12-01')
print(df[af])

# Display the employees who joined after 2015-12-31
df['hiredate']= pd.to_datetime(df['hiredate'], format='%Y-%m-%d')
print(df[df['hiredate']>='2015-12-31'])

#Method 2
ef = df['hiredate']>='2015-12-31'
print(df.loc[ef])

# Display the employees who joined after '2015-12-31' and '2020-12-31'
ef = ((df['hiredate']>='2015-12-31') & (df['hiredate']<='2020-12-31'))
print(df.loc[ef])

# Display the highest salary which is given for a employee whose hiredate is between '2020-01-01' and '2023-12-31'
df['hiredate'] = pd.to_datetime(df['hiredate'], format= '%Y-%m-%d')
ef = (df['hiredate']>='2020-01-01') & (df['hiredate']<='2023-12-31')
print(df[ef][['hiredate','sal']].max())

# Method 2
df['hiredate']= pd.to_datetime(df['hiredate'], format='%Y-%m-%d')
df.set_index('hiredate', inplace=True)
df.sort_index(inplace=True)

print(df['2020':'2022'])
print(df['2020':'2022']['sal'].sum())
print(df['2020':'2022']['sal'].max())
print(df['2020':'2022']['sal'].min())
print(df['2020':'2022']['sal'].count())

# Reading JSON files
df.to_json('json_data',orient='columns')

json_read = pd.read_json('json_data',orient='columns')
ef = json_read
pf = ef['hiredate']>'2020-01-01'
print(ef[pf])