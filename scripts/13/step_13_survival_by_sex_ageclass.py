import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../../data/train.csv')
df.dropna(subset=['Age','Sex','Pclass'],inplace=True)
def age_group(A):
    if A<=12:
        return "Kid"
    elif A<=60:
        return "Adult"
    else:
        return "Elder"
df['AgeGroup']=df['Age'].apply(age_group)
pivot=df.pivot_table(
    values='Survived',
    index=['AgeGroup','Sex'],
    columns='Pclass',
    aggfunc='mean'
)
ax=pivot.plot(kind='bar')
for i in ax.containers:
    for bar in i:
        height=bar.get_height()
        if pd.isna(height)==False:
            ax.text(bar.get_x()+bar.get_width()/2, height+0.01,round(height,2),ha='center',fontsize=8)
plt.title("Survival by sex and ageclass")
plt.xlabel("Sex and Age class")
plt.ylabel("Survival")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()