import pandas as pd 
df=pd.read_csv('F:/Datasets/Titanic/train.csv')
print(df['Sex'].value_counts())
live=df['Survived']==1
print(df[live]['Sex'].value_counts())
sex=df['Sex'].sort_index().value_counts()
num_sex_live=df[live]['Sex'].sort_index().value_counts()
print(((num_sex_live['female']/sex['female'])*100))
print(((num_sex_live['male']/sex['male'])*100))
x=df.groupby('Sex')['Survived'].mean()
print(x)
##groupbyدر واقع میاد دو کروه زن و مرد میسازه و رو هر کدوم میانگین میگیره 