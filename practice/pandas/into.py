import pandas as pd 

# mydataset = {
#     'cars':["BMW","Volvo","Ford"],
#     'passings' : [3,7,2]
# }
# myvar = pd.DataFrame(mydataset)
# print(myvar)
'''
o/p:
    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2'''
#***************Series*************
# s = pd.Series([10,20,30,40])
# print(s)
'''
o/p:
0    10
1    20
2    30
3    40
dtype: int64'''

# s= pd.Series([10,20,30],index = ["a","b","c"])
# print(s)
'''
o/p:
a    10
b    20
c    30
dtype: int64'''
# calories = {"day1": 420,"day2": 380,"day3":390}
# myvar = pd.Series(calories)
# print(myvar)
'''
o/p:
day1    420
day2    380
day3    390
dtype: int64'''

# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories, index = ["day1"])
# print(myvar)

'''o/p:
day1    420
dtype: int64
'''
# data = {
#     "calories": [420,380,390],
#     "duration": [50,40,45]
    
# }

# myvar = pd.DataFrame(data)
# print(myvar)
# print(myvar.loc[[0,1]])
# print(myvar.loc[0])
'''
o/p:
       calories  duration
0       420        50
1       380        40
2       390        45
   calories  duration
0       420        50
1       380        40
calories    420
duration     50
Name: 0, dtype: int64
'''
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

#df = pd.DataFrame(data)
# df.to_csv('data.csv',index = False)# omits index in the csv file that created
# df = pd.read_csv('data.csv')

#print(df) 
'''
o/p:      Name  Age      City
0    Alice   25  New York
1      Bob   30    London
2  Charlie   35     Paris
'''
#print(df.to_string()) 

#print (pd.options.display.max_rows)

# pd.options.display.max_rows = 9999
# df = pd.read_csv('data.csv')
# print(df) 

df = pd.DataFrame(data)
df.to_json('data.json', orient='records', indent=2)
df = pd.read_json('data.json')

#print(df.to_string())
'''      Name  Age      City
0    Alice   25  New York
1      Bob   30    London
2  Charlie   35     Paris'''

#print(df.tail())
'''      Name  Age      City
0    Alice   25  New York
1      Bob   30    London
2  Charlie   35     Paris'''

#print(df.info())
'''<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Name    3 non-null      object
 1   Age     3 non-null      int64
 2   City    3 non-null      object
dtypes: int64(1), object(2)
memory usage: 204.0+ bytes
None'''

# dates = pd.date_range('20230101',periods = 4)#it returns the next 4 days 
# data = pd.Series([100,200,150,300],index = dates)
# print(data)

s = pd.Series([1,2,None,4])
print(s)
print("-"*25)
s = s.fillna(0)
print(s)