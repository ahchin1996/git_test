import pandas as pd
from _datetime import datetime
fd_path =  'D:/Time_Series_Research/new_data/GSPC/GSPC_2004.csv'
df = pd.read_csv(fd_path, sep=',', header=0)
date_array = pd.to_datetime(df['Date'] )
year = eval(input("Input current year!"))
split_no = 0
while date_array.iloc[split_no] < datetime(year, 11, 1, 0, 0):
    split_no += 1
print(split_no)

all_len = len(date_array)

print(all_len - split_no)

# all are non-important
