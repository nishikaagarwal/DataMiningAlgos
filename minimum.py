from numpy import minimum


distances = [
    [10, 20],
    [5, 4],
    [4, 22],
    ]

positions = []

for row in distances:
    minimum = min(row)
    position = row.index(minimum)+1
    positions.append(position)

print(positions)



