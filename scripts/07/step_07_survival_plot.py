import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv('F:/Datasets/Titanic/train.csv')
print(df.groupby('Sex')['Survived'].mean())
Survival=df.groupby('Sex')['Survived'].mean()
Survival_rate=Survival.plot(kind='bar')
plt.title("survival")
plt.xlabel='Sex'
plt.ylabel='Survival Rate'
for i ,j in enumerate(Survival):
    plt.text(i,j,round(j,2),ha='center')
plt.show()