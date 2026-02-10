import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('f:/Datasets/Titanic/train.csv')
df.dropna(subset=['Fare'],inplace=True)
def Fare_Group(price):
    if price<10:
        return "Low"
    elif price<50:
        return "Medium"
    else:
        return "High"
df["FareGroup"]=df["Fare"].apply(Fare_Group)
FareGroup_Survival=df.groupby('FareGroup')['Survived'].mean()
print(FareGroup_Survival)
FareGroup_Survival=FareGroup_Survival.reindex(['High','Medium','Low'])
FareGroup_Survival.plot(kind='bar',color=['b','r','m'])
plt.xlabel('FareGroup')
plt.ylabel('Survival')
for i , j in enumerate(FareGroup_Survival):
    plt.text(i,j+0.01,round(j,2),ha='center')
plt.title('Survival rate by fare group')
plt.show()

