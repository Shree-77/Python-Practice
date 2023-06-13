# Write a Pandas program to get the first 3 rows of a given DataFrame.
# Sample Python dictionary data and list labels:
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',
# 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


import pandas as pd

exam_Data={
    'name':['Anastasia', 'Dima','Katherine','james','Emily','Michael','Mathew',
            'Laura','Kevin','Jonas'],
    'score':[12.5, 9, 16.5, None, 9, 20, 14.5, None, 8, 19],
    'attempts':[1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify':['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
   }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

dataframe = pd.DataFrame(exam_Data,index=labels)



first_three_rows=dataframe.head(3)

print(first_three_rows)