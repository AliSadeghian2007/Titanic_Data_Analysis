import pandas as pd 
df=pd.read_csv('F:/Datasets/Titanic/train.csv')
print(df.columns)
survived=df['Survived'].value_counts().sort_index()
survived.index=['Dead','Live']
print(survived)
Dead_percent=((survived[0]/survived.sum())*100).round(2)
print(Dead_percent)
Live_percent=((survived[1]/survived.sum())*100).round(2)
print(Live_percent)
print(df['Survived'].mean())
##most of the people have been survived(survival rate by mean)
print(f"Most of the people {survived.idxmax()}")


##point:mean between 0 and 1 show percent