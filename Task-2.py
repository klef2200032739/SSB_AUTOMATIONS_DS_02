import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import StringIO

# Sample CSV content
csv_data = """Name,Age,Department,Salary
John,28,Sales,50000
Jane,34,Marketing,60000
Doe,45,HR,55000
Alice,30,IT,70000
Bob,50,Sales,80000
Charlie,32,IT,75000
Eve,29,Marketing,72000
Frank,33,HR,48000"""

# Load the CSV data into a DataFrame
df = pd.read_csv(StringIO(csv_data))

# Set the style for the plots
sns.set(style="whitegrid")

# Histogram of employee ages
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], kde=True, bins=10)
plt.title('Histogram of Employee Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Scatter plot of employee salaries by age
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Salary', hue='Department', data=df, s=100)
plt.title('Scatter Plot of Employee Salaries by Age')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend(title='Department')
plt.show()
