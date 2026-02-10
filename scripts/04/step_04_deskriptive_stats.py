import pandas as pd 
df=pd.read_csv('F:/Datasets/Titanic/train.csv')
print(df.info())
df1=df.select_dtypes(['Int64','Float64'])
print(df1.describe())
print(df['Age'].min())
print(df['Age'].max())
print(df['Age'].mean())
print(df['Age'].median())