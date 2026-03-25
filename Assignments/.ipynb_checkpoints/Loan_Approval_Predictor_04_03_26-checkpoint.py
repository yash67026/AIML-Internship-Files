import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
data = {
    'Income': [50000, 80000, 30000, 120000, 45000, 95000],
    'Credit_Score': [600, 750, 520, 800, 580, 710],
    'Age': [25, 45, 22, 35, 30, 40],
    'Loan_Amount': [15000, 20000, 5000, 50000, 12000, 30000],
    'Employment_Years': [2, 10, 1, 15, 3, 8],
    'Target': [0, 1, 0, 1, 0, 1] # 0 = Denied, 1 = Approved
}

df = pd.DataFrame(data)
X = df.drop('Target', axis=1)
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Decision Tree
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)

# Train the Random Forest
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)

# Compare Accuracy
dt_acc = accuracy_score(y_test, dt_model.predict(X_test))
rf_acc = accuracy_score(y_test, rf_model.predict(X_test))

print(f"Decision Tree Accuracy: {dt_acc * 100}%")
print(f"Random Forest Accuracy: {rf_acc * 100}%")

# Show Random Forest
importances = pd.Series(rf_model.feature_importances_, index=X.columns)
print("\nFeature Importances:\n", importances.sort_values(ascending=False))

# Save Model using Pickle
with open('loan_rf_model.pkl', 'wb') as f:
    pickle.dump(rf_model, f)
print("\nModel saved successfully as 'loan_rf_model.pkl'")
