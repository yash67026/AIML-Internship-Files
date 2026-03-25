import pandas as pd

# Sample dirty dataset
data = {
    "Name": ["Anand", "Pranav", "BabuRao", None, "Nanda Gopal"],
    "City": ["Bangalore", "bangalore", "Mumbai", "Delhi", "Chennai"],
    "Marks": [85, None, 85, 70, 91]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# ---------------- HANDLE MISSING VALUES ----------------
df["Marks"].fillna(df["Marks"].mean(), inplace=True)

# ---------------- REMOVE DUPLICATES --------------------
df = df.drop_duplicates()

# ---------------- STANDARDIZE TEXT ---------------------
df["City"] = df["City"].str.title()

# ---------------- REMOVE NULL NAMES --------------------
df = df.dropna(subset=["Name"])

print("\nCleaned Dataset:")
print(df)