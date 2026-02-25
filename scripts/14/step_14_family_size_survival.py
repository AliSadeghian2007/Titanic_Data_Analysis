import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('../../data/train.csv')
df.info()
df['FamilySize']=df['Parch']+df['SibSp']+1
def family_group(S):
    if S==1:
        return "Alone"
    elif S<=4:
        return 'Small'
    else :
        return 'Large'
df['FamilyGroup']=df['FamilySize'].apply(family_group)
pivot=df.pivot_table(
    index='FamilyGroup',
    values='Survived',
    aggfunc='mean'
)
pivot=pivot.reindex(['Alone','Small','Large'])
ax=pivot.plot(kind='bar')
for i in ax.containers:
    for bar in i:
        height=bar.get_height()
        if pd.isna(height)==False:
            plt.text(bar.get_x()+bar.get_width()/2, height+0.01,round(height,2),ha='center')
plt.title('FamilyGroup Survival',fontdict={'fontsize':14})
plt.xlabel('FamilyGroup',fontdict={'fontsize':14})
plt.ylabel('Survival',fontdict={'fontsize':14})
plt.xticks(rotation=45)
plt.ylim(0,1)
plt.tight_layout()
plt.show()