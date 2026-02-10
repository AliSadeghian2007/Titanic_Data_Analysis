import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv('F:/Datasets/Titanic/train.csv')
df.info()
print(df['Age'].isnull().value_counts())
df.dropna(subset=['Age'],how='any',inplace=True)
## if you said df['Age'].dropna() it makes a series but the up line save it into data_frame
def Age_Group(A):
    if A<=12:
        return 'kid'
    elif  A<=60:
        return 'adult'
    else:
        return 'elder'
df['AgeGroup']=df['Age'].apply(Age_Group)
Survival_Group_Age=df.groupby('AgeGroup')['Survived'].mean()
print(Survival_Group_Age)
Survival_Group_Age=Survival_Group_Age.reindex(['kid','adult','elder'])
Survival_Group_Age.plot(kind='bar')
plt.ylim(0,1)
plt.xlabel('Age_Group')
plt.ylabel('Survival')
plt.title("Survival_For_All_Group_Age")
for i , j in enumerate(Survival_Group_Age):
    plt.text(i,j,round(j,2),ha='center')
plt.show()