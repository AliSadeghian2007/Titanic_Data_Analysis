import pandas as pd 
df=pd.read_csv('F:/Datasets/Titanic/train.csv')
print(df.info())
print(df.select_dtypes(include=['Int64','float64']))
print(df.select_dtypes(exclude=['Int64','float64']))
##a way for counting number_columns
print(len(df.select_dtypes(include=['Int64','float64']).columns))
##another way for counting non_number_columns
x=df.select_dtypes(exclude=['int64','float64'])
print(x.shape[1])