import numpy as np
import pandas as pd
from sklearn.cluster import  KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from pysal.lib.weights import lat2W 
from pysal.explore.esda import Moran
from functions import define_names, grid_plot, cluster_plot

names=define_names()
data = pd.read_csv("../data/EDA_processed_data.csv")

# trasposizione dei dati
data_t = data.transpose()
new_header = data_t.iloc[1]
data_t = data_t[2:]
data_t.columns = new_header

# K-means
# correlation clusters
cluster_KM = KMeans(n_clusters=5,max_iter=6000,tol=0.0001)
cluster_KM.fit(data_t)
label = cluster_KM.labels_
cluster_plot(names,label,data)
plt.savefig("../../reports/figures/correlation_clusters.png",format = 'png')

clust_mat=label.reshape(11,11)
w = lat2W(clust_mat.shape[0], clust_mat.shape[1]) #genero i pesi (neares neighbours)
Imoran=[]
for a in np.unique(label):
    temp=clust_mat.copy()
    for i in range(0,11):
        for j in range (0,11):
            if temp[i,j]==a:
                temp[i,j]=1
            else:
                temp[i,j]=0
    moran=Moran(temp, w)
    Imoran.append(moran.I)
labels_moran=[round(Imoran[i],4) for i in label]
grid_plot(labels_moran)
plt.savefig("../../reports/figures/correlation_grid.png",format = 'png')

# Ineritia
cluster_KM = KMeans(n_clusters=6,max_iter=6000,tol=1e-4)
cluster_KM.fit(data_t)

# calcolo l'inertia per vari numeri di cluster
n_cluster=30 # max number of clusters
inertia=[]
bound = 0.001
cluster_KM = KMeans(n_clusters = 2,max_iter=6000,tol=1e-4)
cluster_KM.fit(data_t)
N_cluster=[]
for i in range(n_cluster):
    a=i+3
    d = cluster_KM.inertia_
    cluster_KM = KMeans(n_clusters =a,max_iter=6000,tol=1e-4)
    cluster_KM.fit(data_t)
    inertia.append(cluster_KM.inertia_)
    c = cluster_KM.inertia_
    diff = abs(c-d)
    if  diff < bound:
        N_cluster.append(a)
font = {'size': 15}
plt.rc('font',**font)
plt.figure(figsize=(14,6.5))
plt.scatter(list(np.array(range(n_cluster))+3),inertia)
plt.plot(list(np.array(range(n_cluster))+3),inertia)
plt.scatter(N_cluster[0],inertia[N_cluster[0]-3],s=150)
plt.xlabel("Number of cluster")
plt.ylabel("Inertia")
plt.savefig("../../reports/figures/number_cluster.png",format = 'png')

cluster_KM = KMeans(n_clusters=N_cluster[0],max_iter=6000,tol=1e-4)
cluster_KM.fit(data_t)
label = cluster_KM.labels_
cluster_plot(names,label,data)
plt.savefig("../../reports/figures/FIT_cluster.png",format = 'png')

# genero un pandas dataframe con i centroidi e salvo i dati
centres=pd.DataFrame(data.wn.copy())
for i in range(len(np.unique(label))):
    centres=centres.join(pd.DataFrame(cluster_KM.cluster_centers_[i],columns=[str(i)]))

centres.to_csv("../data/CLUSTERING_data_centres.csv")
np.savetxt("../data/CLUSTERING_labels.txt",label)