import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv('F:/Datasets/Titanic/train.csv')
Sex_pclass_Survival=df.groupby(['Sex','Pclass'])['Survived'].mean().unstack()
##you have two index
##unstack set your second index to column
print(Sex_pclass_Survival)
##class1 and female has the most survival rate
Sex_pclass_Survival=Sex_pclass_Survival.transpose()
ax=Sex_pclass_Survival.plot(kind='bar')
plt.ylim(0,1)
for i , col in enumerate(Sex_pclass_Survival.columns):
    for j , val in enumerate(Sex_pclass_Survival[str(col)]):
        ax.text(j,val,round(val,2),ha='center')
plt.show()

