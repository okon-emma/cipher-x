import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('data.csv')

###number of clusters
k = 2

kmeans = KMeans(n_clusters=k)
kmeans = kmeans.fit(df)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print("Labels: ", end=" ")
print(labels)
