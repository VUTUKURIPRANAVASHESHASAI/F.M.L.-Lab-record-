# 2. Pandas: Selection, Filtering, and Data Cleaning
import pandas as pd
import numpy as np

print("=== 4. PANDAS DATA FRAME CREATION ===")
# Raw dirty data with missing values (NaN)
raw_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', np.nan, 'Bob'],
    'Age': [25, np.nan, 30, 22, 28, np.nan],
    'Score': [85, 90, np.nan, 70, 95, 90],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Chicago', 'Los Angeles']
}
df = pd.DataFrame(raw_data)
print("Original DataFrame:\n", df)

print("\n=== 5. SELECTION & FILTERING ===")
# Selecting columns and filtering rows
print("Selecting 'Name' and 'Score' columns:\n", df[['Name', 'Score']])
filtered_df = df[df['Score'] > 80]
print("Filtering rows where Score > 80:\n", filtered_df)

print("\n=== 6. DATA CLEANING ===")
# Handling duplicates and missing values
print("Duplicate rows count:", df.duplicated().sum())
df_cleaned = df.drop_duplicates()
print("Filling missing scores with mean and dropping remaining NaNs...")
df_cleaned['Score'] = df_cleaned['Score'].fillna(df_cleaned['Score'].mean())
df_cleaned = df_cleaned.dropna(subset=['Name', 'Age'])
print("Cleaned DataFrame:\n", df_cleaned)
