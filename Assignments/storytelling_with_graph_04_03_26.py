import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset: Study hours vs marks
data = {
    "Student": ["Arjun", "Yudhishthira", "Bheem", "Nakul", "Sahadev", "Karna", "Kunti"],
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8],
    "Marks": [97, 75, 80, 76, 7, 92, 98]
}

df = pd.DataFrame(data)

# ---------------- BAR CHART ----------------
plt.figure()
plt.bar(df["Student"], df["Marks"])
plt.title("Marks Scored")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# ---------------- PIE CHART ----------------
plt.figure()
plt.pie(df["Study_Hours"], labels=df["Student"], autopct="%1.1f%%")
plt.title("Study hours distribution")
plt.show()

# ---------------- HISTOGRAM ----------------
plt.figure()
plt.hist(df["Marks"], bins=5)
plt.title("Marks distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
