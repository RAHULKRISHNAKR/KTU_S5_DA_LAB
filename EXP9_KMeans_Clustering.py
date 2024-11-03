'''
_________________ALGORITHM____________________________________________

Input:
A dataset of data points with multiple features
Number of clusters (k)
Steps:
Load Dataset

Read the dataset from a CSV file into a pandas DataFrame
Convert the DataFrame into a NumPy array
Set Number of Clusters

Prompt the user to enter the number of clusters (k)
Initialize Centroids

Randomly select k data points from the dataset as initial centroids
K-Means Clustering Algorithm

Iterate up to a maximum number of iterations (e.g., 100 times)
Assign Clusters:
Create empty clusters for each centroid
For each data point in the dataset:
Calculate the distance between the data point and each centroid
Assign the data point to the nearest centroid's cluster
Update Centroids:
Calculate the new centroids by taking the mean of all data points in each cluster
Check for Convergence:
If the centroids do not change, break the loop
Update Centroids:
Update the centroids for the next iteration
Convert Clusters for Plotting

Convert the clusters to NumPy arrays for plotting
Print Cluster Details

Print the data points in each cluster
Print the final centroids
Plot Clusters

Plot the data points in each cluster using different colors
Plot the centroids with a cross marker
Add title and labels to the plot
Output:
Data points in each cluster
Final centroids
Plot of the clusters and centroids
Example:
Input: Dataset of data points, k = 3
Output: Data points in each cluster, final centroids, and plot of the clusters and centroids
Notes:
Adjust the number of clusters (k) and maximum iterations based on your specific problem and dataset.
Ensure the dataset is in the correct format (data points with multiple features).
______________________________________________________________________
'''


import pandas as pd_
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Data/KMeans_Clustering.csv')

# Convert DataFrame to NumPy array
X = df.values

# Set the number of clusters
k = int(input("Enter the number of clusters:"))

# Randomly initialize centroids
centroids = X[np.random.choice(X.shape[0], k, replace=False)]

# K-Means clustering algorithm
for _ in range(100):  # Iterate up to 100 times
    # Create empty clusters
    clusters = [[] for _ in range(k)]
    
    # Assign each data point to the nearest centroid
    for x in X:
        # Calculate the distance between the point and each centroid
        distances = [np.sqrt(np.sum((x - centroid) ** 2)) for centroid in centroids]
        # Find the index of the nearest centroid
        cluster = np.argmin(distances)
        # Assign the point to the nearest centroid's cluster
        clusters[cluster].append(x)
    
    # Update centroids by calculating the mean of all points in each cluster
    new_centroids = np.array([np.mean(cluster, axis=0) for cluster in clusters])
    
    # Check for convergence (if centroids do not change)
    if np.all(centroids == new_centroids):
        break
    
    # Update centroids for the next iteration
    centroids = new_centroids

# Convert clusters to numpy arrays for plotting
clusters = [np.array(cluster) for cluster in clusters]

# Print cluster details
for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1}:")
    print(cluster)
    print()

# Print final centroids
print("Final Centroids:")
print(centroids)

# Plot the clusters
# Get a colormap with 'k' distinct colors from the 'tab10' colormap
# 'tab10' is a colormap with 10 distinct colors, suitable for categorical data
# 'k' is the number of clusters, so we get 'k' colors from the colormap
colors = plt.cm.get_cmap('tab10', k).colors

# Iterate over each cluster and its index
for i, cluster in enumerate(clusters):
    # Plot the data points in the cluster
    # cluster[:, 0] and cluster[:, 1] are the x and y coordinates of the data points
    # s=100 sets the size of the points
    # c=[colors[i]] sets the color of the points to the i-th color from the colormap
    # label=f'Cluster {i+1}' sets the label for the cluster in the legend
    plt.scatter(cluster[:, 0], cluster[:, 1], s=100, c=[colors[i]], label=f'Cluster {i+1}')

# Plot the centroids with a cross marker
# centroids[:, 0] and centroids[:, 1] are the x and y coordinates of the centroids
# s=300 sets the size of the centroids
# c='red' sets the color of the centroids to red
# marker='x' sets the marker style to a cross
# label='Centroids' sets the label for the centroids in the legend
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red', marker='x', label='Centroids')

# Add title and labels to the plot
plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()