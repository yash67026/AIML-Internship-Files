import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "Area": [1000, 1500, 2000, 2500],
    "Bedrooms": [2,3,4,4],
    "Bathrooms": [1,2,3,3],
    "Price": [5000000,7500000,10000000,12500000]
}

df = pd.DataFrame(data)

# Features
X = df[["Area","Bedrooms","Bathrooms"]]
y = df["Price"]

# Train_the_Model
model = LinearRegression()
model.fit(X,y)

# Predict_New_House_Prices
new_house = [[1800,3,2]]
prediction = model.predict(new_house)

print("Predicted Price:", prediction[0])