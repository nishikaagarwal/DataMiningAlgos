


centroid = [3,4]
data = [
    [6,8],
    [2,6],
    [6,5],
    [8,2],
]


distance = []

for point in data:
    sumsq=0
    for i in range(0, len(point)):
        sumsq = sumsq + pow((centroid[i]-point[i]),2)
    distance.append(pow(sumsq,0.5))

print(distance)
