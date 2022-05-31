cluster1 = [
    [1,4],
    [2,6],
    [6,5],
    [8,2],
]

cluster2 = [
    [3,5],
    [7,7],
    [8,9],
    [1,4],
]



def findcentroid(cluster):
    centroid = []
    for j in range (0,2):
        sum = 0
        for i in range (0,len(cluster)):
            sum = sum + cluster[i][j]
        centroid.append(sum/len(cluster))
    return centroid
        
centroid1 = findcentroid(cluster1)
print(centroid1)

centroid2 = findcentroid(cluster2)
print(centroid2)