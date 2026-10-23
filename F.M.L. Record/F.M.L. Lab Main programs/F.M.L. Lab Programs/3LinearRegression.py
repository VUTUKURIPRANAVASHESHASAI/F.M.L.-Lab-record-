import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load dataset
data = pd.read_csv("data.csv")

# 2. Define Input Feature (Independent Variable) and Target Variable (Dependent Variable)
X = data[['Hours_Studied']]
y = data['Marks']

# 3. Split dataset into 80% Training and 20% Testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Create Linear Regression model
model = LinearRegression()

# 5. Train the model
model.fit(X_train, y_train)

# 6. Predict test set values
y_pred = model.predict(X_test)

# 7. Evaluate model performance
print("--- Model Evaluation ---")
print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))
print("R2 Score (Coefficient of Determination):", r2_score(y_test, y_pred))

# 8. Display target predictions vs actual evaluations
print("\n--- Actual vs Predicted Marks ---")
for actual, pred in zip(y_test, y_pred):
    print(f"Actual Marks: {actual} -> Predicted Marks: {pred:.2f}")

# 9. Plotting the Regression Graph
plt.scatter(X_test, y_test, color='blue', label="Actual Data")
plt.plot(X_test, y_pred, color='red', linewidth=2, label="Regression Line")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Linear Regression Analysis")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
