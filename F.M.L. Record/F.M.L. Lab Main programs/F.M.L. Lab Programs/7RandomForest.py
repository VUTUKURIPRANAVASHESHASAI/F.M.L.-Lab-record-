import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load dataset
data = pd.read_csv("data.csv")

# 2. Define Input features and Target variable
X = data[['Hours_Studied', 'Attendance', 'Assignments']]
y = data['Result']

# 3. Split dataset into 80% Training and 20% Testing sets 
# (Fixed the missing closing parenthesis syntax error here)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Create Random Forest Classifier Model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# 5. Train the model
model.fit(X_train, y_train)

# 6. Predict test data outcomes
y_pred = model.predict(X_test)

# Explicit target category tracking to clean up small dataset console warnings
all_labels = ['Fail', 'Pass']

# 7. Print Evaluation Metrics
print("--- Random Forest Model Evaluation ---")
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred, labels=all_labels))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, labels=all_labels, zero_division=0))

# 8. PICTURE GENERATION: Plot Feature Importance Graph
importance = model.feature_importances_

plt.figure(figsize=(7, 5))
plt.bar(X.columns, importance, color='teal', edgecolor='k', alpha=0.8)
plt.xlabel("Features")
plt.ylabel("Importance Score")
plt.title("Random Forest - Feature Importance Analysis")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
