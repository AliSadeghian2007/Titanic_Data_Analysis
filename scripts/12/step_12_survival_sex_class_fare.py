import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../../data/train.csv')
df = df.dropna(subset=['Sex', 'Pclass', 'Fare'])
def fare_group(price):
    if price < 10:
        return "Low"
    elif price <= 50:
        return "Medium"
    else:
        return "High"

df['FareGroup'] = df['Fare'].apply(fare_group)

# Pivot table
### Create a pivot table to analyze survival rate
# Rows: Sex and FareGroup
# Columns: Passenger Class
# Values: Mean survival rate
pivot = df.pivot_table(
    values='Survived',
    index=['Sex', 'FareGroup'],
    columns='Pclass',
    aggfunc='mean'
)
ax = pivot.plot(kind='bar')
plt.title('Survival Rate by Sex, Fare Group and Passenger Class')
plt.xlabel('Sex and Fare Group')
plt.ylabel('Survival Rate')
plt.grid(axis='y')

# Add value labels with smaller font
for container in ax.containers:
    for bar in container:
        height = bar.get_height()
        if not pd.isna(height):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height + 0.01,
                round(height, 2),
                ha='center',
                fontsize=8  
            )

plt.tight_layout()
plt.show()