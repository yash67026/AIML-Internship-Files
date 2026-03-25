import pandas as pd
from sklearn.linear_model import LinearRegression

# Creating dataset
data = {
    "Study_Hours": [1,2,3,4,5,6,7,8],
    "Marks": [55,40,50,68,45,70,80,90]
}

df = pd.DataFrame(data)

# Labels
X = df[["Study_Hours"]]   # Feature
y = df["Marks"]           # Label

# T-mtodel
model = LinearRegression()
model.fit(X, y)

# Prediction
predicted_marks = model.predict(pd.DataFrame([[5]], columns=["Study_Hours"]))
print("Predicted marks for 5 study hours:", predicted_marks[0])
