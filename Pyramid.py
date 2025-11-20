import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
# Replace 'your_file.csv' with the path to your CSV file
data = pd.read_csv(r'C:\Users\Administrator\Downloads\Simba.csv')

# Check the first few rows of the DataFrame
print(data.head())

# Group by age and gender to get counts
age_gender_counts = data.groupby(['Age', 'Gender']).size().unstack(fill_value=0)

# Prepare data for the population pyramid
# Convert counts to percentages
age_gender_counts['total'] = age_gender_counts.sum(axis=1)
for col in age_gender_counts.columns[:-1]:  # Exclude 'total' from the following
    age_gender_counts[col] = (age_gender_counts[col] / age_gender_counts['total']) * 100

# Prepare data for plotting
male = -age_gender_counts['Male']  # Negative for left side of pyramid
female = age_gender_counts['Female']

# Create the figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the bars
ax.barh(age_gender_counts.index, male, color='blue', label='Male')
ax.barh(age_gender_counts.index, female, color='pink', label='Female')

# Add labels and title
ax.set_xlabel('Percentage of Respondents')
ax.set_ylabel('Age Groups')
ax.set_title('Population Pyramid of Informal Manufacturers')
ax.set_xticks(range(-100, 101, 20))
ax.set_xticklabels([str(abs(x)) for x in range(-100, 101, 20)])
ax.legend()

# Show the plot
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()