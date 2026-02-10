import pandas as pd 
df=pd.read_csv('F:/Datasets/Titanic/train.csv')
null_count=df.isnull().sum()
print (null_count)
print("Null values in each column : ")
print(null_count)

max_null_columns=null_count.idxmax()
print("the column with most nan value:")
print(max_null_columns)

no_null_columns=null_count[null_count==0]
print(list(no_null_columns.index))


