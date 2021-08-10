from itertools import combinations
def makeDateColumns(df):
    # selecting columns with date data types
    date_columns= df.select_dtypes(include=[np.datetime64]).columns
    print("Dataframe with date columns are: ", date_columns)
    # creating a combination of a date columns.Example [ (date1,date2), (date1,date3), (date2,date3)]
    date_combination = list(combinations(date_columns, 2))
    for new_column in date_combination:
        a1 = str(new_column[0])
        a2 = str(new_column[1])
        column_name= a1 + '-' + a2
        df[column_name] = df[new_column[0]] - df[new_column[1]] # subtracting to calculate the difference


import pandas as pd
import numpy as np
date1 = pd.date_range('2019-04-15', periods=6, freq='D')
date2 = pd.date_range('2016-02-24', periods=6, freq='D')
date3 = pd.date_range('2019-05-18', periods=6, freq='D')
names = ['john','careter','peter','Nick','charlie','jonas']
df = pd.DataFrame({'Names':names, 'date1':date1, 'date2':date2,'date3':date3})
makeDateColumns(df)
print(df)
