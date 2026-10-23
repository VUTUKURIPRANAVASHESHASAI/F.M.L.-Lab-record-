import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load dataset
data = pd.read_csv("data.csv")

# 2. Define Input features and Target variable
X = data[['Hours_Studied', 'Attendance', 'Assignments']]
y = data['Result']

# 3. Split dataset into 80% Training and 20% Testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Create KNN Classifier Model
model = KNeighborsClassifier(n_neighbors=3)

# 5. Train the model
model.fit(X_train, y_train)

# 6. Predict the target values for test set
y_pred = model.predict(X_test)

# Define all possible target categories explicitly to fix the warning
all_labels = ['Fail', 'Pass']

# 7. Print Evaluation Metrics
print("--- Model Evaluation ---")
print("Accuracy Score:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
# Added labels=all_labels to eliminate the warning
print(confusion_matrix(y_test, y_pred, labels=all_labels))

print("\nClassification Report:")
# Added labels=all_labels to make both Fail and Pass show up in the report
print(classification_report(y_test, y_pred, labels=all_labels, zero_division=0))
