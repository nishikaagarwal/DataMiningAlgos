import numpy as np
import pandas as pd
import math
import warnings

'''
K-Means Algorithm for the use
1 -> Read the data 
2 -> Take input of k
3 -> randomly assign k centroids
4 -> find average and iterate 
5 -> if the prev centroids and the current centroids are same then end

'''

def assign_centres(k : int, df ):
    random_array = df.sample(n=k)
    return random_array


def find_cluster_no(pos_matrix):
    positions = np.argmin(pos_matrix, axis=0)
    return positions

def calc_distance(pos_matrix, data, centers, k):
    for i in range(0, k):
        for row in range(0, len(data)):
            sub = []
            for j in range(0, len(data[row])):
                sub.append(data[row][j] - centers[i][j]) 
            sumsq = math.sqrt(sum([s**2 for s in sub]))
            pos_matrix[i][row] = sumsq

        # pos_matrix[i] = np.sqrt(np.sum(np.square(data - centers[i]), axis=1))
        
    return find_cluster_no(pos_matrix)

def find_mean(dataset, positions, k):
    cluster_sub_data = []
    for j in range(0, len(positions)):
        if positions[j] == i:
            cluster_sub_data.append(dataset[j])
    new_cent = [0 for x in dataset[0]]
    for row in range(0, len(cluster_sub_data)):
        for col in range(0, len(cluster_sub_data[row])):
            new_cent[col] += cluster_sub_data[row][col]
    for ele in range(0, len(new_cent)):
        new_cent[ele]/=len(cluster_sub_data)
    return new_cent



if __name__=="__main__":
    warnings.simplefilter("ignore", category=RuntimeWarning)

    k = int(input("Enter value of k: "))
    iter = 0
    df = pd.read_csv(r'test-class-kmeans.csv')
    dataset = np.array(df)

    k_clusters = np.array(assign_centres(k, df))
    prev_cluster = -1 * k_clusters.copy()

    pos_matrix = np.zeros((k, dataset.shape[0]))
    # calculate distances
    positions = calc_distance(pos_matrix, dataset, k_clusters, k)

    # new centroids = 
    
    while((prev_cluster!=k_clusters).all() and iter < 15):
        prev_cluster = k_clusters.copy()
        iter += 1
        for i in range(0, k):
            # k_clusters[i] = np.mean(dataset[np.nonzero(positions == i)], axis=0)
            k_clusters[i] = find_mean(dataset, positions, k)

            pos_matrix = np.zeros((k, dataset.shape[0]))
            # calculate distances
            positions = calc_distance(pos_matrix, dataset, k_clusters, k)
    print("Final Centroids\n", k_clusters)
    print("Clusters\n", positions)
    

    