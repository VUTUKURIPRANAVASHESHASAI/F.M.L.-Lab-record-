import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load dataset
data = pd.read_csv("data.csv")

# 2. Input features and Target variable
X = data[['Hours_Studied', 'Attendance', 'Assignments']]
y = data['Result']

# 3. Split dataset into 80% Training and 20% Testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Create SVM model
model = SVC(kernel='linear')

# 5. Train model
model.fit(X_train, y_train)

# 6. Predict
y_pred = model.predict(X_test)

# Define target categories explicitly to clean up console warnings
all_labels = ['Fail', 'Pass']

# 7. Print Evaluation Metrics
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred, labels=all_labels))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, labels=all_labels, zero_division=0))

# --- GENERATING THE EXACT CHART FROM THE PICTURE ---
# Convert the true string labels to numerical values (0 for Fail, 1 for Pass) for the graph Y-axis
y_test_numeric = y_test.map({'Fail': 0, 'Pass': 1})

plt.figure(figsize=(5, 4))
# Plots Hours Studied on the X-axis and numerical results on the Y-axis
plt.scatter(X_test['Hours_Studied'], y_test_numeric, label="Actual", color='tab:blue')

# Formatting to match the image title and layout parameters exactly
plt.title("SVM Classification")
plt.ylim(-0.1, 1.1)
plt.legend(loc="upper left")
plt.show()
