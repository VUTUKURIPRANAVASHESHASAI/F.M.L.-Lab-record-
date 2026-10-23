import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# 1. Load dataset
data = pd.read_csv("data.csv")

# 2. Select numerical features for clustering
X = data[['Hours_Studied', 'Marks']]

# 3. Create hierarchical linkage matrix using Ward's method
linked = linkage(X, method='ward')

# 4. Plot the Dendrogram tree diagram
plt.figure(figsize=(8, 5))
dendrogram(linked)
plt.title("Dendrogram for Hierarchical Clustering")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.show()

# 5. Apply Hierarchical (Agglomerative) Clustering
hc = AgglomerativeClustering(n_clusters=3)
clusters = hc.fit_predict(X)

# 6. Append calculated cluster markers back into the dataset DataFrame
data['Cluster'] = clusters

print("--- Clustered Dataset Output ---")
print(data)

# 7. Generate Cluster Visual Scatter Plot distribution
plt.figure(figsize=(8, 5))
plt.scatter(X['Hours_Studied'], X['Marks'], c=clusters, cmap='rainbow', edgecolors='k', s=60)
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Hierarchical Clustering Assignments")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
