import pandas as pd

# Take dataset file name from user
file_name = input("Enter dataset file name (with .csv extension): ")

# Load dataset
dataset = pd.read_csv(file_name)

# Display top 5 rows
print("\nTop 5 rows of the dataset:")
print(dataset.head())

# Select only numeric columns
numeric_data = dataset.select_dtypes(include='number')

# Find column with highest value
highest_value_column = numeric_data.max().idxmax()
highest_value = numeric_data[highest_value_column].max()

print("\nColumn with highest value:", highest_value_column)
print("Highest value:", highest_value)

# Count missing values
missing_values = dataset.isnull().sum()

print("\nMissing values in each column:")
print(missing_values)
