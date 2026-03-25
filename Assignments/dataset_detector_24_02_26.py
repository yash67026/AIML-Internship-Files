import pandas as pd
import os

# Get directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Take file name from user
file_name = input("Enter dataset file name (with .csv extension): ")

# Build full path safely
file_path = os.path.join(script_dir, file_name)

# Load dataset
dataset = pd.read_csv(file_path)

# Display top 5 rows
print("\nTop 5 rows of the dataset:")
print(dataset.head())

# Numeric columns only
numeric_data = dataset.select_dtypes(include='number')

# Highest value column
highest_value_column = numeric_data.max().idxmax()
highest_value = numeric_data[highest_value_column].max()

print("\nColumn with highest value:", highest_value_column)
print("Highest value:", highest_value)

# Missing values
print("\nMissing values in each column:")
print(dataset.isnull().sum())