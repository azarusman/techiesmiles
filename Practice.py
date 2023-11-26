import pandas as pd
import numpy as np

data = {

    'empid': [101, 102, 103, 104, 105, 106, 107, 108, 109],
    'firstname': ['John', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah'],
    'lastname': [None, 'Johnson', 'Williams', 'Brown', 'Davis', 'Lee', 'Wilson', 'Allen', 'Adams'],
    'sal': [None, 45000, 75000, None, 75000, 68000, 43000, 59000, 58000],
    'deptno': [None, 2, 1, 3, 1, 3, 1, 1, 3],
    'manager': [None, 101, None, None, 102, 103, np.nan, 101, 102],
    'hiredate': ['1900-01-01', '2022-03-10', '2022-02-20', '2022-04-05', '2010-03-01', '2022-05-12', '2022-01-20', '2022-02-15', '2022-03-25'],
    'technology': [None, 'Java', 'SQL', 'JavaScript', 'Python', 'Java', 'SQL', 'C++', 'Python'],
    'location': [None, None , 'New York', 'Los Angeles', 'San Francisco', 'Los Angeles', 'New York', 'San Francisco', 'Los Angeles'],
    'age': [33,36,26,24,23,'20',np.nan,None,0], 
    'date': ['2020-12-01 08-PM','2014-02-25 11-AM','2018-06-28 09-AM','2003-10-22 02-PM','2004-09-19 05-PM','2001-06-01 08-PM',
             '2023-03-29 12-PM','2010-12-25 10-PM','2010-12-25 10-PM']

}

df = pd.DataFrame(data)
pd.set_option('Display.max_column',None)
pd.set_option('Display.max_row', 20)

# Reading JSON files
df.to_json('json_data',orient='columns')
json_read = pd.read_json('json_data',orient='columns')
ef = json_read
pf = ef['hiredate']>'2020-01-01'
print(ef[pf])