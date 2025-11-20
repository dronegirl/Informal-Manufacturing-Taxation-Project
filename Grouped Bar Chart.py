import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
data = pd.read_csv(r'C:\Users\Administrator\Downloads\Simba.csv')

# Check the first few rows of the DataFrame
print(data.head())

# Group the data by site and education/training type, then count
grouped_data = data.groupby(['site', 'Level of industrial training']).size().unstack(fill_value=0)

# Plotting
grouped_data.plot(kind='bar', figsize=(10, 6), width=0.8)

# Add chart elements
plt.title('Level of Industrial Training Among Manufacturers by Site')
plt.xlabel('Site')
plt.ylabel('Number of Respondents')
plt.xticks(rotation=0)
plt.legend(title='Education Level', bbox_to_anchor=(1.05, 1), loc='upper left')  # Adjust the legend

# Show the plot
plt.tight_layout()
plt.show()