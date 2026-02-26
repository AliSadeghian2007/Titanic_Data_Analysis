import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('../../data/train.csv')
df.info()
print(df['Name'].head(10))
def get_Title(name):
    return name.split(',')[1].split('.')[0].strip()
df['Title']=df['Name'].apply(get_Title)
x=df['Title'].value_counts()
##x=df.groupby('Title')['Title'].count().sort_values(ascending=False)
print(x)
common_title=['Mr','Miss','Mrs','Master']
def clean_title(title):
    if title in common_title:
        return title
    else:
        return "Rare"
df['Title']=df['Title'].apply(clean_title)
print(df['Title'].value_counts())

pivot=df.pivot_table(
    index='Title',
    values='Survived',
    aggfunc='mean'
)
ax=pivot.plot(kind='bar')
for i in ax.containers:
    for bar in i:
        height=bar.get_height()
        if pd.isna(height)==False:
            plt.text(bar.get_x()+bar.get_width()/2,height+0.01,round(height,2),ha='center')

plt.title('Name_Title Survival',fontdict={'fontsize':12})
plt.xlabel('Name_Title',fontdict={'fontsize':12})
plt.ylabel('Survival',fontdict={'fontsize':12})
plt.xticks(rotation=45)
plt.ylim(0,1)
plt.tight_layout()
plt.show()
