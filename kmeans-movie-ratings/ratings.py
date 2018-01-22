#!/usr/bin/env python

from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

#import pdb
#pdb.set_trace()

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

""" load data and plot """
f = open("/mnt/zram/ratings.csv")
#f = open("r.csv")
f.readline()        # skip the header
data = np.loadtxt(f, delimiter=',')
X = data[:, :-1]    # ignore the 'timestamp' field
plt.figure()
plt.title("KMeans - ratings")
plt.xlabel("movie-id")
plt.ylabel("rating")
plt.grid()
plt.plot(X[:, 1], X[:, 2], 'bo', color='b', label='ratings')

""" compute the K-means cluster """
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
C = kmeans.cluster_centers_
plt.plot(C[:, 1], C[:, 2], 'bo', color='r', label='centroids')

plt.legend(loc="best")
plt.show()
