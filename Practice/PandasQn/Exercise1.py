import  pandas as pd
data = pd.read_csv("nba.csv")
data_top = data.head()
data_tail= data.tail()
print(data_top)
print(data_tail)

