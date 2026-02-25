# Titanic Survival Analysis 🚢

This repository contains a series of data analysis exercises based on the Titanic dataset.  
The goal of these exercises is to practice data cleaning, grouping, aggregation, and visualization using Python, Pandas, and Matplotlib.

---

## Dataset
The dataset used in this project is the Titanic dataset from Kaggle (train.csv).

---

## Exercises

### Exercise 1: Loading and Exploring the Dataset
- Loaded the Titanic dataset using Pandas.
- Inspected the dataset structure using info() and head().
- Identified numerical and categorical features.

---

### Exercise 2: Handling Missing Values
- Checked for missing values in different columns.
- Focused on columns with significant missing data such as Age.
- Understood the impact of missing values on analysis.

---

### Exercise 3: Basic Statistical Analysis
- Calculated basic statistics (mean, count).
- Explored the overall survival rate.
- Compared survival counts using simple aggregations.

---

### Exercise 4: Survival Rate by Gender
- Grouped passengers by Sex.
- Calculated the mean survival rate for each gender.
- Observed that females had a much higher survival rate than males.

---

### Exercise 5: Survival Rate by Passenger Class
- Grouped data by Pclass.
- Compared survival rates among different passenger classes.
- Found that 1st class passengers had the highest survival rate.

---

### Exercise 6: Combining Multiple Groupings
- Grouped passengers by both Sex and Pclass.
- Used groupby() with multiple columns.
- Applied unstack() to reshape the result for better readability.

---

### Exercise 7: Data Visualization
- Visualized survival rates using bar charts.
- Used Matplotlib to label axes and titles.
- Compared survival rates visually across groups.

---

### Exercise 8: Interpreting Visual Results
- Analyzed plotted charts to extract insights.
- Identified patterns and trends in survival data.
- Practiced drawing conclusions from visualized data.

---

### Exercise 9: Survival Rate by Sex and Class
- Calculated survival rates grouped by Sex and Pclass.
- Transformed grouped data for visualization.
- Plotted survival rates using bar charts.

---

### Exercise 10: Survival Rate by Age Groups
- Removed missing values from the Age column.
- Created custom age groups (Kid, Adult, Elder).
- Calculated and visualized survival rates for each age group.

---

### Exercise 11: Survival Rate by Fare Groups
- Grouped passengers based on ticket fare.
- Analyzed the relationship between fare price and survival rate.
- Observed that passengers who paid higher fares had better survival chances.

---

### Exercise 12: Survival by Sex, Fare Group, and Class
- Categorized ticket prices into three groups: Low (<10), Medium (10–50), High (>50).  
- Removed rows with missing Sex, Pclass, or Fare.  
- Used a pivot table to calculate mean survival rates for each combination of Sex, FareGroup, and Pclass.  
- Visualized results with a bar chart and added small value labels (fontsize=8) above each bar.  
- Observed survival patterns across gender, class, and fare group.

---

### Exercise 13: Survival by Sex, Age Group, and Class
- Removed missing values from the Age column.
- Created a new column AgeGroup (Kid ≤12, Adult 13–60, Elder >60).
- Used a pivot table to calculate mean survival rates for each combination of Sex, AgeGroup, and Pclass.
- Visualized the results using a bar chart.
- Added small value labels (fontsize=8) above each bar for clarity.
- Analyzed how age, gender, and passenger class together influenced survival.

---

### Exercise 14: Survival Rate by Family Size

- Created a new feature called FamilySize using SibSp and Parch.
- Engineered a categorical feature FamilyGroup (Alone, Small, Large).
- Calculated survival rates using pivot_table().
- Visualized survival patterns across different family sizes.
- Practiced feature engineering and categorical analysis.

---

## Tools & Libraries
- Python
- Pandas
- Matplotlib

---

## Notes
These exercises are intended for learning and practice in data analysis and visualization.
