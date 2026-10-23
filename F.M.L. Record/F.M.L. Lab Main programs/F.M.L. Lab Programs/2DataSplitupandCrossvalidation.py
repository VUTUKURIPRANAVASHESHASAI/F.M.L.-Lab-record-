import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.neighbors import KNeighborsClassifier

# 1. Load dataset
data = pd.read_csv("data.csv")

# 2. Define Features (Inputs) and Target (Output)
X = data[['Hours_Studied', 'Attendance', 'Assignments']]
y = data['Result']

# 3. Split data into 80% Training and 20% Testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Display Data Splits (showing first 5 rows to keep output clean)
print("--- Data Split Up ---")
print("Training Data Samples (First 5 rows):")
print(X_train.head())

print("\nTesting Data Samples (First 5 rows):")
print(X_test.head())

print(f"\nTraining Samples Count: {len(X_train)}")
print(f"Testing Samples Count: {len(X_test)}")

# 5. Create KNN Classifier Model
model = KNeighborsClassifier(n_neighbors=3)

# 6. Perform 5-Fold Cross Validation using standard KFold (removes the warning)
print("\n--- Cross Validation ---")
kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kf)

print("Cross Validation Scores:")
print(scores)

print("\nAverage Accuracy:")
print(scores.mean())
