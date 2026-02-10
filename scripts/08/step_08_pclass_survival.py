import pandas as pd
import matplotlib.pyplot as plt 
df=pd.read_csv('F:/Datasets/Titanic/train.csv')
##Pclass is class of Ticket
Survival_rate_Pclass=df.groupby('Pclass')['Survived'].mean()
print(Survival_rate_Pclass)
##as you can see class 1 has the most survival rate but the lowest was for class3
Survival_rate_Pclass.plot(kind='bar')
plt.xlabel('Pclass')
plt.ylabel('Survival_Rate')
for i , j in enumerate(Survival_rate_Pclass):
    plt.text(i,j,round(j,2),ha='center')
plt.ylim(0,1)
plt.show()
